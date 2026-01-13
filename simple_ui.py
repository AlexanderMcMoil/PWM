# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simple_uiIjFAMX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.channel_info_header_group = QHBoxLayout()
        self.channel_info_header_group.setObjectName(u"channel_info_header_group")
        self.channel_header_label = QLabel(self.centralwidget)
        self.channel_header_label.setObjectName(u"channel_header_label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.channel_header_label.sizePolicy().hasHeightForWidth())
        self.channel_header_label.setSizePolicy(sizePolicy)

        self.channel_info_header_group.addWidget(self.channel_header_label)

        self.frequency_header_label = QLabel(self.centralwidget)
        self.frequency_header_label.setObjectName(u"frequency_header_label")

        self.channel_info_header_group.addWidget(self.frequency_header_label)

        self.pulse_width_header_label = QLabel(self.centralwidget)
        self.pulse_width_header_label.setObjectName(u"pulse_width_header_label")

        self.channel_info_header_group.addWidget(self.pulse_width_header_label)

        self.amplitude_header_label = QLabel(self.centralwidget)
        self.amplitude_header_label.setObjectName(u"amplitude_header_label")

        self.channel_info_header_group.addWidget(self.amplitude_header_label)


        self.verticalLayout.addLayout(self.channel_info_header_group)

        self.edit_parameters_label = QLabel(self.centralwidget)
        self.edit_parameters_label.setObjectName(u"edit_parameters_label")

        self.verticalLayout.addWidget(self.edit_parameters_label)

        self.channel_input_group = QHBoxLayout()
        self.channel_input_group.setObjectName(u"channel_input_group")
        self.channel_input = QComboBox(self.centralwidget)
        self.channel_input.addItem("")
        self.channel_input.addItem("")
        self.channel_input.addItem("")
        self.channel_input.addItem("")
        self.channel_input.addItem("")
        self.channel_input.addItem("")
        self.channel_input.addItem("")
        self.channel_input.addItem("")
        self.channel_input.setObjectName(u"channel_input")

        self.channel_input_group.addWidget(self.channel_input)

        self.frequency_input = QLineEdit(self.centralwidget)
        self.frequency_input.setObjectName(u"frequency_input")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frequency_input.sizePolicy().hasHeightForWidth())
        self.frequency_input.setSizePolicy(sizePolicy1)

        self.channel_input_group.addWidget(self.frequency_input)

        self.pulse_width_input = QLineEdit(self.centralwidget)
        self.pulse_width_input.setObjectName(u"pulse_width_input")
        sizePolicy1.setHeightForWidth(self.pulse_width_input.sizePolicy().hasHeightForWidth())
        self.pulse_width_input.setSizePolicy(sizePolicy1)

        self.channel_input_group.addWidget(self.pulse_width_input)

        self.amplitude_input = QLineEdit(self.centralwidget)
        self.amplitude_input.setObjectName(u"amplitude_input")
        sizePolicy1.setHeightForWidth(self.amplitude_input.sizePolicy().hasHeightForWidth())
        self.amplitude_input.setSizePolicy(sizePolicy1)

        self.channel_input_group.addWidget(self.amplitude_input)


        self.verticalLayout.addLayout(self.channel_input_group)

        self.confirm_button = QPushButton(self.centralwidget)
        self.confirm_button.setObjectName(u"confirm_button")

        self.verticalLayout.addWidget(self.confirm_button)

        self.parameter_info_label = QLabel(self.centralwidget)
        self.parameter_info_label.setObjectName(u"parameter_info_label")

        self.verticalLayout.addWidget(self.parameter_info_label)

        self.channel_info_group_0 = QHBoxLayout()
        self.channel_info_group_0.setObjectName(u"channel_info_group_0")
        self.channel_label_0 = QLabel(self.centralwidget)
        self.channel_label_0.setObjectName(u"channel_label_0")
        sizePolicy.setHeightForWidth(self.channel_label_0.sizePolicy().hasHeightForWidth())
        self.channel_label_0.setSizePolicy(sizePolicy)

        self.channel_info_group_0.addWidget(self.channel_label_0)

        self.frequency_label_0 = QLabel(self.centralwidget)
        self.frequency_label_0.setObjectName(u"frequency_label_0")

        self.channel_info_group_0.addWidget(self.frequency_label_0)

        self.pulse_width_label_0 = QLabel(self.centralwidget)
        self.pulse_width_label_0.setObjectName(u"pulse_width_label_0")

        self.channel_info_group_0.addWidget(self.pulse_width_label_0)

        self.amplitude_label_0 = QLabel(self.centralwidget)
        self.amplitude_label_0.setObjectName(u"amplitude_label_0")

        self.channel_info_group_0.addWidget(self.amplitude_label_0)


        self.verticalLayout.addLayout(self.channel_info_group_0)

        self.channel_info_group_1 = QHBoxLayout()
        self.channel_info_group_1.setObjectName(u"channel_info_group_1")
        self.channel_label_1 = QLabel(self.centralwidget)
        self.channel_label_1.setObjectName(u"channel_label_1")

        self.channel_info_group_1.addWidget(self.channel_label_1)

        self.frequency_label_1 = QLabel(self.centralwidget)
        self.frequency_label_1.setObjectName(u"frequency_label_1")

        self.channel_info_group_1.addWidget(self.frequency_label_1)

        self.pulse_width_label_1 = QLabel(self.centralwidget)
        self.pulse_width_label_1.setObjectName(u"pulse_width_label_1")

        self.channel_info_group_1.addWidget(self.pulse_width_label_1)

        self.amplitude_label_1 = QLabel(self.centralwidget)
        self.amplitude_label_1.setObjectName(u"amplitude_label_1")

        self.channel_info_group_1.addWidget(self.amplitude_label_1)


        self.verticalLayout.addLayout(self.channel_info_group_1)

        self.channel_info_group_2 = QHBoxLayout()
        self.channel_info_group_2.setObjectName(u"channel_info_group_2")
        self.channel_label_2 = QLabel(self.centralwidget)
        self.channel_label_2.setObjectName(u"channel_label_2")

        self.channel_info_group_2.addWidget(self.channel_label_2)

        self.frequency_label_2 = QLabel(self.centralwidget)
        self.frequency_label_2.setObjectName(u"frequency_label_2")

        self.channel_info_group_2.addWidget(self.frequency_label_2)

        self.pulse_width_label_2 = QLabel(self.centralwidget)
        self.pulse_width_label_2.setObjectName(u"pulse_width_label_2")

        self.channel_info_group_2.addWidget(self.pulse_width_label_2)

        self.amplitude_label_2 = QLabel(self.centralwidget)
        self.amplitude_label_2.setObjectName(u"amplitude_label_2")

        self.channel_info_group_2.addWidget(self.amplitude_label_2)


        self.verticalLayout.addLayout(self.channel_info_group_2)

        self.channel_info_group_3 = QHBoxLayout()
        self.channel_info_group_3.setObjectName(u"channel_info_group_3")
        self.channel_label_3 = QLabel(self.centralwidget)
        self.channel_label_3.setObjectName(u"channel_label_3")

        self.channel_info_group_3.addWidget(self.channel_label_3)

        self.frequency_label_3 = QLabel(self.centralwidget)
        self.frequency_label_3.setObjectName(u"frequency_label_3")

        self.channel_info_group_3.addWidget(self.frequency_label_3)

        self.pulse_width_label_3 = QLabel(self.centralwidget)
        self.pulse_width_label_3.setObjectName(u"pulse_width_label_3")

        self.channel_info_group_3.addWidget(self.pulse_width_label_3)

        self.amplitude_label_3 = QLabel(self.centralwidget)
        self.amplitude_label_3.setObjectName(u"amplitude_label_3")

        self.channel_info_group_3.addWidget(self.amplitude_label_3)


        self.verticalLayout.addLayout(self.channel_info_group_3)

        self.channel_info_group_4 = QHBoxLayout()
        self.channel_info_group_4.setObjectName(u"channel_info_group_4")
        self.channel_label_4 = QLabel(self.centralwidget)
        self.channel_label_4.setObjectName(u"channel_label_4")

        self.channel_info_group_4.addWidget(self.channel_label_4)

        self.frequency_label_4 = QLabel(self.centralwidget)
        self.frequency_label_4.setObjectName(u"frequency_label_4")

        self.channel_info_group_4.addWidget(self.frequency_label_4)

        self.pulse_width_label_4 = QLabel(self.centralwidget)
        self.pulse_width_label_4.setObjectName(u"pulse_width_label_4")

        self.channel_info_group_4.addWidget(self.pulse_width_label_4)

        self.amplitude_label_4 = QLabel(self.centralwidget)
        self.amplitude_label_4.setObjectName(u"amplitude_label_4")

        self.channel_info_group_4.addWidget(self.amplitude_label_4)


        self.verticalLayout.addLayout(self.channel_info_group_4)

        self.channel_info_group_5 = QHBoxLayout()
        self.channel_info_group_5.setObjectName(u"channel_info_group_5")
        self.channel_label_5 = QLabel(self.centralwidget)
        self.channel_label_5.setObjectName(u"channel_label_5")

        self.channel_info_group_5.addWidget(self.channel_label_5)

        self.frequency_label_5 = QLabel(self.centralwidget)
        self.frequency_label_5.setObjectName(u"frequency_label_5")

        self.channel_info_group_5.addWidget(self.frequency_label_5)

        self.pulse_width_label_5 = QLabel(self.centralwidget)
        self.pulse_width_label_5.setObjectName(u"pulse_width_label_5")

        self.channel_info_group_5.addWidget(self.pulse_width_label_5)

        self.amplitude_label_5 = QLabel(self.centralwidget)
        self.amplitude_label_5.setObjectName(u"amplitude_label_5")

        self.channel_info_group_5.addWidget(self.amplitude_label_5)


        self.verticalLayout.addLayout(self.channel_info_group_5)

        self.channel_info_group_6 = QHBoxLayout()
        self.channel_info_group_6.setObjectName(u"channel_info_group_6")
        self.channel_label_6 = QLabel(self.centralwidget)
        self.channel_label_6.setObjectName(u"channel_label_6")

        self.channel_info_group_6.addWidget(self.channel_label_6)

        self.frequency_label_6 = QLabel(self.centralwidget)
        self.frequency_label_6.setObjectName(u"frequency_label_6")

        self.channel_info_group_6.addWidget(self.frequency_label_6)

        self.pulse_width_label_6 = QLabel(self.centralwidget)
        self.pulse_width_label_6.setObjectName(u"pulse_width_label_6")

        self.channel_info_group_6.addWidget(self.pulse_width_label_6)

        self.amplitude_label_6 = QLabel(self.centralwidget)
        self.amplitude_label_6.setObjectName(u"amplitude_label_6")

        self.channel_info_group_6.addWidget(self.amplitude_label_6)


        self.verticalLayout.addLayout(self.channel_info_group_6)

        self.channel_info_group_7 = QHBoxLayout()
        self.channel_info_group_7.setObjectName(u"channel_info_group_7")
        self.channel_label_7 = QLabel(self.centralwidget)
        self.channel_label_7.setObjectName(u"channel_label_7")

        self.channel_info_group_7.addWidget(self.channel_label_7)

        self.frequency_label_7 = QLabel(self.centralwidget)
        self.frequency_label_7.setObjectName(u"frequency_label_7")

        self.channel_info_group_7.addWidget(self.frequency_label_7)

        self.pulse_width_label_7 = QLabel(self.centralwidget)
        self.pulse_width_label_7.setObjectName(u"pulse_width_label_7")

        self.channel_info_group_7.addWidget(self.pulse_width_label_7)

        self.amplitude_label_7 = QLabel(self.centralwidget)
        self.amplitude_label_7.setObjectName(u"amplitude_label_7")

        self.channel_info_group_7.addWidget(self.amplitude_label_7)


        self.verticalLayout.addLayout(self.channel_info_group_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.channel_header_label.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.frequency_header_label.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.pulse_width_header_label.setText(QCoreApplication.translate("MainWindow", u"Pulse Width", None))
        self.amplitude_header_label.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.edit_parameters_label.setText(QCoreApplication.translate("MainWindow", u"Edit Parameters", None))
        self.channel_input.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.channel_input.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.channel_input.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.channel_input.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.channel_input.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.channel_input.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.channel_input.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.channel_input.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))

        self.confirm_button.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.parameter_info_label.setText(QCoreApplication.translate("MainWindow", u"Channel Information", None))
        self.channel_label_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.frequency_label_0.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pulse_width_label_0.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.amplitude_label_0.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.channel_label_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.frequency_label_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pulse_width_label_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.amplitude_label_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.channel_label_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.frequency_label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pulse_width_label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.amplitude_label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.channel_label_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.frequency_label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pulse_width_label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.amplitude_label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.channel_label_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.frequency_label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pulse_width_label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.amplitude_label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.channel_label_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.frequency_label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pulse_width_label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.amplitude_label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.channel_label_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.frequency_label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pulse_width_label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.amplitude_label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.channel_label_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.frequency_label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pulse_width_label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.amplitude_label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

