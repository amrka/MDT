import pyopencl as cl
import numpy as np
from mot.utils import get_cl_pragma_double, set_correct_cl_data_type
from mot.cl_routines.base import AbstractCLRoutine
from mot.load_balance_strategies import Worker


__author__ = 'Robbert Harms'
__date__ = "2014-05-18"
__license__ = "LGPL v3"
__maintainer__ = "Robbert Harms"
__email__ = "robbert.harms@maastrichtuniversity.nl"


class CalculateEigenvectors(AbstractCLRoutine):

    def convert_theta_phi_psi(self, theta_roi, phi_roi, psi_roi):
        """Calculate the eigenvectors from the given theta, phi and psi angles.

        This will return the eigenvectors unsorted (since we know nothing about the eigenvalues).

        Args:
            theta_roi (ndarray): The list of theta's per voxel in the ROI
            phi_roi (ndarray): The list of phi's per voxel in the ROI
            psi_roi (ndarray): The list of psi's per voxel in the ROI

        Returns:
            The three eigenvectors per voxel in the ROI. The return matrix is of shape (n, 3, 3) where n is the number
            of voxels and the second dimension holds the number of evecs and the last dimension the direction per evec.

            This gives for one voxel the matrix:
                [evec_1_x, evec_1_y, evec_1_z,
                 evec_2_x, evec_2_y, evec_2_z
                 evec_3_x, evec_3_y, evec_3_z]

            The resulting eigenvectors are the same as those from the Tensor.
        """
        theta_roi = set_correct_cl_data_type(theta_roi)
        phi_roi = set_correct_cl_data_type(phi_roi)
        psi_roi = set_correct_cl_data_type(psi_roi)

        rows = theta_roi.shape[0]
        evecs = np.zeros((rows, 3*3), dtype=np.float64)

        workers = self._create_workers(_CEWorker, theta_roi, phi_roi, psi_roi, evecs)
        self.load_balancer.process(workers, rows)

        return np.reshape(evecs, (rows, 3, 3))


class _CEWorker(Worker):

    def __init__(self, cl_environment, theta_roi, phi_roi, psi_roi, evecs):
        super(_CEWorker, self).__init__(cl_environment)

        self._theta_roi = theta_roi
        self._phi_roi = phi_roi
        self._psi_roi = psi_roi
        self._evecs = evecs
        self._kernel = self._build_kernel()

    def calculate(self, range_start, range_end):
        nmr_problems = range_end - range_start
        write_flags = self._cl_environment.get_write_only_cl_mem_flags()
        read_flags = self._cl_environment.get_read_only_cl_mem_flags()

        thetas_buf = cl.Buffer(self._cl_environment.context, read_flags, hostbuf=self._theta_roi[range_start:range_end])
        phis_buf = cl.Buffer(self._cl_environment.context, read_flags, hostbuf=self._phi_roi[range_start:range_end])
        psis_buf = cl.Buffer(self._cl_environment.context, read_flags, hostbuf=self._psi_roi[range_start:range_end])
        evecs_buf = cl.Buffer(self._cl_environment.context, write_flags, hostbuf=self._evecs[range_start:range_end, :])
        buffers = [thetas_buf, phis_buf, psis_buf, evecs_buf]

        self._kernel.generate_tensor(self._queue, (int(nmr_problems), ), None, *buffers)
        event = cl.enqueue_copy(self._queue, self._evecs[range_start:range_end, :], evecs_buf, is_blocking=False)

        return event

    def _get_kernel_source(self):
        kernel_source = get_cl_pragma_double()
        kernel_source += '''
            double4 Tensor_rotateVector(const double4 vector, const double4 axis_rotate, const double psi){
                double4 n1 = axis_rotate;
                if(axis_rotate.z < 0 || ((axis_rotate.z == 0.0) && (axis_rotate.x < 0.0))){
                    n1 *= -1;
                }
                return vector * cos(psi) + (cross(vector, n1) * sin(psi)) + (n1 * dot(n1, vector) * (1-cos(psi)));
            }

            __kernel void generate_tensor(
                global double* thetas,
                global double* phis,
                global double* psis,
                global double* evecs
                ){
                    int gid = get_global_id(0);

                    double theta = thetas[gid];
                    double phi = phis[gid];
                    double psi = psis[gid];

                    double sinT = sin(theta);
                    double sinP = sin(phi);
                    double cosP = cos(phi);
                    double rst = sin(theta+(M_PI_2));

                    double4 n1 = (double4)(cosP * sinT, sinP * sinT, cos(theta), 0.0);
                    double4 n2 = Tensor_rotateVector((double4)(rst * cosP, rst * sinP, cos(theta+(M_PI_2)), 0.0),
                                                     n1, psi);

                    double4 n3 = cross(n1, n2);

                    evecs[gid*9] = n1.x;
                    evecs[gid*9 + 1] = n1.y;
                    evecs[gid*9 + 2] = n1.z;

                    evecs[gid*9 + 3] = n2.x;
                    evecs[gid*9 + 4] = n2.y;
                    evecs[gid*9 + 5] = n2.z;

                    evecs[gid*9 + 6] = n3.x;
                    evecs[gid*9 + 7] = n3.y;
                    evecs[gid*9 + 8] = n3.z;
            }
        '''
        return kernel_source