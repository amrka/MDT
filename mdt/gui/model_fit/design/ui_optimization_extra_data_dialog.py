# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optimization_extra_data_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OptimizationExtraDataDialog(object):
    def setupUi(self, OptimizationExtraDataDialog):
        OptimizationExtraDataDialog.setObjectName("OptimizationExtraDataDialog")
        OptimizationExtraDataDialog.resize(843, 331)
        self.verticalLayout = QtWidgets.QVBoxLayout(OptimizationExtraDataDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(OptimizationExtraDataDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(OptimizationExtraDataDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(OptimizationExtraDataDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_15 = QtWidgets.QLabel(OptimizationExtraDataDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(OptimizationExtraDataDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 2, 1, 1)
        self.line_5 = QtWidgets.QFrame(OptimizationExtraDataDialog)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 3, 0, 1, 3)
        self.label_7 = QtWidgets.QLabel(OptimizationExtraDataDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(OptimizationExtraDataDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 2, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gradientDeviations = QtWidgets.QLineEdit(OptimizationExtraDataDialog)
        self.gradientDeviations.setObjectName("gradientDeviations")
        self.horizontalLayout_6.addWidget(self.gradientDeviations)
        self.gradDevFileSelect = QtWidgets.QPushButton(OptimizationExtraDataDialog)
        self.gradDevFileSelect.setObjectName("gradDevFileSelect")
        self.horizontalLayout_6.addWidget(self.gradDevFileSelect)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(OptimizationExtraDataDialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.noiseStd = QtWidgets.QLineEdit(OptimizationExtraDataDialog)
        self.noiseStd.setObjectName("noiseStd")
        self.horizontalLayout_5.addWidget(self.noiseStd)
        self.noiseStdFileSelect = QtWidgets.QPushButton(OptimizationExtraDataDialog)
        self.noiseStdFileSelect.setObjectName("noiseStdFileSelect")
        self.horizontalLayout_5.addWidget(self.noiseStdFileSelect)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.staticMaps = QtWidgets.QListWidget(OptimizationExtraDataDialog)
        self.staticMaps.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.staticMaps.setObjectName("staticMaps")
        self.verticalLayout_2.addWidget(self.staticMaps)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.addStaticMap = QtWidgets.QPushButton(OptimizationExtraDataDialog)
        self.addStaticMap.setObjectName("addStaticMap")
        self.horizontalLayout_8.addWidget(self.addStaticMap)
        self.removeStaticMap = QtWidgets.QPushButton(OptimizationExtraDataDialog)
        self.removeStaticMap.setObjectName("removeStaticMap")
        self.horizontalLayout_8.addWidget(self.removeStaticMap)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.gridLayout.addLayout(self.verticalLayout_2, 4, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(OptimizationExtraDataDialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(OptimizationExtraDataDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line_3 = QtWidgets.QFrame(OptimizationExtraDataDialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(OptimizationExtraDataDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(OptimizationExtraDataDialog)
        self.buttonBox.accepted.connect(OptimizationExtraDataDialog.accept)
        self.buttonBox.rejected.connect(OptimizationExtraDataDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OptimizationExtraDataDialog)
        OptimizationExtraDataDialog.setTabOrder(self.noiseStd, self.noiseStdFileSelect)
        OptimizationExtraDataDialog.setTabOrder(self.noiseStdFileSelect, self.gradientDeviations)
        OptimizationExtraDataDialog.setTabOrder(self.gradientDeviations, self.gradDevFileSelect)
        OptimizationExtraDataDialog.setTabOrder(self.gradDevFileSelect, self.staticMaps)
        OptimizationExtraDataDialog.setTabOrder(self.staticMaps, self.addStaticMap)
        OptimizationExtraDataDialog.setTabOrder(self.addStaticMap, self.removeStaticMap)

    def retranslateUi(self, OptimizationExtraDataDialog):
        _translate = QtCore.QCoreApplication.translate
        OptimizationExtraDataDialog.setWindowTitle(_translate("OptimizationExtraDataDialog", "Additional problem data"))
        self.label_3.setText(_translate("OptimizationExtraDataDialog", "Additional problem data"))
        self.label_4.setText(_translate("OptimizationExtraDataDialog", "Extra data that can be used in the model fitting procedure"))
        self.label_15.setText(_translate("OptimizationExtraDataDialog", "(Per voxel 9 values that constitute the gradient non-linearities)"))
        self.label_10.setText(_translate("OptimizationExtraDataDialog", "(Additional maps to be used in the fitting routine)"))
        self.label_7.setText(_translate("OptimizationExtraDataDialog", "Noise standard deviation:"))
        self.label_14.setText(_translate("OptimizationExtraDataDialog", "(Empty for auto detection, or set a scalar or a path to a nifti file)"))
        self.gradDevFileSelect.setText(_translate("OptimizationExtraDataDialog", "File browser"))
        self.label_8.setText(_translate("OptimizationExtraDataDialog", "Gradient deviations:"))
        self.noiseStdFileSelect.setText(_translate("OptimizationExtraDataDialog", "File browser"))
        self.addStaticMap.setText(_translate("OptimizationExtraDataDialog", "Add map"))
        self.removeStaticMap.setText(_translate("OptimizationExtraDataDialog", "Remove selected"))
        self.label_2.setText(_translate("OptimizationExtraDataDialog", "Static maps:"))

