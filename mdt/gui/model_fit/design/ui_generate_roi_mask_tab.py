# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generate_roi_mask_tab.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GenerateROIMaskTabContent(object):
    def setupUi(self, GenerateROIMaskTabContent):
        GenerateROIMaskTabContent.setObjectName("GenerateROIMaskTabContent")
        GenerateROIMaskTabContent.resize(827, 427)
        self.verticalLayout = QtWidgets.QVBoxLayout(GenerateROIMaskTabContent)
        self.verticalLayout.setContentsMargins(-1, 11, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(GenerateROIMaskTabContent)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(GenerateROIMaskTabContent)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(GenerateROIMaskTabContent)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.dimensionInput = QtWidgets.QSpinBox(GenerateROIMaskTabContent)
        self.dimensionInput.setMinimum(0)
        self.dimensionInput.setMaximum(2)
        self.dimensionInput.setProperty("value", 2)
        self.dimensionInput.setObjectName("dimensionInput")
        self.horizontalLayout_5.addWidget(self.dimensionInput)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(GenerateROIMaskTabContent)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(GenerateROIMaskTabContent)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(GenerateROIMaskTabContent)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.selectMaskButton = QtWidgets.QPushButton(GenerateROIMaskTabContent)
        self.selectMaskButton.setObjectName("selectMaskButton")
        self.horizontalLayout_2.addWidget(self.selectMaskButton)
        self.selectedMaskText = QtWidgets.QLineEdit(GenerateROIMaskTabContent)
        self.selectedMaskText.setText("")
        self.selectedMaskText.setObjectName("selectedMaskText")
        self.horizontalLayout_2.addWidget(self.selectedMaskText)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(GenerateROIMaskTabContent)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(GenerateROIMaskTabContent)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sliceInput = QtWidgets.QSpinBox(GenerateROIMaskTabContent)
        self.sliceInput.setMinimum(0)
        self.sliceInput.setMaximum(10000)
        self.sliceInput.setProperty("value", 0)
        self.sliceInput.setObjectName("sliceInput")
        self.horizontalLayout_3.addWidget(self.sliceInput)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(3, -1, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(GenerateROIMaskTabContent)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.maxSliceLabel = QtWidgets.QLabel(GenerateROIMaskTabContent)
        self.maxSliceLabel.setObjectName("maxSliceLabel")
        self.horizontalLayout_6.addWidget(self.maxSliceLabel)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(GenerateROIMaskTabContent)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(GenerateROIMaskTabContent)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.selectOutputFileInput = QtWidgets.QPushButton(GenerateROIMaskTabContent)
        self.selectOutputFileInput.setObjectName("selectOutputFileInput")
        self.horizontalLayout_4.addWidget(self.selectOutputFileInput)
        self.selectedOutputFileText = QtWidgets.QLineEdit(GenerateROIMaskTabContent)
        self.selectedOutputFileText.setObjectName("selectedOutputFileText")
        self.horizontalLayout_4.addWidget(self.selectedOutputFileText)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(GenerateROIMaskTabContent)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_2 = QtWidgets.QFrame(GenerateROIMaskTabContent)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 6, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.generateButton = QtWidgets.QPushButton(GenerateROIMaskTabContent)
        self.generateButton.setEnabled(False)
        self.generateButton.setObjectName("generateButton")
        self.horizontalLayout.addWidget(self.generateButton)
        self.viewButton = QtWidgets.QPushButton(GenerateROIMaskTabContent)
        self.viewButton.setEnabled(False)
        self.viewButton.setObjectName("viewButton")
        self.horizontalLayout.addWidget(self.viewButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(GenerateROIMaskTabContent)
        QtCore.QMetaObject.connectSlotsByName(GenerateROIMaskTabContent)
        GenerateROIMaskTabContent.setTabOrder(self.selectMaskButton, self.selectedMaskText)
        GenerateROIMaskTabContent.setTabOrder(self.selectedMaskText, self.dimensionInput)
        GenerateROIMaskTabContent.setTabOrder(self.dimensionInput, self.sliceInput)
        GenerateROIMaskTabContent.setTabOrder(self.sliceInput, self.selectOutputFileInput)
        GenerateROIMaskTabContent.setTabOrder(self.selectOutputFileInput, self.selectedOutputFileText)
        GenerateROIMaskTabContent.setTabOrder(self.selectedOutputFileText, self.generateButton)
        GenerateROIMaskTabContent.setTabOrder(self.generateButton, self.viewButton)

    def retranslateUi(self, GenerateROIMaskTabContent):
        _translate = QtCore.QCoreApplication.translate
        GenerateROIMaskTabContent.setWindowTitle(_translate("GenerateROIMaskTabContent", "Form"))
        self.label.setText(_translate("GenerateROIMaskTabContent", "Generate ROI mask"))
        self.label_2.setText(_translate("GenerateROIMaskTabContent", "Create a mask with a Region Of Interest including only the voxels in the selected slice."))
        self.label_6.setText(_translate("GenerateROIMaskTabContent", "Select brain mask:"))
        self.label_3.setText(_translate("GenerateROIMaskTabContent", "Select output file:"))
        self.label_10.setText(_translate("GenerateROIMaskTabContent", "(The index of the single slice in the current dimension)"))
        self.selectMaskButton.setText(_translate("GenerateROIMaskTabContent", "Browse"))
        self.label_4.setText(_translate("GenerateROIMaskTabContent", "(Select your brain mask)"))
        self.label_5.setText(_translate("GenerateROIMaskTabContent", "(The dimension of the single slice)"))
        self.label_7.setText(_translate("GenerateROIMaskTabContent", "/ "))
        self.maxSliceLabel.setText(_translate("GenerateROIMaskTabContent", "x"))
        self.label_11.setText(_translate("GenerateROIMaskTabContent", "Select dimension:"))
        self.label_14.setText(_translate("GenerateROIMaskTabContent", "(Default is <mask_name>_<dim>_<slice>.nii.gz)"))
        self.selectOutputFileInput.setText(_translate("GenerateROIMaskTabContent", "Browse"))
        self.label_12.setText(_translate("GenerateROIMaskTabContent", "Select slice:"))
        self.generateButton.setText(_translate("GenerateROIMaskTabContent", "Generate"))
        self.viewButton.setText(_translate("GenerateROIMaskTabContent", "View ROI"))

