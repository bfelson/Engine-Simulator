# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PregenPlotsWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_PregenPlotsWindow(object):
    def setupUi(self, PregenPlotsWindow):
        if not PregenPlotsWindow.objectName():
            PregenPlotsWindow.setObjectName(u"PregenPlotsWindow")
        PregenPlotsWindow.resize(559, 618)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PregenPlotsWindow.sizePolicy().hasHeightForWidth())
        PregenPlotsWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(PregenPlotsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setFamilies([u"Cambria"])
        font1.setPointSize(9)
        self.pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_9)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.svalueoutput = QLabel(self.centralwidget)
        self.svalueoutput.setObjectName(u"svalueoutput")
        font2 = QFont()
        font2.setFamilies([u"Cambria"])
        font2.setPointSize(16)
        self.svalueoutput.setFont(font2)

        self.verticalLayout_2.addWidget(self.svalueoutput)

        PregenPlotsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PregenPlotsWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 559, 31))
        PregenPlotsWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PregenPlotsWindow)
        self.statusbar.setObjectName(u"statusbar")
        PregenPlotsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PregenPlotsWindow)
        self.pushButton.clicked.connect(PregenPlotsWindow.plot_ca_pressure)
        self.pushButton_2.clicked.connect(PregenPlotsWindow.plot_ca_temp)
        self.pushButton_3.clicked.connect(PregenPlotsWindow.plot_pv_diagram)
        self.pushButton_4.clicked.connect(PregenPlotsWindow.plot_ts_diagram)
        self.pushButton_5.clicked.connect(PregenPlotsWindow.plot_QW)
        self.pushButton_6.clicked.connect(PregenPlotsWindow.plot_gas_composition)
        self.pushButton_7.clicked.connect(PregenPlotsWindow.heat_release)
        self.pushButton_8.clicked.connect(PregenPlotsWindow.expansion_power)
        self.pushButton_9.clicked.connect(PregenPlotsWindow.efficiency)

        QMetaObject.connectSlotsByName(PregenPlotsWindow)
    # setupUi

    def retranslateUi(self, PregenPlotsWindow):
        PregenPlotsWindow.setWindowTitle(QCoreApplication.translate("PregenPlotsWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("PregenPlotsWindow", u"Pregenerated Plotting Functions", None))
        self.pushButton.setText(QCoreApplication.translate("PregenPlotsWindow", u"Pressure vs. Time", None))
        self.pushButton_2.setText(QCoreApplication.translate("PregenPlotsWindow", u"Temperature vs. Time", None))
        self.pushButton_3.setText(QCoreApplication.translate("PregenPlotsWindow", u"P-V Diagram", None))
        self.pushButton_4.setText(QCoreApplication.translate("PregenPlotsWindow", u"T-S Diagram", None))
        self.pushButton_5.setText(QCoreApplication.translate("PregenPlotsWindow", u"Heat of Reaction and Expansion Work", None))
        self.pushButton_6.setText(QCoreApplication.translate("PregenPlotsWindow", u"Gas Composition", None))
        self.pushButton_7.setText(QCoreApplication.translate("PregenPlotsWindow", u"Heat Release", None))
        self.pushButton_8.setText(QCoreApplication.translate("PregenPlotsWindow", u"Expansion Power", None))
        self.pushButton_9.setText(QCoreApplication.translate("PregenPlotsWindow", u"Efficiency", None))
        self.svalueoutput.setText(QCoreApplication.translate("PregenPlotsWindow", u"Space for Single Value Outputs", None))
    # retranslateUi

