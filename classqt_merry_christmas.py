from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget

from mainwindow import Ui_Dialog
import sys
import cv2

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_red.clicked.connect(self.clicked_press_me_red)
        self.ui.pushButton_green.clicked.connect(self.clicked_press_me_green)
        self.ui.pic.mouseReleaseEvent = self.pic_clicked
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setValue(87)
        self.ui.horizontalSlider.setMaximum(250)
        self.ui.horizontalSlider.setMinimum(0)
        self.ui.horizontalSlider.valueChanged.connect(self.slider_change)
        self.ui.horizontalSlider.sliderReleased.connect(self.slider_release)
    
    def clicked_press_me_red(self):
        x = self.ui.lineEdit.text()
        message = QMessageBox()
        message.setWindowTitle("ho! ho! ho!")
        message.setInformativeText("        {}                ".format(x))
        message.exec_()
    
    def clicked_press_me_green(self):
        img = cv2.imread("pic/dai.jpg")
        cv2.imshow("hi~", img)
        cv2.waitKey(0)
    
    def pic_clicked(self, event):
        imessage = QMessageBox()
        imessage.setWindowTitle("ho! ho! ho!")
        imessage.setInformativeText("don't touch me       ")
        imessage.exec_()
        print(str(event.x()) + "," + str(event.y()))
        print(event.button())
    
    def slider_change(self):
        x = self.ui.horizontalSlider.value()
        self.ui.pic.setGeometry(QtCore.QRect(int(150-x/2), int(70-x/2), 100+x, 100+x))
    def slider_release(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #t = QTranslator()
    #t.load("chinese.qm")
    #app.installTranslator(t)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())