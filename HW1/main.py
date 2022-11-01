from PyQt5 import QtWidgets
from myDesign import Ui_MainWindow
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5.QtGui import *


class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.ui.showGraphic.clicked.connect(self.make_graphic)
        self.ui.pushButton_happy.clicked.connect(
            lambda: self.ui.lblPicture.setPixmap(QPixmap("happy.png")))
        self.ui.pushButton_angry.clicked.connect(
            lambda: self.ui.lblPicture.setPixmap(QPixmap("angry.png")))
        self.ui.pushButton_sad.clicked.connect(
            lambda: self.ui.lblPicture.setPixmap(QPixmap("sad.png")))
        self.ui.btnShowData.setToolTip("Кузин Никита Сергеевич\nПрограммная инженерия\nИУК4-32Б")
        self.ui.btnShowData.clicked.connect(lambda: self.ui.txtBrowserInfo.setText('Данные просмотрены!'))

    def make_graphic(self):
        fig = Figure(figsize=(9, 4))
        can = FigureCanvasQTAgg(fig)
        layout = QtWidgets.QVBoxLayout(self.ui.widget)
        layout.addWidget(can)
        ax = can.figure.add_subplot(111)
        ax.cla()
        x = np.arange(-2.5, 2.51, 0.25)
        ax.plot(x, (np.cos(x)) * (np.cos(x)) * (np.tan(2 * x)) - (1 / (4 * x)))
        ax.grid(True)
        can.figure.tight_layout()
        can.draw()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Application()
    application.show()
    app.exec_()
