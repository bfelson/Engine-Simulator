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

class Canvas(FigureCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots()
        super().__init__(fig)
        self.setParent(parent)

    def plot(self, x, y, xlabel, ylabel, title):
        self.ax.plot(x, y)
        self.set_xlabel(xlabel)
        self.set_ylabel(ylabel)
        self.title(title)

class matplotlibWidget(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.canvas = Canvas(self)
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        self.setLayout(vertical_layout)

        self.main = None

    def plot_ca_pressure(self):
        self.canvas.plot(
            self.main.simulator.t,
            self.main.simulator.states.P,
            r'$\phi$ (rad)',
            '$T$ (K)',
            'Pressure vs. Crank Angle'
        )