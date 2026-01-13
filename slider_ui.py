# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'slider_uiiRMbiC.ui'
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
        MainWindow.resize(800, 566)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_0 = QWidget()
        self.tab_0.setObjectName(u"tab_0")
        self.gridLayout_8 = QGridLayout(self.tab_0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.wrapping_layout_0 = QVBoxLayout()
        self.wrapping_layout_0.setObjectName(u"wrapping_layout_0")
        self.options_layout_0 = QHBoxLayout()
        self.options_layout_0.setObjectName(u"options_layout_0")
        self.active_button_0 = QRadioButton(self.tab_0)
        self.active_button_0.setObjectName(u"active_button_0")

        self.options_layout_0.addWidget(self.active_button_0)

        self.asymmetric_button_0 = QCheckBox(self.tab_0)
        self.asymmetric_button_0.setObjectName(u"asymmetric_button_0")
        self.asymmetric_button_0.setTristate(False)

        self.options_layout_0.addWidget(self.asymmetric_button_0)


        self.wrapping_layout_0.addLayout(self.options_layout_0)

        self.parameter_layout_0 = QGridLayout()
        self.parameter_layout_0.setObjectName(u"parameter_layout_0")
        self.amplitude_slider_0 = QSlider(self.tab_0)
        self.amplitude_slider_0.setObjectName(u"amplitude_slider_0")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amplitude_slider_0.sizePolicy().hasHeightForWidth())
        self.amplitude_slider_0.setSizePolicy(sizePolicy)
        self.amplitude_slider_0.setMaximum(15)
        self.amplitude_slider_0.setOrientation(Qt.Vertical)

        self.parameter_layout_0.addWidget(self.amplitude_slider_0, 2, 2, 1, 1)

        self.frequency_label_0 = QLabel(self.tab_0)
        self.frequency_label_0.setObjectName(u"frequency_label_0")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frequency_label_0.sizePolicy().hasHeightForWidth())
        self.frequency_label_0.setSizePolicy(sizePolicy1)
        self.frequency_label_0.setAlignment(Qt.AlignCenter)

        self.parameter_layout_0.addWidget(self.frequency_label_0, 0, 1, 1, 1)

        self.amplitude_falling_layout_0 = QFrame(self.tab_0)
        self.amplitude_falling_layout_0.setObjectName(u"amplitude_falling_layout_0")
        self.amplitude_2_layout = QVBoxLayout(self.amplitude_falling_layout_0)
        self.amplitude_2_layout.setObjectName(u"amplitude_2_layout")
        self.amplitude_2_layout.setContentsMargins(0, 0, 0, 0)
        self.amplitude_falling_label_0 = QLabel(self.amplitude_falling_layout_0)
        self.amplitude_falling_label_0.setObjectName(u"amplitude_falling_label_0")
        sizePolicy1.setHeightForWidth(self.amplitude_falling_label_0.sizePolicy().hasHeightForWidth())
        self.amplitude_falling_label_0.setSizePolicy(sizePolicy1)
        self.amplitude_falling_label_0.setAlignment(Qt.AlignCenter)

        self.amplitude_2_layout.addWidget(self.amplitude_falling_label_0)

        self.amplitude_falling_value_0 = QLabel(self.amplitude_falling_layout_0)
        self.amplitude_falling_value_0.setObjectName(u"amplitude_falling_value_0")

        self.amplitude_2_layout.addWidget(self.amplitude_falling_value_0)

        self.amplitude_falling_slider_0 = QSlider(self.amplitude_falling_layout_0)
        self.amplitude_falling_slider_0.setObjectName(u"amplitude_falling_slider_0")
        sizePolicy.setHeightForWidth(self.amplitude_falling_slider_0.sizePolicy().hasHeightForWidth())
        self.amplitude_falling_slider_0.setSizePolicy(sizePolicy)
        self.amplitude_falling_slider_0.setMaximum(15)
        self.amplitude_falling_slider_0.setOrientation(Qt.Vertical)

        self.amplitude_2_layout.addWidget(self.amplitude_falling_slider_0)


        self.parameter_layout_0.addWidget(self.amplitude_falling_layout_0, 0, 3, 3, 1)

        self.pulse_width_value_0 = QLabel(self.tab_0)
        self.pulse_width_value_0.setObjectName(u"pulse_width_value_0")

        self.parameter_layout_0.addWidget(self.pulse_width_value_0, 1, 0, 1, 1)

        self.frequency_slider_0 = QSlider(self.tab_0)
        self.frequency_slider_0.setObjectName(u"frequency_slider_0")
        sizePolicy.setHeightForWidth(self.frequency_slider_0.sizePolicy().hasHeightForWidth())
        self.frequency_slider_0.setSizePolicy(sizePolicy)
        self.frequency_slider_0.setMaximum(200)
        self.frequency_slider_0.setOrientation(Qt.Vertical)

        self.parameter_layout_0.addWidget(self.frequency_slider_0, 2, 1, 1, 1)

        self.amplitude_label_0 = QLabel(self.tab_0)
        self.amplitude_label_0.setObjectName(u"amplitude_label_0")
        sizePolicy1.setHeightForWidth(self.amplitude_label_0.sizePolicy().hasHeightForWidth())
        self.amplitude_label_0.setSizePolicy(sizePolicy1)
        self.amplitude_label_0.setAlignment(Qt.AlignCenter)

        self.parameter_layout_0.addWidget(self.amplitude_label_0, 0, 2, 1, 1)

        self.frequency_value_0 = QLabel(self.tab_0)
        self.frequency_value_0.setObjectName(u"frequency_value_0")

        self.parameter_layout_0.addWidget(self.frequency_value_0, 1, 1, 1, 1)

        self.pulse_width_label_0 = QLabel(self.tab_0)
        self.pulse_width_label_0.setObjectName(u"pulse_width_label_0")
        sizePolicy1.setHeightForWidth(self.pulse_width_label_0.sizePolicy().hasHeightForWidth())
        self.pulse_width_label_0.setSizePolicy(sizePolicy1)
        self.pulse_width_label_0.setAlignment(Qt.AlignCenter)
        self.pulse_width_label_0.setWordWrap(False)

        self.parameter_layout_0.addWidget(self.pulse_width_label_0, 0, 0, 1, 1)

        self.pulse_width_slider_0 = QSlider(self.tab_0)
        self.pulse_width_slider_0.setObjectName(u"pulse_width_slider_0")
        sizePolicy.setHeightForWidth(self.pulse_width_slider_0.sizePolicy().hasHeightForWidth())
        self.pulse_width_slider_0.setSizePolicy(sizePolicy)
        self.pulse_width_slider_0.setMaximum(200)
        self.pulse_width_slider_0.setOrientation(Qt.Vertical)

        self.parameter_layout_0.addWidget(self.pulse_width_slider_0, 2, 0, 1, 1)

        self.amplitude_value_0 = QLabel(self.tab_0)
        self.amplitude_value_0.setObjectName(u"amplitude_value_0")

        self.parameter_layout_0.addWidget(self.amplitude_value_0, 1, 2, 1, 1)


        self.wrapping_layout_0.addLayout(self.parameter_layout_0)


        self.gridLayout_8.addLayout(self.wrapping_layout_0, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_0, "")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_9 = QGridLayout(self.tab_1)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.wrapping_layout_1 = QVBoxLayout()
        self.wrapping_layout_1.setObjectName(u"wrapping_layout_1")
        self.options_layout_1 = QHBoxLayout()
        self.options_layout_1.setObjectName(u"options_layout_1")
        self.active_button_1 = QRadioButton(self.tab_1)
        self.active_button_1.setObjectName(u"active_button_1")

        self.options_layout_1.addWidget(self.active_button_1)

        self.asymmetric_button_1 = QCheckBox(self.tab_1)
        self.asymmetric_button_1.setObjectName(u"asymmetric_button_1")
        self.asymmetric_button_1.setTristate(False)

        self.options_layout_1.addWidget(self.asymmetric_button_1)


        self.wrapping_layout_1.addLayout(self.options_layout_1)

        self.parameter_layout_1 = QGridLayout()
        self.parameter_layout_1.setObjectName(u"parameter_layout_1")
        self.amplitude_slider_1 = QSlider(self.tab_1)
        self.amplitude_slider_1.setObjectName(u"amplitude_slider_1")
        sizePolicy.setHeightForWidth(self.amplitude_slider_1.sizePolicy().hasHeightForWidth())
        self.amplitude_slider_1.setSizePolicy(sizePolicy)
        self.amplitude_slider_1.setMaximum(15)
        self.amplitude_slider_1.setOrientation(Qt.Vertical)

        self.parameter_layout_1.addWidget(self.amplitude_slider_1, 2, 2, 1, 1)

        self.frequency_label_1 = QLabel(self.tab_1)
        self.frequency_label_1.setObjectName(u"frequency_label_1")
        sizePolicy1.setHeightForWidth(self.frequency_label_1.sizePolicy().hasHeightForWidth())
        self.frequency_label_1.setSizePolicy(sizePolicy1)
        self.frequency_label_1.setAlignment(Qt.AlignCenter)

        self.parameter_layout_1.addWidget(self.frequency_label_1, 0, 1, 1, 1)

        self.amplitude_falling_layout_1 = QFrame(self.tab_1)
        self.amplitude_falling_layout_1.setObjectName(u"amplitude_falling_layout_1")
        self.amplitude_2_layout_2 = QVBoxLayout(self.amplitude_falling_layout_1)
        self.amplitude_2_layout_2.setObjectName(u"amplitude_2_layout_2")
        self.amplitude_2_layout_2.setContentsMargins(0, 0, 0, 0)
        self.amplitude_falling_label_1 = QLabel(self.amplitude_falling_layout_1)
        self.amplitude_falling_label_1.setObjectName(u"amplitude_falling_label_1")
        sizePolicy1.setHeightForWidth(self.amplitude_falling_label_1.sizePolicy().hasHeightForWidth())
        self.amplitude_falling_label_1.setSizePolicy(sizePolicy1)
        self.amplitude_falling_label_1.setAlignment(Qt.AlignCenter)

        self.amplitude_2_layout_2.addWidget(self.amplitude_falling_label_1)

        self.amplitude_falling_value_1 = QLabel(self.amplitude_falling_layout_1)
        self.amplitude_falling_value_1.setObjectName(u"amplitude_falling_value_1")

        self.amplitude_2_layout_2.addWidget(self.amplitude_falling_value_1)

        self.amplitude_falling_slider_1 = QSlider(self.amplitude_falling_layout_1)
        self.amplitude_falling_slider_1.setObjectName(u"amplitude_falling_slider_1")
        sizePolicy.setHeightForWidth(self.amplitude_falling_slider_1.sizePolicy().hasHeightForWidth())
        self.amplitude_falling_slider_1.setSizePolicy(sizePolicy)
        self.amplitude_falling_slider_1.setMaximum(15)
        self.amplitude_falling_slider_1.setOrientation(Qt.Vertical)

        self.amplitude_2_layout_2.addWidget(self.amplitude_falling_slider_1)


        self.parameter_layout_1.addWidget(self.amplitude_falling_layout_1, 0, 3, 3, 1)

        self.pulse_width_value_1 = QLabel(self.tab_1)
        self.pulse_width_value_1.setObjectName(u"pulse_width_value_1")

        self.parameter_layout_1.addWidget(self.pulse_width_value_1, 1, 0, 1, 1)

        self.frequency_slider_1 = QSlider(self.tab_1)
        self.frequency_slider_1.setObjectName(u"frequency_slider_1")
        sizePolicy.setHeightForWidth(self.frequency_slider_1.sizePolicy().hasHeightForWidth())
        self.frequency_slider_1.setSizePolicy(sizePolicy)
        self.frequency_slider_1.setMaximum(200)
        self.frequency_slider_1.setOrientation(Qt.Vertical)

        self.parameter_layout_1.addWidget(self.frequency_slider_1, 2, 1, 1, 1)

        self.amplitude_label_1 = QLabel(self.tab_1)
        self.amplitude_label_1.setObjectName(u"amplitude_label_1")
        sizePolicy1.setHeightForWidth(self.amplitude_label_1.sizePolicy().hasHeightForWidth())
        self.amplitude_label_1.setSizePolicy(sizePolicy1)
        self.amplitude_label_1.setAlignment(Qt.AlignCenter)

        self.parameter_layout_1.addWidget(self.amplitude_label_1, 0, 2, 1, 1)

        self.frequency_value_1 = QLabel(self.tab_1)
        self.frequency_value_1.setObjectName(u"frequency_value_1")

        self.parameter_layout_1.addWidget(self.frequency_value_1, 1, 1, 1, 1)

        self.pulse_width_label_1 = QLabel(self.tab_1)
        self.pulse_width_label_1.setObjectName(u"pulse_width_label_1")
        sizePolicy1.setHeightForWidth(self.pulse_width_label_1.sizePolicy().hasHeightForWidth())
        self.pulse_width_label_1.setSizePolicy(sizePolicy1)
        self.pulse_width_label_1.setAlignment(Qt.AlignCenter)
        self.pulse_width_label_1.setWordWrap(False)

        self.parameter_layout_1.addWidget(self.pulse_width_label_1, 0, 0, 1, 1)

        self.pulse_width_slider_1 = QSlider(self.tab_1)
        self.pulse_width_slider_1.setObjectName(u"pulse_width_slider_1")
        sizePolicy.setHeightForWidth(self.pulse_width_slider_1.sizePolicy().hasHeightForWidth())
        self.pulse_width_slider_1.setSizePolicy(sizePolicy)
        self.pulse_width_slider_1.setMaximum(200)
        self.pulse_width_slider_1.setOrientation(Qt.Vertical)

        self.parameter_layout_1.addWidget(self.pulse_width_slider_1, 2, 0, 1, 1)

        self.amplitude_value_1 = QLabel(self.tab_1)
        self.amplitude_value_1.setObjectName(u"amplitude_value_1")

        self.parameter_layout_1.addWidget(self.amplitude_value_1, 1, 2, 1, 1)


        self.wrapping_layout_1.addLayout(self.parameter_layout_1)


        self.gridLayout_9.addLayout(self.wrapping_layout_1, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.wrapping_layout_2 = QVBoxLayout()
        self.wrapping_layout_2.setObjectName(u"wrapping_layout_2")
        self.options_layout_2 = QHBoxLayout()
        self.options_layout_2.setObjectName(u"options_layout_2")
        self.active_button_2 = QRadioButton(self.tab_2)
        self.active_button_2.setObjectName(u"active_button_2")

        self.options_layout_2.addWidget(self.active_button_2)

        self.asymmetric_button_2 = QCheckBox(self.tab_2)
        self.asymmetric_button_2.setObjectName(u"asymmetric_button_2")
        self.asymmetric_button_2.setTristate(False)

        self.options_layout_2.addWidget(self.asymmetric_button_2)


        self.wrapping_layout_2.addLayout(self.options_layout_2)

        self.parameter_layout_2 = QGridLayout()
        self.parameter_layout_2.setObjectName(u"parameter_layout_2")
        self.amplitude_slider_2 = QSlider(self.tab_2)
        self.amplitude_slider_2.setObjectName(u"amplitude_slider_2")
        sizePolicy.setHeightForWidth(self.amplitude_slider_2.sizePolicy().hasHeightForWidth())
        self.amplitude_slider_2.setSizePolicy(sizePolicy)
        self.amplitude_slider_2.setMaximum(15)
        self.amplitude_slider_2.setOrientation(Qt.Vertical)

        self.parameter_layout_2.addWidget(self.amplitude_slider_2, 2, 2, 1, 1)

        self.frequency_label_2 = QLabel(self.tab_2)
        self.frequency_label_2.setObjectName(u"frequency_label_2")
        sizePolicy1.setHeightForWidth(self.frequency_label_2.sizePolicy().hasHeightForWidth())
        self.frequency_label_2.setSizePolicy(sizePolicy1)
        self.frequency_label_2.setAlignment(Qt.AlignCenter)

        self.parameter_layout_2.addWidget(self.frequency_label_2, 0, 1, 1, 1)

        self.amplitude_falling_layout_2 = QFrame(self.tab_2)
        self.amplitude_falling_layout_2.setObjectName(u"amplitude_falling_layout_2")
        self.amplitude_2_layout_3 = QVBoxLayout(self.amplitude_falling_layout_2)
        self.amplitude_2_layout_3.setObjectName(u"amplitude_2_layout_3")
        self.amplitude_2_layout_3.setContentsMargins(0, 0, 0, 0)
        self.amplitude_falling_label_2 = QLabel(self.amplitude_falling_layout_2)
        self.amplitude_falling_label_2.setObjectName(u"amplitude_falling_label_2")
        sizePolicy1.setHeightForWidth(self.amplitude_falling_label_2.sizePolicy().hasHeightForWidth())
        self.amplitude_falling_label_2.setSizePolicy(sizePolicy1)
        self.amplitude_falling_label_2.setAlignment(Qt.AlignCenter)

        self.amplitude_2_layout_3.addWidget(self.amplitude_falling_label_2)

        self.amplitude_falling_value_2 = QLabel(self.amplitude_falling_layout_2)
        self.amplitude_falling_value_2.setObjectName(u"amplitude_falling_value_2")

        self.amplitude_2_layout_3.addWidget(self.amplitude_falling_value_2)

        self.amplitude_falling_slider_2 = QSlider(self.amplitude_falling_layout_2)
        self.amplitude_falling_slider_2.setObjectName(u"amplitude_falling_slider_2")
        sizePolicy.setHeightForWidth(self.amplitude_falling_slider_2.sizePolicy().hasHeightForWidth())
        self.amplitude_falling_slider_2.setSizePolicy(sizePolicy)
        self.amplitude_falling_slider_2.setMaximum(15)
        self.amplitude_falling_slider_2.setOrientation(Qt.Vertical)

        self.amplitude_2_layout_3.addWidget(self.amplitude_falling_slider_2)


        self.parameter_layout_2.addWidget(self.amplitude_falling_layout_2, 0, 3, 3, 1)

        self.pulse_width_value_2 = QLabel(self.tab_2)
        self.pulse_width_value_2.setObjectName(u"pulse_width_value_2")

        self.parameter_layout_2.addWidget(self.pulse_width_value_2, 1, 0, 1, 1)

        self.frequency_slider_2 = QSlider(self.tab_2)
        self.frequency_slider_2.setObjectName(u"frequency_slider_2")
        sizePolicy.setHeightForWidth(self.frequency_slider_2.sizePolicy().hasHeightForWidth())
        self.frequency_slider_2.setSizePolicy(sizePolicy)
        self.frequency_slider_2.setMaximum(200)
        self.frequency_slider_2.setOrientation(Qt.Vertical)

        self.parameter_layout_2.addWidget(self.frequency_slider_2, 2, 1, 1, 1)

        self.amplitude_label_2 = QLabel(self.tab_2)
        self.amplitude_label_2.setObjectName(u"amplitude_label_2")
        sizePolicy1.setHeightForWidth(self.amplitude_label_2.sizePolicy().hasHeightForWidth())
        self.amplitude_label_2.setSizePolicy(sizePolicy1)
        self.amplitude_label_2.setAlignment(Qt.AlignCenter)

        self.parameter_layout_2.addWidget(self.amplitude_label_2, 0, 2, 1, 1)

        self.frequency_value_2 = QLabel(self.tab_2)
        self.frequency_value_2.setObjectName(u"frequency_value_2")

        self.parameter_layout_2.addWidget(self.frequency_value_2, 1, 1, 1, 1)

        self.pulse_width_label_2 = QLabel(self.tab_2)
        self.pulse_width_label_2.setObjectName(u"pulse_width_label_2")
        sizePolicy1.setHeightForWidth(self.pulse_width_label_2.sizePolicy().hasHeightForWidth())
        self.pulse_width_label_2.setSizePolicy(sizePolicy1)
        self.pulse_width_label_2.setAlignment(Qt.AlignCenter)
        self.pulse_width_label_2.setWordWrap(False)

        self.parameter_layout_2.addWidget(self.pulse_width_label_2, 0, 0, 1, 1)

        self.pulse_width_slider_2 = QSlider(self.tab_2)
        self.pulse_width_slider_2.setObjectName(u"pulse_width_slider_2")
        sizePolicy.setHeightForWidth(self.pulse_width_slider_2.sizePolicy().hasHeightForWidth())
        self.pulse_width_slider_2.setSizePolicy(sizePolicy)
        self.pulse_width_slider_2.setMaximum(200)
        self.pulse_width_slider_2.setOrientation(Qt.Vertical)

        self.parameter_layout_2.addWidget(self.pulse_width_slider_2, 2, 0, 1, 1)

        self.amplitude_value_2 = QLabel(self.tab_2)
        self.amplitude_value_2.setObjectName(u"amplitude_value_2")

        self.parameter_layout_2.addWidget(self.amplitude_value_2, 1, 2, 1, 1)


        self.wrapping_layout_2.addLayout(self.parameter_layout_2)


        self.gridLayout_2.addLayout(self.wrapping_layout_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.wrapping_layout_3 = QVBoxLayout()
        self.wrapping_layout_3.setObjectName(u"wrapping_layout_3")
        self.options_layout_3 = QHBoxLayout()
        self.options_layout_3.setObjectName(u"options_layout_3")
        self.active_button_3 = QRadioButton(self.tab_3)
        self.active_button_3.setObjectName(u"active_button_3")

        self.options_layout_3.addWidget(self.active_button_3)

        self.asymmetric_button_3 = QCheckBox(self.tab_3)
        self.asymmetric_button_3.setObjectName(u"asymmetric_button_3")
        self.asymmetric_button_3.setTristate(False)

        self.options_layout_3.addWidget(self.asymmetric_button_3)


        self.wrapping_layout_3.addLayout(self.options_layout_3)

        self.parameter_layout_3 = QGridLayout()
        self.parameter_layout_3.setObjectName(u"parameter_layout_3")
        self.amplitude_slider_3 = QSlider(self.tab_3)
        self.amplitude_slider_3.setObjectName(u"amplitude_slider_3")
        sizePolicy.setHeightForWidth(self.amplitude_slider_3.sizePolicy().hasHeightForWidth())
        self.amplitude_slider_3.setSizePolicy(sizePolicy)
        self.amplitude_slider_3.setMaximum(15)
        self.amplitude_slider_3.setOrientation(Qt.Vertical)

        self.parameter_layout_3.addWidget(self.amplitude_slider_3, 2, 2, 1, 1)

        self.frequency_label_3 = QLabel(self.tab_3)
        self.frequency_label_3.setObjectName(u"frequency_label_3")
        sizePolicy1.setHeightForWidth(self.frequency_label_3.sizePolicy().hasHeightForWidth())
        self.frequency_label_3.setSizePolicy(sizePolicy1)
        self.frequency_label_3.setAlignment(Qt.AlignCenter)

        self.parameter_layout_3.addWidget(self.frequency_label_3, 0, 1, 1, 1)

        self.amplitude_falling_layout_3 = QFrame(self.tab_3)
        self.amplitude_falling_layout_3.setObjectName(u"amplitude_falling_layout_3")
        self.amplitude_2_layout_4 = QVBoxLayout(self.amplitude_falling_layout_3)
        self.amplitude_2_layout_4.setObjectName(u"amplitude_2_layout_4")
        self.amplitude_2_layout_4.setContentsMargins(0, 0, 0, 0)
        self.amplitude_falling_label_3 = QLabel(self.amplitude_falling_layout_3)
        self.amplitude_falling_label_3.setObjectName(u"amplitude_falling_label_3")
        sizePolicy1.setHeightForWidth(self.amplitude_falling_label_3.sizePolicy().hasHeightForWidth())
        self.amplitude_falling_label_3.setSizePolicy(sizePolicy1)
        self.amplitude_falling_label_3.setAlignment(Qt.AlignCenter)

        self.amplitude_2_layout_4.addWidget(self.amplitude_falling_label_3)

        self.amplitude_falling_value_3 = QLabel(self.amplitude_falling_layout_3)
        self.amplitude_falling_value_3.setObjectName(u"amplitude_falling_value_3")

        self.amplitude_2_layout_4.addWidget(self.amplitude_falling_value_3)

        self.amplitude_falling_slider_3 = QSlider(self.amplitude_falling_layout_3)
        self.amplitude_falling_slider_3.setObjectName(u"amplitude_falling_slider_3")
        sizePolicy.setHeightForWidth(self.amplitude_falling_slider_3.sizePolicy().hasHeightForWidth())
        self.amplitude_falling_slider_3.setSizePolicy(sizePolicy)
        self.amplitude_falling_slider_3.setMaximum(15)
        self.amplitude_falling_slider_3.setOrientation(Qt.Vertical)

        self.amplitude_2_layout_4.addWidget(self.amplitude_falling_slider_3)


        self.parameter_layout_3.addWidget(self.amplitude_falling_layout_3, 0, 3, 3, 1)

        self.pulse_width_value_3 = QLabel(self.tab_3)
        self.pulse_width_value_3.setObjectName(u"pulse_width_value_3")

        self.parameter_layout_3.addWidget(self.pulse_width_value_3, 1, 0, 1, 1)

        self.frequency_slider_3 = QSlider(self.tab_3)
        self.frequency_slider_3.setObjectName(u"frequency_slider_3")
        sizePolicy.setHeightForWidth(self.frequency_slider_3.sizePolicy().hasHeightForWidth())
        self.frequency_slider_3.setSizePolicy(sizePolicy)
        self.frequency_slider_3.setMaximum(200)
        self.frequency_slider_3.setOrientation(Qt.Vertical)

        self.parameter_layout_3.addWidget(self.frequency_slider_3, 2, 1, 1, 1)

        self.amplitude_label_3 = QLabel(self.tab_3)
        self.amplitude_label_3.setObjectName(u"amplitude_label_3")
        sizePolicy1.setHeightForWidth(self.amplitude_label_3.sizePolicy().hasHeightForWidth())
        self.amplitude_label_3.setSizePolicy(sizePolicy1)
        self.amplitude_label_3.setAlignment(Qt.AlignCenter)

        self.parameter_layout_3.addWidget(self.amplitude_label_3, 0, 2, 1, 1)

        self.frequency_value_3 = QLabel(self.tab_3)
        self.frequency_value_3.setObjectName(u"frequency_value_3")

        self.parameter_layout_3.addWidget(self.frequency_value_3, 1, 1, 1, 1)

        self.pulse_width_label_3 = QLabel(self.tab_3)
        self.pulse_width_label_3.setObjectName(u"pulse_width_label_3")
        sizePolicy1.setHeightForWidth(self.pulse_width_label_3.sizePolicy().hasHeightForWidth())
        self.pulse_width_label_3.setSizePolicy(sizePolicy1)
        self.pulse_width_label_3.setAlignment(Qt.AlignCenter)
        self.pulse_width_label_3.setWordWrap(False)

        self.parameter_layout_3.addWidget(self.pulse_width_label_3, 0, 0, 1, 1)

        self.pulse_width_slider_3 = QSlider(self.tab_3)
        self.pulse_width_slider_3.setObjectName(u"pulse_width_slider_3")
        sizePolicy.setHeightForWidth(self.pulse_width_slider_3.sizePolicy().hasHeightForWidth())
        self.pulse_width_slider_3.setSizePolicy(sizePolicy)
        self.pulse_width_slider_3.setMaximum(200)
        self.pulse_width_slider_3.setOrientation(Qt.Vertical)

        self.parameter_layout_3.addWidget(self.pulse_width_slider_3, 2, 0, 1, 1)

        self.amplitude_value_3 = QLabel(self.tab_3)
        self.amplitude_value_3.setObjectName(u"amplitude_value_3")

        self.parameter_layout_3.addWidget(self.amplitude_value_3, 1, 2, 1, 1)


        self.wrapping_layout_3.addLayout(self.parameter_layout_3)


        self.gridLayout_3.addLayout(self.wrapping_layout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.wrapping_layout_4 = QVBoxLayout()
        self.wrapping_layout_4.setObjectName(u"wrapping_layout_4")
        self.options_layout_4 = QHBoxLayout()
        self.options_layout_4.setObjectName(u"options_layout_4")
        self.active_button_4 = QRadioButton(self.tab_4)
        self.active_button_4.setObjectName(u"active_button_4")

        self.options_layout_4.addWidget(self.active_button_4)

        self.asymmetric_button_4 = QCheckBox(self.tab_4)
        self.asymmetric_button_4.setObjectName(u"asymmetric_button_4")
        self.asymmetric_button_4.setTristate(False)

        self.options_layout_4.addWidget(self.asymmetric_button_4)


        self.wrapping_layout_4.addLayout(self.options_layout_4)

        self.parameter_layout_4 = QGridLayout()
        self.parameter_layout_4.setObjectName(u"parameter_layout_4")
        self.amplitude_slider_4 = QSlider(self.tab_4)
        self.amplitude_slider_4.setObjectName(u"amplitude_slider_4")
        sizePolicy.setHeightForWidth(self.amplitude_slider_4.sizePolicy().hasHeightForWidth())
        self.amplitude_slider_4.setSizePolicy(sizePolicy)
        self.amplitude_slider_4.setMaximum(15)
        self.amplitude_slider_4.setOrientation(Qt.Vertical)

        self.parameter_layout_4.addWidget(self.amplitude_slider_4, 2, 2, 1, 1)

        self.frequency_label_4 = QLabel(self.tab_4)
        self.frequency_label_4.setObjectName(u"frequency_label_4")
        sizePolicy1.setHeightForWidth(self.frequency_label_4.sizePolicy().hasHeightForWidth())
        self.frequency_label_4.setSizePolicy(sizePolicy1)
        self.frequency_label_4.setAlignment(Qt.AlignCenter)

        self.parameter_layout_4.addWidget(self.frequency_label_4, 0, 1, 1, 1)

        self.amplitude_falling_layout_4 = QFrame(self.tab_4)
        self.amplitude_falling_layout_4.setObjectName(u"amplitude_falling_layout_4")
        self.amplitude_2_layout_5 = QVBoxLayout(self.amplitude_falling_layout_4)
        self.amplitude_2_layout_5.setObjectName(u"amplitude_2_layout_5")
        self.amplitude_2_layout_5.setContentsMargins(0, 0, 0, 0)
        self.amplitude_falling_label_4 = QLabel(self.amplitude_falling_layout_4)
        self.amplitude_falling_label_4.setObjectName(u"amplitude_falling_label_4")
        sizePolicy1.setHeightForWidth(self.amplitude_falling_label_4.sizePolicy().hasHeightForWidth())
        self.amplitude_falling_label_4.setSizePolicy(sizePolicy1)
        self.amplitude_falling_label_4.setAlignment(Qt.AlignCenter)

        self.amplitude_2_layout_5.addWidget(self.amplitude_falling_label_4)

        self.amplitude_falling_value_4 = QLabel(self.amplitude_falling_layout_4)
        self.amplitude_falling_value_4.setObjectName(u"amplitude_falling_value_4")

        self.amplitude_2_layout_5.addWidget(self.amplitude_falling_value_4)

        self.amplitude_falling_slider_4 = QSlider(self.amplitude_falling_layout_4)
        self.amplitude_falling_slider_4.setObjectName(u"amplitude_falling_slider_4")
        sizePolicy.setHeightForWidth(self.amplitude_falling_slider_4.sizePolicy().hasHeightForWidth())
        self.amplitude_falling_slider_4.setSizePolicy(sizePolicy)
        self.amplitude_falling_slider_4.setMaximum(15)
        self.amplitude_falling_slider_4.setOrientation(Qt.Vertical)

        self.amplitude_2_layout_5.addWidget(self.amplitude_falling_slider_4)


        self.parameter_layout_4.addWidget(self.amplitude_falling_layout_4, 0, 3, 3, 1)

        self.pulse_width_value_4 = QLabel(self.tab_4)
        self.pulse_width_value_4.setObjectName(u"pulse_width_value_4")

        self.parameter_layout_4.addWidget(self.pulse_width_value_4, 1, 0, 1, 1)

        self.frequency_slider_4 = QSlider(self.tab_4)
        self.frequency_slider_4.setObjectName(u"frequency_slider_4")
        sizePolicy.setHeightForWidth(self.frequency_slider_4.sizePolicy().hasHeightForWidth())
        self.frequency_slider_4.setSizePolicy(sizePolicy)
        self.frequency_slider_4.setMaximum(200)
        self.frequency_slider_4.setOrientation(Qt.Vertical)

        self.parameter_layout_4.addWidget(self.frequency_slider_4, 2, 1, 1, 1)

        self.amplitude_label_4 = QLabel(self.tab_4)
        self.amplitude_label_4.setObjectName(u"amplitude_label_4")
        sizePolicy1.setHeightForWidth(self.amplitude_label_4.sizePolicy().hasHeightForWidth())
        self.amplitude_label_4.setSizePolicy(sizePolicy1)
        self.amplitude_label_4.setAlignment(Qt.AlignCenter)

        self.parameter_layout_4.addWidget(self.amplitude_label_4, 0, 2, 1, 1)

        self.frequency_value_4 = QLabel(self.tab_4)
        self.frequency_value_4.setObjectName(u"frequency_value_4")

        self.parameter_layout_4.addWidget(self.frequency_value_4, 1, 1, 1, 1)

        self.pulse_width_label_4 = QLabel(self.tab_4)
        self.pulse_width_label_4.setObjectName(u"pulse_width_label_4")
        sizePolicy1.setHeightForWidth(self.pulse_width_label_4.sizePolicy().hasHeightForWidth())
        self.pulse_width_label_4.setSizePolicy(sizePolicy1)
        self.pulse_width_label_4.setAlignment(Qt.AlignCenter)
        self.pulse_width_label_4.setWordWrap(False)

        self.parameter_layout_4.addWidget(self.pulse_width_label_4, 0, 0, 1, 1)

        self.pulse_width_slider_4 = QSlider(self.tab_4)
        self.pulse_width_slider_4.setObjectName(u"pulse_width_slider_4")
        sizePolicy.setHeightForWidth(self.pulse_width_slider_4.sizePolicy().hasHeightForWidth())
        self.pulse_width_slider_4.setSizePolicy(sizePolicy)
        self.pulse_width_slider_4.setMaximum(200)
        self.pulse_width_slider_4.setOrientation(Qt.Vertical)

        self.parameter_layout_4.addWidget(self.pulse_width_slider_4, 2, 0, 1, 1)

        self.amplitude_value_4 = QLabel(self.tab_4)
        self.amplitude_value_4.setObjectName(u"amplitude_value_4")

        self.parameter_layout_4.addWidget(self.amplitude_value_4, 1, 2, 1, 1)


        self.wrapping_layout_4.addLayout(self.parameter_layout_4)


        self.gridLayout_4.addLayout(self.wrapping_layout_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_5 = QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.wrapping_layout_5 = QVBoxLayout()
        self.wrapping_layout_5.setObjectName(u"wrapping_layout_5")
        self.options_layout_5 = QHBoxLayout()
        self.options_layout_5.setObjectName(u"options_layout_5")
        self.active_button_5 = QRadioButton(self.tab_5)
        self.active_button_5.setObjectName(u"active_button_5")

        self.options_layout_5.addWidget(self.active_button_5)

        self.asymmetric_button_5 = QCheckBox(self.tab_5)
        self.asymmetric_button_5.setObjectName(u"asymmetric_button_5")
        self.asymmetric_button_5.setTristate(False)

        self.options_layout_5.addWidget(self.asymmetric_button_5)


        self.wrapping_layout_5.addLayout(self.options_layout_5)

        self.parameter_layout_5 = QGridLayout()
        self.parameter_layout_5.setObjectName(u"parameter_layout_5")
        self.amplitude_slider_5 = QSlider(self.tab_5)
        self.amplitude_slider_5.setObjectName(u"amplitude_slider_5")
        sizePolicy.setHeightForWidth(self.amplitude_slider_5.sizePolicy().hasHeightForWidth())
        self.amplitude_slider_5.setSizePolicy(sizePolicy)
        self.amplitude_slider_5.setMaximum(15)
        self.amplitude_slider_5.setOrientation(Qt.Vertical)

        self.parameter_layout_5.addWidget(self.amplitude_slider_5, 2, 2, 1, 1)

        self.frequency_label_5 = QLabel(self.tab_5)
        self.frequency_label_5.setObjectName(u"frequency_label_5")
        sizePolicy1.setHeightForWidth(self.frequency_label_5.sizePolicy().hasHeightForWidth())
        self.frequency_label_5.setSizePolicy(sizePolicy1)
        self.frequency_label_5.setAlignment(Qt.AlignCenter)

        self.parameter_layout_5.addWidget(self.frequency_label_5, 0, 1, 1, 1)

        self.amplitude_falling_layout_5 = QFrame(self.tab_5)
        self.amplitude_falling_layout_5.setObjectName(u"amplitude_falling_layout_5")
        self.amplitude_2_layout_6 = QVBoxLayout(self.amplitude_falling_layout_5)
        self.amplitude_2_layout_6.setObjectName(u"amplitude_2_layout_6")
        self.amplitude_2_layout_6.setContentsMargins(0, 0, 0, 0)
        self.amplitude_falling_label_5 = QLabel(self.amplitude_falling_layout_5)
        self.amplitude_falling_label_5.setObjectName(u"amplitude_falling_label_5")
        sizePolicy1.setHeightForWidth(self.amplitude_falling_label_5.sizePolicy().hasHeightForWidth())
        self.amplitude_falling_label_5.setSizePolicy(sizePolicy1)
        self.amplitude_falling_label_5.setAlignment(Qt.AlignCenter)

        self.amplitude_2_layout_6.addWidget(self.amplitude_falling_label_5)

        self.amplitude_falling_value_5 = QLabel(self.amplitude_falling_layout_5)
        self.amplitude_falling_value_5.setObjectName(u"amplitude_falling_value_5")

        self.amplitude_2_layout_6.addWidget(self.amplitude_falling_value_5)

        self.amplitude_falling_slider_5 = QSlider(self.amplitude_falling_layout_5)
        self.amplitude_falling_slider_5.setObjectName(u"amplitude_falling_slider_5")
        sizePolicy.setHeightForWidth(self.amplitude_falling_slider_5.sizePolicy().hasHeightForWidth())
        self.amplitude_falling_slider_5.setSizePolicy(sizePolicy)
        self.amplitude_falling_slider_5.setMaximum(15)
        self.amplitude_falling_slider_5.setOrientation(Qt.Vertical)

        self.amplitude_2_layout_6.addWidget(self.amplitude_falling_slider_5)


        self.parameter_layout_5.addWidget(self.amplitude_falling_layout_5, 0, 3, 3, 1)

        self.pulse_width_value_5 = QLabel(self.tab_5)
        self.pulse_width_value_5.setObjectName(u"pulse_width_value_5")

        self.parameter_layout_5.addWidget(self.pulse_width_value_5, 1, 0, 1, 1)

        self.frequency_slider_5 = QSlider(self.tab_5)
        self.frequency_slider_5.setObjectName(u"frequency_slider_5")
        sizePolicy.setHeightForWidth(self.frequency_slider_5.sizePolicy().hasHeightForWidth())
        self.frequency_slider_5.setSizePolicy(sizePolicy)
        self.frequency_slider_5.setMaximum(200)
        self.frequency_slider_5.setOrientation(Qt.Vertical)

        self.parameter_layout_5.addWidget(self.frequency_slider_5, 2, 1, 1, 1)

        self.amplitude_label_5 = QLabel(self.tab_5)
        self.amplitude_label_5.setObjectName(u"amplitude_label_5")
        sizePolicy1.setHeightForWidth(self.amplitude_label_5.sizePolicy().hasHeightForWidth())
        self.amplitude_label_5.setSizePolicy(sizePolicy1)
        self.amplitude_label_5.setAlignment(Qt.AlignCenter)

        self.parameter_layout_5.addWidget(self.amplitude_label_5, 0, 2, 1, 1)

        self.frequency_value_5 = QLabel(self.tab_5)
        self.frequency_value_5.setObjectName(u"frequency_value_5")

        self.parameter_layout_5.addWidget(self.frequency_value_5, 1, 1, 1, 1)

        self.pulse_width_label_5 = QLabel(self.tab_5)
        self.pulse_width_label_5.setObjectName(u"pulse_width_label_5")
        sizePolicy1.setHeightForWidth(self.pulse_width_label_5.sizePolicy().hasHeightForWidth())
        self.pulse_width_label_5.setSizePolicy(sizePolicy1)
        self.pulse_width_label_5.setAlignment(Qt.AlignCenter)
        self.pulse_width_label_5.setWordWrap(False)

        self.parameter_layout_5.addWidget(self.pulse_width_label_5, 0, 0, 1, 1)

        self.pulse_width_slider_5 = QSlider(self.tab_5)
        self.pulse_width_slider_5.setObjectName(u"pulse_width_slider_5")
        sizePolicy.setHeightForWidth(self.pulse_width_slider_5.sizePolicy().hasHeightForWidth())
        self.pulse_width_slider_5.setSizePolicy(sizePolicy)
        self.pulse_width_slider_5.setMaximum(200)
        self.pulse_width_slider_5.setOrientation(Qt.Vertical)

        self.parameter_layout_5.addWidget(self.pulse_width_slider_5, 2, 0, 1, 1)

        self.amplitude_value_5 = QLabel(self.tab_5)
        self.amplitude_value_5.setObjectName(u"amplitude_value_5")

        self.parameter_layout_5.addWidget(self.amplitude_value_5, 1, 2, 1, 1)


        self.wrapping_layout_5.addLayout(self.parameter_layout_5)


        self.gridLayout_5.addLayout(self.wrapping_layout_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_6 = QGridLayout(self.tab_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.wrapping_layout_6 = QVBoxLayout()
        self.wrapping_layout_6.setObjectName(u"wrapping_layout_6")
        self.options_layout_6 = QHBoxLayout()
        self.options_layout_6.setObjectName(u"options_layout_6")
        self.active_button_6 = QRadioButton(self.tab_6)
        self.active_button_6.setObjectName(u"active_button_6")

        self.options_layout_6.addWidget(self.active_button_6)

        self.asymmetric_button_6 = QCheckBox(self.tab_6)
        self.asymmetric_button_6.setObjectName(u"asymmetric_button_6")
        self.asymmetric_button_6.setTristate(False)

        self.options_layout_6.addWidget(self.asymmetric_button_6)


        self.wrapping_layout_6.addLayout(self.options_layout_6)

        self.parameter_layout_6 = QGridLayout()
        self.parameter_layout_6.setObjectName(u"parameter_layout_6")
        self.amplitude_slider_6 = QSlider(self.tab_6)
        self.amplitude_slider_6.setObjectName(u"amplitude_slider_6")
        sizePolicy.setHeightForWidth(self.amplitude_slider_6.sizePolicy().hasHeightForWidth())
        self.amplitude_slider_6.setSizePolicy(sizePolicy)
        self.amplitude_slider_6.setMaximum(15)
        self.amplitude_slider_6.setOrientation(Qt.Vertical)

        self.parameter_layout_6.addWidget(self.amplitude_slider_6, 2, 2, 1, 1)

        self.frequency_label_6 = QLabel(self.tab_6)
        self.frequency_label_6.setObjectName(u"frequency_label_6")
        sizePolicy1.setHeightForWidth(self.frequency_label_6.sizePolicy().hasHeightForWidth())
        self.frequency_label_6.setSizePolicy(sizePolicy1)
        self.frequency_label_6.setAlignment(Qt.AlignCenter)

        self.parameter_layout_6.addWidget(self.frequency_label_6, 0, 1, 1, 1)

        self.amplitude_falling_layout_6 = QFrame(self.tab_6)
        self.amplitude_falling_layout_6.setObjectName(u"amplitude_falling_layout_6")
        self.amplitude_2_layout_7 = QVBoxLayout(self.amplitude_falling_layout_6)
        self.amplitude_2_layout_7.setObjectName(u"amplitude_2_layout_7")
        self.amplitude_2_layout_7.setContentsMargins(0, 0, 0, 0)
        self.amplitude_falling_label_6 = QLabel(self.amplitude_falling_layout_6)
        self.amplitude_falling_label_6.setObjectName(u"amplitude_falling_label_6")
        sizePolicy1.setHeightForWidth(self.amplitude_falling_label_6.sizePolicy().hasHeightForWidth())
        self.amplitude_falling_label_6.setSizePolicy(sizePolicy1)
        self.amplitude_falling_label_6.setAlignment(Qt.AlignCenter)

        self.amplitude_2_layout_7.addWidget(self.amplitude_falling_label_6)

        self.amplitude_falling_value_6 = QLabel(self.amplitude_falling_layout_6)
        self.amplitude_falling_value_6.setObjectName(u"amplitude_falling_value_6")

        self.amplitude_2_layout_7.addWidget(self.amplitude_falling_value_6)

        self.amplitude_falling_slider_6 = QSlider(self.amplitude_falling_layout_6)
        self.amplitude_falling_slider_6.setObjectName(u"amplitude_falling_slider_6")
        sizePolicy.setHeightForWidth(self.amplitude_falling_slider_6.sizePolicy().hasHeightForWidth())
        self.amplitude_falling_slider_6.setSizePolicy(sizePolicy)
        self.amplitude_falling_slider_6.setMaximum(15)
        self.amplitude_falling_slider_6.setOrientation(Qt.Vertical)

        self.amplitude_2_layout_7.addWidget(self.amplitude_falling_slider_6)


        self.parameter_layout_6.addWidget(self.amplitude_falling_layout_6, 0, 3, 3, 1)

        self.pulse_width_value_6 = QLabel(self.tab_6)
        self.pulse_width_value_6.setObjectName(u"pulse_width_value_6")

        self.parameter_layout_6.addWidget(self.pulse_width_value_6, 1, 0, 1, 1)

        self.frequency_slider_6 = QSlider(self.tab_6)
        self.frequency_slider_6.setObjectName(u"frequency_slider_6")
        sizePolicy.setHeightForWidth(self.frequency_slider_6.sizePolicy().hasHeightForWidth())
        self.frequency_slider_6.setSizePolicy(sizePolicy)
        self.frequency_slider_6.setMaximum(200)
        self.frequency_slider_6.setOrientation(Qt.Vertical)

        self.parameter_layout_6.addWidget(self.frequency_slider_6, 2, 1, 1, 1)

        self.amplitude_label_6 = QLabel(self.tab_6)
        self.amplitude_label_6.setObjectName(u"amplitude_label_6")
        sizePolicy1.setHeightForWidth(self.amplitude_label_6.sizePolicy().hasHeightForWidth())
        self.amplitude_label_6.setSizePolicy(sizePolicy1)
        self.amplitude_label_6.setAlignment(Qt.AlignCenter)

        self.parameter_layout_6.addWidget(self.amplitude_label_6, 0, 2, 1, 1)

        self.frequency_value_6 = QLabel(self.tab_6)
        self.frequency_value_6.setObjectName(u"frequency_value_6")

        self.parameter_layout_6.addWidget(self.frequency_value_6, 1, 1, 1, 1)

        self.pulse_width_label_6 = QLabel(self.tab_6)
        self.pulse_width_label_6.setObjectName(u"pulse_width_label_6")
        sizePolicy1.setHeightForWidth(self.pulse_width_label_6.sizePolicy().hasHeightForWidth())
        self.pulse_width_label_6.setSizePolicy(sizePolicy1)
        self.pulse_width_label_6.setAlignment(Qt.AlignCenter)
        self.pulse_width_label_6.setWordWrap(False)

        self.parameter_layout_6.addWidget(self.pulse_width_label_6, 0, 0, 1, 1)

        self.pulse_width_slider_6 = QSlider(self.tab_6)
        self.pulse_width_slider_6.setObjectName(u"pulse_width_slider_6")
        sizePolicy.setHeightForWidth(self.pulse_width_slider_6.sizePolicy().hasHeightForWidth())
        self.pulse_width_slider_6.setSizePolicy(sizePolicy)
        self.pulse_width_slider_6.setMaximum(200)
        self.pulse_width_slider_6.setOrientation(Qt.Vertical)

        self.parameter_layout_6.addWidget(self.pulse_width_slider_6, 2, 0, 1, 1)

        self.amplitude_value_6 = QLabel(self.tab_6)
        self.amplitude_value_6.setObjectName(u"amplitude_value_6")

        self.parameter_layout_6.addWidget(self.amplitude_value_6, 1, 2, 1, 1)


        self.wrapping_layout_6.addLayout(self.parameter_layout_6)


        self.gridLayout_6.addLayout(self.wrapping_layout_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_7 = QGridLayout(self.tab_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.wrapping_layout_7 = QVBoxLayout()
        self.wrapping_layout_7.setObjectName(u"wrapping_layout_7")
        self.options_layout_7 = QHBoxLayout()
        self.options_layout_7.setObjectName(u"options_layout_7")
        self.active_button_7 = QRadioButton(self.tab_7)
        self.active_button_7.setObjectName(u"active_button_7")

        self.options_layout_7.addWidget(self.active_button_7)

        self.asymmetric_button_7 = QCheckBox(self.tab_7)
        self.asymmetric_button_7.setObjectName(u"asymmetric_button_7")
        self.asymmetric_button_7.setTristate(False)

        self.options_layout_7.addWidget(self.asymmetric_button_7)


        self.wrapping_layout_7.addLayout(self.options_layout_7)

        self.parameter_layout_7 = QGridLayout()
        self.parameter_layout_7.setObjectName(u"parameter_layout_7")
        self.amplitude_slider_7 = QSlider(self.tab_7)
        self.amplitude_slider_7.setObjectName(u"amplitude_slider_7")
        sizePolicy.setHeightForWidth(self.amplitude_slider_7.sizePolicy().hasHeightForWidth())
        self.amplitude_slider_7.setSizePolicy(sizePolicy)
        self.amplitude_slider_7.setMaximum(15)
        self.amplitude_slider_7.setOrientation(Qt.Vertical)

        self.parameter_layout_7.addWidget(self.amplitude_slider_7, 2, 2, 1, 1)

        self.frequency_label_7 = QLabel(self.tab_7)
        self.frequency_label_7.setObjectName(u"frequency_label_7")
        sizePolicy1.setHeightForWidth(self.frequency_label_7.sizePolicy().hasHeightForWidth())
        self.frequency_label_7.setSizePolicy(sizePolicy1)
        self.frequency_label_7.setAlignment(Qt.AlignCenter)

        self.parameter_layout_7.addWidget(self.frequency_label_7, 0, 1, 1, 1)

        self.amplitude_falling_layout_7 = QFrame(self.tab_7)
        self.amplitude_falling_layout_7.setObjectName(u"amplitude_falling_layout_7")
        self.amplitude_2_layout_8 = QVBoxLayout(self.amplitude_falling_layout_7)
        self.amplitude_2_layout_8.setObjectName(u"amplitude_2_layout_8")
        self.amplitude_2_layout_8.setContentsMargins(0, 0, 0, 0)
        self.amplitude_falling_label_7 = QLabel(self.amplitude_falling_layout_7)
        self.amplitude_falling_label_7.setObjectName(u"amplitude_falling_label_7")
        sizePolicy1.setHeightForWidth(self.amplitude_falling_label_7.sizePolicy().hasHeightForWidth())
        self.amplitude_falling_label_7.setSizePolicy(sizePolicy1)
        self.amplitude_falling_label_7.setAlignment(Qt.AlignCenter)

        self.amplitude_2_layout_8.addWidget(self.amplitude_falling_label_7)

        self.amplitude_falling_value_7 = QLabel(self.amplitude_falling_layout_7)
        self.amplitude_falling_value_7.setObjectName(u"amplitude_falling_value_7")

        self.amplitude_2_layout_8.addWidget(self.amplitude_falling_value_7)

        self.amplitude_falling_slider_7 = QSlider(self.amplitude_falling_layout_7)
        self.amplitude_falling_slider_7.setObjectName(u"amplitude_falling_slider_7")
        sizePolicy.setHeightForWidth(self.amplitude_falling_slider_7.sizePolicy().hasHeightForWidth())
        self.amplitude_falling_slider_7.setSizePolicy(sizePolicy)
        self.amplitude_falling_slider_7.setMaximum(15)
        self.amplitude_falling_slider_7.setOrientation(Qt.Vertical)

        self.amplitude_2_layout_8.addWidget(self.amplitude_falling_slider_7)


        self.parameter_layout_7.addWidget(self.amplitude_falling_layout_7, 0, 3, 3, 1)

        self.pulse_width_value_7 = QLabel(self.tab_7)
        self.pulse_width_value_7.setObjectName(u"pulse_width_value_7")

        self.parameter_layout_7.addWidget(self.pulse_width_value_7, 1, 0, 1, 1)

        self.frequency_slider_7 = QSlider(self.tab_7)
        self.frequency_slider_7.setObjectName(u"frequency_slider_7")
        sizePolicy.setHeightForWidth(self.frequency_slider_7.sizePolicy().hasHeightForWidth())
        self.frequency_slider_7.setSizePolicy(sizePolicy)
        self.frequency_slider_7.setMaximum(200)
        self.frequency_slider_7.setOrientation(Qt.Vertical)

        self.parameter_layout_7.addWidget(self.frequency_slider_7, 2, 1, 1, 1)

        self.amplitude_label_7 = QLabel(self.tab_7)
        self.amplitude_label_7.setObjectName(u"amplitude_label_7")
        sizePolicy1.setHeightForWidth(self.amplitude_label_7.sizePolicy().hasHeightForWidth())
        self.amplitude_label_7.setSizePolicy(sizePolicy1)
        self.amplitude_label_7.setAlignment(Qt.AlignCenter)

        self.parameter_layout_7.addWidget(self.amplitude_label_7, 0, 2, 1, 1)

        self.frequency_value_7 = QLabel(self.tab_7)
        self.frequency_value_7.setObjectName(u"frequency_value_7")

        self.parameter_layout_7.addWidget(self.frequency_value_7, 1, 1, 1, 1)

        self.pulse_width_label_7 = QLabel(self.tab_7)
        self.pulse_width_label_7.setObjectName(u"pulse_width_label_7")
        sizePolicy1.setHeightForWidth(self.pulse_width_label_7.sizePolicy().hasHeightForWidth())
        self.pulse_width_label_7.setSizePolicy(sizePolicy1)
        self.pulse_width_label_7.setAlignment(Qt.AlignCenter)
        self.pulse_width_label_7.setWordWrap(False)

        self.parameter_layout_7.addWidget(self.pulse_width_label_7, 0, 0, 1, 1)

        self.pulse_width_slider_7 = QSlider(self.tab_7)
        self.pulse_width_slider_7.setObjectName(u"pulse_width_slider_7")
        sizePolicy.setHeightForWidth(self.pulse_width_slider_7.sizePolicy().hasHeightForWidth())
        self.pulse_width_slider_7.setSizePolicy(sizePolicy)
        self.pulse_width_slider_7.setMaximum(200)
        self.pulse_width_slider_7.setOrientation(Qt.Vertical)

        self.parameter_layout_7.addWidget(self.pulse_width_slider_7, 2, 0, 1, 1)

        self.amplitude_value_7 = QLabel(self.tab_7)
        self.amplitude_value_7.setObjectName(u"amplitude_value_7")

        self.parameter_layout_7.addWidget(self.amplitude_value_7, 1, 2, 1, 1)


        self.wrapping_layout_7.addLayout(self.parameter_layout_7)


        self.gridLayout_7.addLayout(self.wrapping_layout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_7, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.active_button_0.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.asymmetric_button_0.setText(QCoreApplication.translate("MainWindow", u"Asymmetric", None))
        self.frequency_label_0.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.amplitude_falling_label_0.setText(QCoreApplication.translate("MainWindow", u"Falling Amplitude", None))
        self.amplitude_falling_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pulse_width_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.amplitude_label_0.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.frequency_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pulse_width_label_0.setText(QCoreApplication.translate("MainWindow", u"Pulse Width", None))
        self.amplitude_value_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_0), QCoreApplication.translate("MainWindow", u"Channel 1", None))
        self.active_button_1.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.asymmetric_button_1.setText(QCoreApplication.translate("MainWindow", u"Asymmetric", None))
        self.frequency_label_1.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.amplitude_falling_label_1.setText(QCoreApplication.translate("MainWindow", u"Falling Amplitude", None))
        self.amplitude_falling_value_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pulse_width_value_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.amplitude_label_1.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.frequency_value_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pulse_width_label_1.setText(QCoreApplication.translate("MainWindow", u"Pulse Width", None))
        self.amplitude_value_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Channel 2", None))
        self.active_button_2.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.asymmetric_button_2.setText(QCoreApplication.translate("MainWindow", u"Asymmetric", None))
        self.frequency_label_2.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.amplitude_falling_label_2.setText(QCoreApplication.translate("MainWindow", u"Falling Amplitude", None))
        self.amplitude_falling_value_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pulse_width_value_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.amplitude_label_2.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.frequency_value_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pulse_width_label_2.setText(QCoreApplication.translate("MainWindow", u"Pulse Width", None))
        self.amplitude_value_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Channel 3", None))
        self.active_button_3.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.asymmetric_button_3.setText(QCoreApplication.translate("MainWindow", u"Asymmetric", None))
        self.frequency_label_3.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.amplitude_falling_label_3.setText(QCoreApplication.translate("MainWindow", u"Falling Amplitude", None))
        self.amplitude_falling_value_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pulse_width_value_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.amplitude_label_3.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.frequency_value_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pulse_width_label_3.setText(QCoreApplication.translate("MainWindow", u"Pulse Width", None))
        self.amplitude_value_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Channel 4", None))
        self.active_button_4.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.asymmetric_button_4.setText(QCoreApplication.translate("MainWindow", u"Asymmetric", None))
        self.frequency_label_4.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.amplitude_falling_label_4.setText(QCoreApplication.translate("MainWindow", u"Falling Amplitude", None))
        self.amplitude_falling_value_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pulse_width_value_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.amplitude_label_4.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.frequency_value_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pulse_width_label_4.setText(QCoreApplication.translate("MainWindow", u"Pulse Width", None))
        self.amplitude_value_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Channel 5", None))
        self.active_button_5.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.asymmetric_button_5.setText(QCoreApplication.translate("MainWindow", u"Asymmetric", None))
        self.frequency_label_5.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.amplitude_falling_label_5.setText(QCoreApplication.translate("MainWindow", u"Falling Amplitude", None))
        self.amplitude_falling_value_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pulse_width_value_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.amplitude_label_5.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.frequency_value_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pulse_width_label_5.setText(QCoreApplication.translate("MainWindow", u"Pulse Width", None))
        self.amplitude_value_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Channel 6", None))
        self.active_button_6.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.asymmetric_button_6.setText(QCoreApplication.translate("MainWindow", u"Asymmetric", None))
        self.frequency_label_6.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.amplitude_falling_label_6.setText(QCoreApplication.translate("MainWindow", u"Falling Amplitude", None))
        self.amplitude_falling_value_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pulse_width_value_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.amplitude_label_6.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.frequency_value_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pulse_width_label_6.setText(QCoreApplication.translate("MainWindow", u"Pulse Width", None))
        self.amplitude_value_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Channel 7", None))
        self.active_button_7.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.asymmetric_button_7.setText(QCoreApplication.translate("MainWindow", u"Asymmetric", None))
        self.frequency_label_7.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.amplitude_falling_label_7.setText(QCoreApplication.translate("MainWindow", u"Falling Amplitude", None))
        self.amplitude_falling_value_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pulse_width_value_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.amplitude_label_7.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.frequency_value_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pulse_width_label_7.setText(QCoreApplication.translate("MainWindow", u"Pulse Width", None))
        self.amplitude_value_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Channel 8", None))
    # retranslateUi

