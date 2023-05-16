from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QToolButton, QVBoxLayout, QWidget)

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# class Canvas(FigureCanvas):
#     def __init__(self, parent):
#         self.fig, self.ax = plt.subplots()
#         super().__init__(self.fig)
#         self.setParent(parent)

#     def plot(self, x, y, xlabel, ylabel, title):
#         self.ax.plot(x, y)
#         self.ax.set_xlabel(xlabel)
#         self.ax.set_ylabel(ylabel)
#         self.ax.set_title(title)
#         self.show()

class matplotlibWidget(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        # self.canvas = Canvas(self)

    def plot_ca_pressure(self):
        fig, ax = plt.subplots()
        ax.plot(self.main.simulator.states.t, self.main.simulator.states.P)
        ax.set_xlabel(r'$\phi$ (deg)')
        ax.set_ylabel("Pressure (Pa)")
        plt.show()