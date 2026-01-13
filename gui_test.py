# from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QDateTime, QDate, QTime, QTimer, Qt
from PySide6.QtWidgets import QApplication, QTableWidgetItem, QTableView, QAbstractItemView, QSizePolicy, QFileDialog
from PySide6.QtGui import QColor, QPalette
import sys
import simple_ui
import slider_ui
import numpy as np
from utils.utils import *
import serial
import copy

class UI_Wrapper(QtWidgets.QMainWindow, simple_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.channel_parameters = np.zeros((8,3))
        self.serial = serial.Serial(port=arduino_port, baudrate=baudrate)
        self.setup()

    def setup(self):
        self.confirm_button.pressed.connect(self.confirm_button_pressed)
        pass
    def confirm_button_pressed(self):
        channel = self.channel_input.currentIndex()
        freq = self.frequency_input.text()
        pulse_width = self.pulse_width_input.text()
        amplitude = self.amplitude_input.text()
        self.channel_parameters[channel] = [int(freq), int(pulse_width), int(amplitude)]
        self.refresh_info()
        self.serial.write(f"{channel} {pulse_width} {freq} {amplitude}\n".encode("utf-8"))

    def refresh_info(self):
        for i in range(self.channel_parameters.shape[0]):
            if 0 in self.channel_parameters[i]:
                vars(self)[f'frequency_label_{i}'].setText(str(None))
                vars(self)[f'pulse_width_label_{i}'].setText(str(None))
                vars(self)[f'amplitude_label_{i}'].setText(str(None))
            else:
                vars(self)[f'frequency_label_{i}'].setText(str(self.channel_parameters[i, 0]))
                vars(self)[f'pulse_width_label_{i}'].setText(str(self.channel_parameters[i, 1]))
                vars(self)[f'amplitude_label_{i}'].setText(str(self.channel_parameters[i, 2]))
            pass



class Slider_UI(QtWidgets.QMainWindow, slider_ui.Ui_MainWindow):
    parameter_names = ["pulse_width", "frequency", "amplitude", "amplitude_falling"]
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.channel_parameters = np.zeros((8,4))
        self.is_active = [False, False, False, False, False, False, False, False]
        self.is_asymmetric = [False, False, False, False, False, False, False, False]

        try:
            self.serial = serial.Serial(port=arduino_port, baudrate=baudrate)
        except:
            print("FES system is not connected")
        self.setup()

    
    def setup(self):
        self.setWindowTitle("FES Parameters")
        # self.frequency_slider_0.valueChanged.connect(lambda val: vars(self)[f"frequency_value_0"].setText(str(val)))
        vars(self)[f"frequency_slider_0"].valueChanged.connect(lambda val: vars(self)[f"frequency_value_0"].setText(str(val)))
        # self.frequency_slider_0.sliderReleased.connect(lambda : self.slider_released("frequency", 0))
        print(self.frequency_slider_0.value().__class__)
        print(self.frequency_slider_0.sliderReleased)
        # self.tabWidget.setTabText
        style_sheet = """
QSlider {
    border: 2px solid #000000;
    border-radius: 0px;
    padding: 0px;
    background-color: #f5f5f5;
}
QSlider::groove:vertical {
    background: #2196F3;
    border-radius: 4px;
}
QSlider::sub-page:vertical {
    background: #DDD;
    height: 8px;
    border-radius: 4px;
}
QSlider::handle:vertical {
    background: black;
    width: 2px;          /* Thin vertical bar */
    height: 4px;        /* Height of the bar */
    margin: -2px 0;     /* Center vertically */
    border-radius: 0px;  /* Remove rounding */
}
QLabel{
    font-size:18pt;
}
QTabWidget{
    font-size:12pt;
    color: red;
}
QCheckBox{
    font-size:12pt;
}
QRadioButton{
    font-size:12pt;
}

"""
        self.setStyleSheet(style_sheet)
        # self.amplitude_slider_0.valueChanged[int].emit
        x = 0
        # Change elements in each tab
        for i in range(8):
            vars(self)[f"amplitude_falling_layout_{i}"].setDisabled(True)
            vars(self)[f"pulse_width_slider_{i}"].setRange(0,500)
            vars(self)[f"frequency_slider_{i}"].setRange(0,100)
            vars(self)[f"amplitude_falling_slider_{i}"].setRange(0,15)
            vars(self)[f"asymmetric_button_{i}"].setLayoutDirection(Qt.RightToLeft)
            vars(self)[f"active_button_{i}"].clicked.connect(lambda val, i=i: self.active_button_clicked(i, val))
            # vars(self)[f"amplitude_slider_{i}"].valueChanged.connect(lambda val, i=i: self.amplitude_slider_matching(i, val))
            vars(self)[f"asymmetric_button_{i}"].clicked.connect(lambda val, i=i: self.asymmetric_button_clicked(i, val))
        
        # self.active_button_0.

        
        
        for i in range(4):
            for j in range(8):
                vars(self)[f"{self.parameter_names[i]}_slider_{j}"].valueChanged.connect(lambda val, parameter=i, index=j: self.slider_dragging(parameter=parameter, i=index, val=val))
                vars(self)[f"{self.parameter_names[i]}_slider_{j}"].valueChanged[int].emit(0)
                vars(self)[f"{self.parameter_names[i]}_slider_{j}"].sliderReleased.connect(lambda i=i, j=j: self.slider_released(i, j))



        pass
    def slider_dragging(self, parameter:int, i:int, val):
        vars(self)[f"{self.parameter_names[parameter]}_value_{i}"].setText(f"{val} {['us', 'Hz', '',''][parameter]}")
        if parameter == 2 and not self.is_asymmetric[i]:
             vars(self)[f"amplitude_falling_slider_{i}"].setValue(val)

    def slider_released(self, parameter, i):
        print(parameter)
        self.channel_parameters[i][parameter] =  vars(self)[f'{self.parameter_names[parameter]}_slider_{i}'].value()
        if parameter == 2 and not self.is_asymmetric[i]:
            self.channel_parameters[i][3] = vars(self)[f'{self.parameter_names[parameter]}_slider_{i}'].value()
        self.send_data(i)

    def amplitude_slider_matching(self, channel, val):
        if not self.is_asymmetric[channel]:
            vars(self)[f"amplitude_falling_slider_{channel}"].setValue(val)

    def active_button_clicked(self, channel:int, status:bool):
        self.is_active[channel] = status
        self.send_data(channel)
        if status:
            pass
            # self.send_data(channel)

#             self.tabWidget.setStyleSheet(f"""
# QTabBar::tab:selected{{
#     background: {QColor(240,240,240).name()};
#     border: 1px solid #c4c4c4;
# }}
# """)
        else:
            pass
#             self.tabWidget.setStyleSheet(f"""
# QTabBar::tab:selected{{
#     background: gray;
#     border: 1px solid #c4c4c4;
# }}
# """)
        # self.is_active[channel] = self
        return
    
    def asymmetric_button_clicked(self, channel:int, status:bool):
        self.is_asymmetric[channel] = status
        if status:
            vars(self)[f"amplitude_falling_layout_{channel}"].setDisabled(not status)
        else:
            vars(self)[f"amplitude_falling_layout_{channel}"].setDisabled(not status)
        return

    def send_data(self, i):
        print(self.channel_parameters)
        try:
            
            if not self.is_active[i]:
                print("Channel Inactive")
                self.serial.write(f"{i} 0 0 0 0\n".encode("utf-8"))

                return
            if 0 in self.channel_parameters[i][0:3]:
                print("A Channel Parameter is set to 0. Cannot turn channel on")
                return
            print(f"{i} {str(np.int32(self.channel_parameters[i]))[1:-1]}\n")
            self.serial.write(f"{i} {str(np.int32(self.channel_parameters[i]))[1:-1]}\n".encode("utf-8"))
        except:
            print("Couldn't send the data")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Slider_UI()
    window.show()
    sys.exit(app.exec())
    