import glob
import os

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFileDialog

from mdt import results_preselection_names, view_results_slice, load_nifti
from mdt.gui.qt.design.ui_view_results_tab import Ui_ViewResultsTabContent
from mdt.utils import split_image_path

__author__ = 'Robbert Harms'
__date__ = "2016-06-26"
__maintainer__ = "Robbert Harms"
__email__ = "robbert.harms@maastrichtuniversity.nl"


class ViewResultsTab(Ui_ViewResultsTabContent):

    def __init__(self, initial_directory, **kwargs):
        self.initial_directory = initial_directory
        self._parameter_files = {}
        self._folder = None

    def setupUi(self, ViewResultsTabContent):
        super(ViewResultsTab, self).setupUi(ViewResultsTabContent)

        self.selectFolderButton.clicked.connect(
            lambda: self.selectedFolderText.setText(QFileDialog().getExistingDirectory(
                caption='Select directory to view', directory=self.initial_directory))
        )

        self.selectedFolderText.textChanged.connect(self.directory_updated)
        self.viewButton.clicked.connect(self.view_maps)
        self.invertSelectionButton.clicked.connect(self.invert_selection)
        self.deselectAllButton.clicked.connect(self.deselect_all)
        self.initialDimensionChooser.setValue(2)
        self.initialDimensionChooser.setMaximum(2)
        self.initialDimensionChooser.setMinimum(0)
        self.initialSliceChooser.setMinimum(0)

    @pyqtSlot(str)
    def directory_updated(self, folder):
        if os.path.isfile(folder):
            folder = os.path.dirname(folder)

        self._folder = folder
        result_files = glob.glob(os.path.join(folder, '*.nii*'))

        def get_name(img_path):
            return split_image_path(os.path.basename(img_path))[1]

        self._parameter_files = {get_name(f): get_name(f) for f in result_files}

        items_list = sorted(self._parameter_files.keys())
        selected_items = results_preselection_names(sorted(self._parameter_files.keys()))

        self.selectMaps.clear()
        self.selectMaps.addItems(items_list)

        for item in [self.selectMaps.item(index) for index in range(self.selectMaps.count())]:
            if item.text() in selected_items:
                item.setSelected(True)

        if items_list:
            shape = load_nifti(result_files[0]).shape
            maximum = shape[self.initialDimensionChooser.value()]
            self.initialSliceChooser.setMaximum(maximum)
            self.initialSliceChooser.setValue(maximum // 2.0)

    @pyqtSlot()
    def invert_selection(self):
        for item in [self.selectMaps.item(index) for index in range(self.selectMaps.count())]:
            item.setSelected(not item.isSelected())

    @pyqtSlot()
    def deselect_all(self):
        for item in [self.selectMaps.item(index) for index in range(self.selectMaps.count())]:
            item.setSelected(False)

    @pyqtSlot()
    def view_maps(self):
        maps_to_show = []
        for item in [self.selectMaps.item(index) for index in range(self.selectMaps.count())]:
            if item.isSelected():
                maps_to_show.append(item.text())

        if maps_to_show:
            view_results_slice(self._folder, maps_to_show=maps_to_show)
