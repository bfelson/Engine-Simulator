# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EngineSimGUI.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1265, 958)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_32 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.bigframe = QFrame(self.centralwidget)
        self.bigframe.setObjectName(u"bigframe")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bigframe.sizePolicy().hasHeightForWidth())
        self.bigframe.setSizePolicy(sizePolicy1)
        self.bigframe.setMaximumSize(QSize(16777215, 16777215))
        self.bigframe.setAutoFillBackground(True)
        self.bigframe.setFrameShape(QFrame.NoFrame)
        self.bigframe.setFrameShadow(QFrame.Plain)
        self.bigframe.setLineWidth(0)
        self.verticalLayout_31 = QVBoxLayout(self.bigframe)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setSizeConstraint(QLayout.SetNoConstraint)
        self.enginesettings = QFrame(self.bigframe)
        self.enginesettings.setObjectName(u"enginesettings")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.enginesettings.sizePolicy().hasHeightForWidth())
        self.enginesettings.setSizePolicy(sizePolicy2)
        self.enginesettings.setFrameShape(QFrame.StyledPanel)
        self.enginesettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.enginesettings)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.enginesettingslabelframe = QFrame(self.enginesettings)
        self.enginesettingslabelframe.setObjectName(u"enginesettingslabelframe")
        self.enginesettingslabelframe.setFrameShape(QFrame.StyledPanel)
        self.enginesettingslabelframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.enginesettingslabelframe)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.enginesettingslable = QLabel(self.enginesettingslabelframe)
        self.enginesettingslable.setObjectName(u"enginesettingslable")
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(10)
        font.setBold(True)
        self.enginesettingslable.setFont(font)
        self.enginesettingslable.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.enginesettingslable, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.enginesettingslabelframe)

        self.engineprops = QFrame(self.enginesettings)
        self.engineprops.setObjectName(u"engineprops")
        sizePolicy2.setHeightForWidth(self.engineprops.sizePolicy().hasHeightForWidth())
        self.engineprops.setSizePolicy(sizePolicy2)
        self.engineprops.setFrameShape(QFrame.StyledPanel)
        self.engineprops.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.engineprops)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.boreframe = QFrame(self.engineprops)
        self.boreframe.setObjectName(u"boreframe")
        self.boreframe.setFrameShape(QFrame.StyledPanel)
        self.boreframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.boreframe)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.boresmallframe = QFrame(self.boreframe)
        self.boresmallframe.setObjectName(u"boresmallframe")
        self.boresmallframe.setFrameShape(QFrame.StyledPanel)
        self.boresmallframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.boresmallframe)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.borelabel = QLabel(self.boresmallframe)
        self.borelabel.setObjectName(u"borelabel")
        font1 = QFont()
        font1.setFamilies([u"Cambria"])
        font1.setPointSize(10)
        self.borelabel.setFont(font1)

        self.verticalLayout_10.addWidget(self.borelabel)

        self.boreedit = QLineEdit(self.boresmallframe)
        self.boreedit.setObjectName(u"boreedit")
        self.boreedit.setFont(font1)
        self.boreedit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.verticalLayout_10.addWidget(self.boreedit)


        self.verticalLayout.addWidget(self.boresmallframe)


        self.horizontalLayout_5.addWidget(self.boreframe)

        self.strokeframe = QFrame(self.engineprops)
        self.strokeframe.setObjectName(u"strokeframe")
        self.strokeframe.setFrameShape(QFrame.StyledPanel)
        self.strokeframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.strokeframe)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.strokesmallframe = QFrame(self.strokeframe)
        self.strokesmallframe.setObjectName(u"strokesmallframe")
        self.strokesmallframe.setFrameShape(QFrame.StyledPanel)
        self.strokesmallframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.strokesmallframe)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.strokelabel = QLabel(self.strokesmallframe)
        self.strokelabel.setObjectName(u"strokelabel")
        self.strokelabel.setFont(font1)

        self.verticalLayout_11.addWidget(self.strokelabel)

        self.strokeedit = QLineEdit(self.strokesmallframe)
        self.strokeedit.setObjectName(u"strokeedit")
        self.strokeedit.setFont(font1)
        self.strokeedit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.verticalLayout_11.addWidget(self.strokeedit)


        self.verticalLayout_2.addWidget(self.strokesmallframe)


        self.horizontalLayout_5.addWidget(self.strokeframe)

        self.cratioframe = QFrame(self.engineprops)
        self.cratioframe.setObjectName(u"cratioframe")
        sizePolicy2.setHeightForWidth(self.cratioframe.sizePolicy().hasHeightForWidth())
        self.cratioframe.setSizePolicy(sizePolicy2)
        self.cratioframe.setFrameShape(QFrame.StyledPanel)
        self.cratioframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.cratioframe)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.cratiosmallframe = QFrame(self.cratioframe)
        self.cratiosmallframe.setObjectName(u"cratiosmallframe")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(5)
        sizePolicy3.setHeightForWidth(self.cratiosmallframe.sizePolicy().hasHeightForWidth())
        self.cratiosmallframe.setSizePolicy(sizePolicy3)
        self.cratiosmallframe.setFrameShape(QFrame.StyledPanel)
        self.cratiosmallframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.cratiosmallframe)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.cratiolabel = QLabel(self.cratiosmallframe)
        self.cratiolabel.setObjectName(u"cratiolabel")
        self.cratiolabel.setFont(font1)

        self.verticalLayout_12.addWidget(self.cratiolabel)

        self.cratioedit = QLineEdit(self.cratiosmallframe)
        self.cratioedit.setObjectName(u"cratioedit")
        self.cratioedit.setFont(font1)
        self.cratioedit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.verticalLayout_12.addWidget(self.cratioedit)


        self.verticalLayout_3.addWidget(self.cratiosmallframe)


        self.horizontalLayout_5.addWidget(self.cratioframe)

        self.cylcountframe = QFrame(self.engineprops)
        self.cylcountframe.setObjectName(u"cylcountframe")
        self.cylcountframe.setFrameShape(QFrame.StyledPanel)
        self.cylcountframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.cylcountframe)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.cylcountsmallframe = QFrame(self.cylcountframe)
        self.cylcountsmallframe.setObjectName(u"cylcountsmallframe")
        self.cylcountsmallframe.setFrameShape(QFrame.StyledPanel)
        self.cylcountsmallframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.cylcountsmallframe)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.cylcountlabel = QLabel(self.cylcountsmallframe)
        self.cylcountlabel.setObjectName(u"cylcountlabel")
        self.cylcountlabel.setFont(font1)

        self.verticalLayout_13.addWidget(self.cylcountlabel)

        self.cylcountedit = QLineEdit(self.cylcountsmallframe)
        self.cylcountedit.setObjectName(u"cylcountedit")
        self.cylcountedit.setFont(font1)
        self.cylcountedit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.verticalLayout_13.addWidget(self.cylcountedit)


        self.verticalLayout_4.addWidget(self.cylcountsmallframe)


        self.horizontalLayout_5.addWidget(self.cylcountframe)


        self.verticalLayout_5.addWidget(self.engineprops)


        self.verticalLayout_31.addWidget(self.enginesettings)

        self.fuelsettingsframe = QFrame(self.bigframe)
        self.fuelsettingsframe.setObjectName(u"fuelsettingsframe")
        self.fuelsettingsframe.setFrameShape(QFrame.StyledPanel)
        self.fuelsettingsframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.fuelsettingsframe)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.fuelsettingslabelframe = QFrame(self.fuelsettingsframe)
        self.fuelsettingslabelframe.setObjectName(u"fuelsettingslabelframe")
        self.fuelsettingslabelframe.setFrameShape(QFrame.StyledPanel)
        self.fuelsettingslabelframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.fuelsettingslabelframe)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.fuelsettingslabel = QLabel(self.fuelsettingslabelframe)
        self.fuelsettingslabel.setObjectName(u"fuelsettingslabel")
        self.fuelsettingslabel.setFont(font)
        self.fuelsettingslabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.fuelsettingslabel)


        self.verticalLayout_9.addWidget(self.fuelsettingslabelframe)

        self.frame_20 = QFrame(self.fuelsettingsframe)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.fileselectframe = QFrame(self.frame_20)
        self.fileselectframe.setObjectName(u"fileselectframe")
        self.fileselectframe.setFrameShape(QFrame.StyledPanel)
        self.fileselectframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.fileselectframe)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.fuelfilelabel = QLabel(self.fileselectframe)
        self.fuelfilelabel.setObjectName(u"fuelfilelabel")
        self.fuelfilelabel.setFont(font1)

        self.verticalLayout_33.addWidget(self.fuelfilelabel)

        self.frame = QFrame(self.fileselectframe)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.filebrowsebutton = QToolButton(self.frame)
        self.filebrowsebutton.setObjectName(u"filebrowsebutton")
        self.filebrowsebutton.setFont(font1)

        self.verticalLayout_34.addWidget(self.filebrowsebutton)

        self.filebrowsefilename = QLineEdit(self.frame)
        self.filebrowsefilename.setObjectName(u"filebrowsefilename")
        self.filebrowsefilename.setFont(font1)

        self.verticalLayout_34.addWidget(self.filebrowsefilename)


        self.verticalLayout_33.addWidget(self.frame)


        self.horizontalLayout_7.addWidget(self.fileselectframe)

        self.rxnmechframe = QFrame(self.frame_20)
        self.rxnmechframe.setObjectName(u"rxnmechframe")
        self.rxnmechframe.setFrameShape(QFrame.StyledPanel)
        self.rxnmechframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.rxnmechframe)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, -1, -1)
        self.rxnmechlabel = QLabel(self.rxnmechframe)
        self.rxnmechlabel.setObjectName(u"rxnmechlabel")
        self.rxnmechlabel.setFont(font1)

        self.verticalLayout_6.addWidget(self.rxnmechlabel)

        self.rxnmechedit = QLineEdit(self.rxnmechframe)
        self.rxnmechedit.setObjectName(u"rxnmechedit")
        self.rxnmechedit.setFont(font1)

        self.verticalLayout_6.addWidget(self.rxnmechedit)


        self.horizontalLayout_7.addWidget(self.rxnmechframe)

        self.aircompframe = QFrame(self.frame_20)
        self.aircompframe.setObjectName(u"aircompframe")
        self.aircompframe.setFrameShape(QFrame.StyledPanel)
        self.aircompframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.aircompframe)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.aircomplabel = QLabel(self.aircompframe)
        self.aircomplabel.setObjectName(u"aircomplabel")
        self.aircomplabel.setFont(font1)

        self.verticalLayout_7.addWidget(self.aircomplabel)

        self.aircompedit = QLineEdit(self.aircompframe)
        self.aircompedit.setObjectName(u"aircompedit")
        self.aircompedit.setFont(font1)

        self.verticalLayout_7.addWidget(self.aircompedit)


        self.horizontalLayout_7.addWidget(self.aircompframe)

        self.fuelcompframe = QFrame(self.frame_20)
        self.fuelcompframe.setObjectName(u"fuelcompframe")
        self.fuelcompframe.setFrameShape(QFrame.StyledPanel)
        self.fuelcompframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.fuelcompframe)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.fuelcomplabel = QLabel(self.fuelcompframe)
        self.fuelcomplabel.setObjectName(u"fuelcomplabel")
        self.fuelcomplabel.setFont(font1)

        self.verticalLayout_8.addWidget(self.fuelcomplabel)

        self.fuelcompedit = QLineEdit(self.fuelcompframe)
        self.fuelcompedit.setObjectName(u"fuelcompedit")
        self.fuelcompedit.setFont(font1)

        self.verticalLayout_8.addWidget(self.fuelcompedit)


        self.horizontalLayout_7.addWidget(self.fuelcompframe)


        self.verticalLayout_9.addWidget(self.frame_20)


        self.verticalLayout_31.addWidget(self.fuelsettingsframe)

        self.fuelinjectorsettingsframe = QFrame(self.bigframe)
        self.fuelinjectorsettingsframe.setObjectName(u"fuelinjectorsettingsframe")
        self.fuelinjectorsettingsframe.setFrameShape(QFrame.StyledPanel)
        self.fuelinjectorsettingsframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.fuelinjectorsettingsframe)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.fuelinjectorsettingsframe)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_28)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_28)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_18, 0, 0, 1, 1)


        self.verticalLayout_21.addWidget(self.frame_28)

        self.injectorprops = QFrame(self.fuelinjectorsettingsframe)
        self.injectorprops.setObjectName(u"injectorprops")
        self.injectorprops.setFrameShape(QFrame.StyledPanel)
        self.injectorprops.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.injectorprops)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.topinjectorprops = QFrame(self.injectorprops)
        self.topinjectorprops.setObjectName(u"topinjectorprops")
        self.topinjectorprops.setFrameShape(QFrame.StyledPanel)
        self.topinjectorprops.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topinjectorprops)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.injectorpressureframe = QFrame(self.topinjectorprops)
        self.injectorpressureframe.setObjectName(u"injectorpressureframe")
        self.injectorpressureframe.setFrameShape(QFrame.StyledPanel)
        self.injectorpressureframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.injectorpressureframe)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.injectorpressurelabel = QLabel(self.injectorpressureframe)
        self.injectorpressurelabel.setObjectName(u"injectorpressurelabel")
        self.injectorpressurelabel.setFont(font1)

        self.verticalLayout_14.addWidget(self.injectorpressurelabel)

        self.injectorpressureedit = QLineEdit(self.injectorpressureframe)
        self.injectorpressureedit.setObjectName(u"injectorpressureedit")
        self.injectorpressureedit.setFont(font1)

        self.verticalLayout_14.addWidget(self.injectorpressureedit)


        self.horizontalLayout.addWidget(self.injectorpressureframe)

        self.injectortempframe = QFrame(self.topinjectorprops)
        self.injectortempframe.setObjectName(u"injectortempframe")
        self.injectortempframe.setFrameShape(QFrame.StyledPanel)
        self.injectortempframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.injectortempframe)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.injectortemplabel = QLabel(self.injectortempframe)
        self.injectortemplabel.setObjectName(u"injectortemplabel")
        self.injectortemplabel.setFont(font1)

        self.verticalLayout_15.addWidget(self.injectortemplabel)

        self.injectortempedit = QLineEdit(self.injectortempframe)
        self.injectortempedit.setObjectName(u"injectortempedit")
        self.injectortempedit.setFont(font1)

        self.verticalLayout_15.addWidget(self.injectortempedit)


        self.horizontalLayout.addWidget(self.injectortempframe)

        self.injectorfuelcompframe = QFrame(self.topinjectorprops)
        self.injectorfuelcompframe.setObjectName(u"injectorfuelcompframe")
        self.injectorfuelcompframe.setFrameShape(QFrame.StyledPanel)
        self.injectorfuelcompframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.injectorfuelcompframe)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.injectorfuelcomplabel = QLabel(self.injectorfuelcompframe)
        self.injectorfuelcomplabel.setObjectName(u"injectorfuelcomplabel")
        self.injectorfuelcomplabel.setFont(font1)

        self.verticalLayout_16.addWidget(self.injectorfuelcomplabel)

        self.injectorfuelcompedit = QLineEdit(self.injectorfuelcompframe)
        self.injectorfuelcompedit.setObjectName(u"injectorfuelcompedit")
        self.injectorfuelcompedit.setFont(font1)

        self.verticalLayout_16.addWidget(self.injectorfuelcompedit)


        self.horizontalLayout.addWidget(self.injectorfuelcompframe)


        self.verticalLayout_20.addWidget(self.topinjectorprops)

        self.buttominjectorprops = QFrame(self.injectorprops)
        self.buttominjectorprops.setObjectName(u"buttominjectorprops")
        self.buttominjectorprops.setFrameShape(QFrame.StyledPanel)
        self.buttominjectorprops.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.buttominjectorprops)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.opentiming = QFrame(self.buttominjectorprops)
        self.opentiming.setObjectName(u"opentiming")
        self.opentiming.setFrameShape(QFrame.StyledPanel)
        self.opentiming.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.opentiming)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.opentiminglabel = QLabel(self.opentiming)
        self.opentiminglabel.setObjectName(u"opentiminglabel")
        self.opentiminglabel.setFont(font1)

        self.verticalLayout_17.addWidget(self.opentiminglabel)

        self.opetimingedit = QLineEdit(self.opentiming)
        self.opetimingedit.setObjectName(u"opetimingedit")
        self.opetimingedit.setFont(font1)

        self.verticalLayout_17.addWidget(self.opetimingedit)


        self.horizontalLayout_2.addWidget(self.opentiming)

        self.closetiming = QFrame(self.buttominjectorprops)
        self.closetiming.setObjectName(u"closetiming")
        self.closetiming.setFrameShape(QFrame.StyledPanel)
        self.closetiming.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.closetiming)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.closetiminglabel = QLabel(self.closetiming)
        self.closetiminglabel.setObjectName(u"closetiminglabel")
        self.closetiminglabel.setFont(font1)

        self.verticalLayout_18.addWidget(self.closetiminglabel)

        self.closetimingedit = QLineEdit(self.closetiming)
        self.closetimingedit.setObjectName(u"closetimingedit")
        self.closetimingedit.setFont(font1)

        self.verticalLayout_18.addWidget(self.closetimingedit)


        self.horizontalLayout_2.addWidget(self.closetiming)

        self.fuelmass = QFrame(self.buttominjectorprops)
        self.fuelmass.setObjectName(u"fuelmass")
        self.fuelmass.setFrameShape(QFrame.StyledPanel)
        self.fuelmass.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.fuelmass)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.fuelmasslabel = QLabel(self.fuelmass)
        self.fuelmasslabel.setObjectName(u"fuelmasslabel")
        self.fuelmasslabel.setFont(font1)

        self.verticalLayout_19.addWidget(self.fuelmasslabel)

        self.fuelmassedit = QLineEdit(self.fuelmass)
        self.fuelmassedit.setObjectName(u"fuelmassedit")
        self.fuelmassedit.setFont(font1)

        self.verticalLayout_19.addWidget(self.fuelmassedit)


        self.horizontalLayout_2.addWidget(self.fuelmass)


        self.verticalLayout_20.addWidget(self.buttominjectorprops)


        self.verticalLayout_21.addWidget(self.injectorprops)


        self.verticalLayout_31.addWidget(self.fuelinjectorsettingsframe)

        self.turbosettingsframe = QFrame(self.bigframe)
        self.turbosettingsframe.setObjectName(u"turbosettingsframe")
        sizePolicy2.setHeightForWidth(self.turbosettingsframe.sizePolicy().hasHeightForWidth())
        self.turbosettingsframe.setSizePolicy(sizePolicy2)
        self.turbosettingsframe.setFrameShape(QFrame.StyledPanel)
        self.turbosettingsframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.turbosettingsframe)
        self.verticalLayout_22.setSpacing(5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.turbosettingslabelframe = QFrame(self.turbosettingsframe)
        self.turbosettingslabelframe.setObjectName(u"turbosettingslabelframe")
        self.turbosettingslabelframe.setFrameShape(QFrame.StyledPanel)
        self.turbosettingslabelframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.turbosettingslabelframe)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.turbosettingslabel = QLabel(self.turbosettingslabelframe)
        self.turbosettingslabel.setObjectName(u"turbosettingslabel")
        self.turbosettingslabel.setFont(font)
        self.turbosettingslabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.turbosettingslabel, 0, 0, 1, 1)


        self.verticalLayout_22.addWidget(self.turbosettingslabelframe)

        self.turbopropsframe = QFrame(self.turbosettingsframe)
        self.turbopropsframe.setObjectName(u"turbopropsframe")
        self.turbopropsframe.setFrameShape(QFrame.StyledPanel)
        self.turbopropsframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.turbopropsframe)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.turboinlettempframe = QFrame(self.turbopropsframe)
        self.turboinlettempframe.setObjectName(u"turboinlettempframe")
        self.turboinlettempframe.setFrameShape(QFrame.StyledPanel)
        self.turboinlettempframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.turboinlettempframe)
        self.verticalLayout_23.setSpacing(2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(5, 5, 5, 5)
        self.turboinletpressuresmallframe_2 = QFrame(self.turboinlettempframe)
        self.turboinletpressuresmallframe_2.setObjectName(u"turboinletpressuresmallframe_2")
        self.turboinletpressuresmallframe_2.setFrameShape(QFrame.StyledPanel)
        self.turboinletpressuresmallframe_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.turboinletpressuresmallframe_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.turboinletpressurelabel_2 = QLabel(self.turboinletpressuresmallframe_2)
        self.turboinletpressurelabel_2.setObjectName(u"turboinletpressurelabel_2")
        self.turboinletpressurelabel_2.setFont(font1)

        self.verticalLayout_24.addWidget(self.turboinletpressurelabel_2)

        self.turboinletpressureedit_2 = QLineEdit(self.turboinletpressuresmallframe_2)
        self.turboinletpressureedit_2.setObjectName(u"turboinletpressureedit_2")
        self.turboinletpressureedit_2.setFont(font1)

        self.verticalLayout_24.addWidget(self.turboinletpressureedit_2)


        self.verticalLayout_23.addWidget(self.turboinletpressuresmallframe_2)


        self.horizontalLayout_9.addWidget(self.turboinlettempframe)

        self.turboinletpressureframe = QFrame(self.turbopropsframe)
        self.turboinletpressureframe.setObjectName(u"turboinletpressureframe")
        self.turboinletpressureframe.setFrameShape(QFrame.StyledPanel)
        self.turboinletpressureframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.turboinletpressureframe)
        self.verticalLayout_25.setSpacing(2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(5, 5, 5, 5)
        self.turboinletpressuresmallframe = QFrame(self.turboinletpressureframe)
        self.turboinletpressuresmallframe.setObjectName(u"turboinletpressuresmallframe")
        self.turboinletpressuresmallframe.setFrameShape(QFrame.StyledPanel)
        self.turboinletpressuresmallframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.turboinletpressuresmallframe)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.turboinletpressurelabel = QLabel(self.turboinletpressuresmallframe)
        self.turboinletpressurelabel.setObjectName(u"turboinletpressurelabel")
        self.turboinletpressurelabel.setFont(font1)

        self.verticalLayout_26.addWidget(self.turboinletpressurelabel)

        self.turboinletpressureedit = QLineEdit(self.turboinletpressuresmallframe)
        self.turboinletpressureedit.setObjectName(u"turboinletpressureedit")
        self.turboinletpressureedit.setFont(font1)

        self.verticalLayout_26.addWidget(self.turboinletpressureedit)


        self.verticalLayout_25.addWidget(self.turboinletpressuresmallframe)


        self.horizontalLayout_9.addWidget(self.turboinletpressureframe)

        self.turbooutlettempframe = QFrame(self.turbopropsframe)
        self.turbooutlettempframe.setObjectName(u"turbooutlettempframe")
        self.turbooutlettempframe.setFrameShape(QFrame.StyledPanel)
        self.turbooutlettempframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.turbooutlettempframe)
        self.verticalLayout_27.setSpacing(2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(5, 5, 5, 5)
        self.turbooutlettempsmallframe = QFrame(self.turbooutlettempframe)
        self.turbooutlettempsmallframe.setObjectName(u"turbooutlettempsmallframe")
        self.turbooutlettempsmallframe.setFrameShape(QFrame.StyledPanel)
        self.turbooutlettempsmallframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.turbooutlettempsmallframe)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.turbooutlettemplabel = QLabel(self.turbooutlettempsmallframe)
        self.turbooutlettemplabel.setObjectName(u"turbooutlettemplabel")
        self.turbooutlettemplabel.setFont(font1)

        self.verticalLayout_28.addWidget(self.turbooutlettemplabel)

        self.turbooutlettempedit = QLineEdit(self.turbooutlettempsmallframe)
        self.turbooutlettempedit.setObjectName(u"turbooutlettempedit")
        self.turbooutlettempedit.setFont(font1)

        self.verticalLayout_28.addWidget(self.turbooutlettempedit)


        self.verticalLayout_27.addWidget(self.turbooutlettempsmallframe)


        self.horizontalLayout_9.addWidget(self.turbooutlettempframe)

        self.turbooutletpressureframe = QFrame(self.turbopropsframe)
        self.turbooutletpressureframe.setObjectName(u"turbooutletpressureframe")
        self.turbooutletpressureframe.setFrameShape(QFrame.StyledPanel)
        self.turbooutletpressureframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.turbooutletpressureframe)
        self.verticalLayout_29.setSpacing(2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(5, 5, 5, 5)
        self.turbooutletpressuresmallframe = QFrame(self.turbooutletpressureframe)
        self.turbooutletpressuresmallframe.setObjectName(u"turbooutletpressuresmallframe")
        self.turbooutletpressuresmallframe.setFrameShape(QFrame.StyledPanel)
        self.turbooutletpressuresmallframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.turbooutletpressuresmallframe)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.turbooutletpressurelabel = QLabel(self.turbooutletpressuresmallframe)
        self.turbooutletpressurelabel.setObjectName(u"turbooutletpressurelabel")
        self.turbooutletpressurelabel.setFont(font1)

        self.verticalLayout_30.addWidget(self.turbooutletpressurelabel)

        self.turbooutletedit = QLineEdit(self.turbooutletpressuresmallframe)
        self.turbooutletedit.setObjectName(u"turbooutletedit")
        self.turbooutletedit.setFont(font1)

        self.verticalLayout_30.addWidget(self.turbooutletedit)


        self.verticalLayout_29.addWidget(self.turbooutletpressuresmallframe)


        self.horizontalLayout_9.addWidget(self.turbooutletpressureframe)


        self.verticalLayout_22.addWidget(self.turbopropsframe)


        self.verticalLayout_31.addWidget(self.turbosettingsframe)

        self.buttonsframe = QFrame(self.bigframe)
        self.buttonsframe.setObjectName(u"buttonsframe")
        self.buttonsframe.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.buttonsframe.sizePolicy().hasHeightForWidth())
        self.buttonsframe.setSizePolicy(sizePolicy2)
        self.buttonsframe.setFrameShape(QFrame.StyledPanel)
        self.buttonsframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.buttonsframe)
        self.horizontalLayout_3.setSpacing(25)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.checkvalues = QPushButton(self.buttonsframe)
        self.checkvalues.setObjectName(u"checkvalues")
        font2 = QFont()
        font2.setFamilies([u"Cambria"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setKerning(True)
        self.checkvalues.setFont(font2)

        self.horizontalLayout_3.addWidget(self.checkvalues)

        self.runsim = QPushButton(self.buttonsframe)
        self.runsim.setObjectName(u"runsim")
        self.runsim.setFont(font2)

        self.horizontalLayout_3.addWidget(self.runsim)

        self.plotsomething = QPushButton(self.buttonsframe)
        self.plotsomething.setObjectName(u"plotsomething")
        self.plotsomething.setFont(font2)

        self.horizontalLayout_3.addWidget(self.plotsomething)

        self.generatedPlots = QPushButton(self.buttonsframe)
        self.generatedPlots.setObjectName(u"generatedPlots")
        self.generatedPlots.setFont(font2)

        self.horizontalLayout_3.addWidget(self.generatedPlots)

        self.createstudy = QPushButton(self.buttonsframe)
        self.createstudy.setObjectName(u"createstudy")
        self.createstudy.setFont(font2)

        self.horizontalLayout_3.addWidget(self.createstudy)


        self.verticalLayout_31.addWidget(self.buttonsframe)


        self.verticalLayout_32.addWidget(self.bigframe)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QRect(0, 0, 1265, 31))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.checkvalues.clicked.connect(MainWindow.submitValues)
        self.runsim.clicked.connect(MainWindow.startSimulation)
        self.plotsomething.clicked.connect(MainWindow.plotValues)
        self.generatedPlots.clicked.connect(MainWindow.pregeneratedPlots)
        self.createstudy.clicked.connect(MainWindow.newStudy)
        self.filebrowsebutton.clicked.connect(MainWindow.selectFile)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Engine Simulator", None))
        self.enginesettingslable.setText(QCoreApplication.translate("MainWindow", u"Engine Settings", None))
        self.borelabel.setText(QCoreApplication.translate("MainWindow", u"Bore Diameter (m)", None))
        self.boreedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.083", None))
        self.strokelabel.setText(QCoreApplication.translate("MainWindow", u"Stroke Length (m)", None))
        self.strokeedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.006", None))
        self.cratiolabel.setText(QCoreApplication.translate("MainWindow", u"Compression Ratio", None))
        self.cratioedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"50", None))
        self.cylcountlabel.setText(QCoreApplication.translate("MainWindow", u"Cylinder Count", None))
        self.cylcountedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"4", None))
        self.fuelsettingslabel.setText(QCoreApplication.translate("MainWindow", u"Fuel Settings", None))
        self.fuelfilelabel.setText(QCoreApplication.translate("MainWindow", u"Fuel Type:", None))
        self.filebrowsebutton.setText(QCoreApplication.translate("MainWindow", u"Browse Files (*.yaml)", None))
        self.rxnmechlabel.setText(QCoreApplication.translate("MainWindow", u"Reaction Mechanism", None))
        self.rxnmechedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"nDodecane_IG", None))
        self.aircomplabel.setText(QCoreApplication.translate("MainWindow", u"Air Composition", None))
        self.aircompedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"o2:1, n2:3.76", None))
        self.fuelcomplabel.setText(QCoreApplication.translate("MainWindow", u"Fuel Composition", None))
        self.fuelcompedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"c12h26:1", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Fuel Injector Settings", None))
        self.injectorpressurelabel.setText(QCoreApplication.translate("MainWindow", u"Pressure (Pa)", None))
        self.injectorpressureedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1600e5", None))
        self.injectortemplabel.setText(QCoreApplication.translate("MainWindow", u"Temperature (K)", None))
        self.injectortempedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"600", None))
        self.injectorfuelcomplabel.setText(QCoreApplication.translate("MainWindow", u"Fuel Composition (can be same as prev)", None))
        self.injectorfuelcompedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"c12h26:1", None))
        self.opentiminglabel.setText(QCoreApplication.translate("MainWindow", u"Open Timing (deg 0-360)", None))
        self.opetimingedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"350", None))
        self.closetiminglabel.setText(QCoreApplication.translate("MainWindow", u"Close Timing (deg 0-360)", None))
        self.closetimingedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"365", None))
        self.fuelmasslabel.setText(QCoreApplication.translate("MainWindow", u"Mass of fuel passing (kg)", None))
        self.fuelmassedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"3.2e-5", None))
        self.turbosettingslabel.setText(QCoreApplication.translate("MainWindow", u"Turbocharger Settings", None))
        self.turboinletpressurelabel_2.setText(QCoreApplication.translate("MainWindow", u"Inlet Temperature (K)", None))
        self.turboinletpressureedit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"600", None))
        self.turboinletpressurelabel.setText(QCoreApplication.translate("MainWindow", u"Inlet Pressure (Pa)", None))
        self.turboinletpressureedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1.3e5", None))
        self.turbooutlettemplabel.setText(QCoreApplication.translate("MainWindow", u"Outlet Pressure (Pa)", None))
        self.turbooutlettempedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1.2e5", None))
        self.turbooutletpressurelabel.setText(QCoreApplication.translate("MainWindow", u"Inlet Composition (air)", None))
        self.turbooutletedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"o2:1, n2:3.76", None))
        self.checkvalues.setText(QCoreApplication.translate("MainWindow", u"Submit Values", None))
        self.runsim.setText(QCoreApplication.translate("MainWindow", u"Start Simulation", None))
        self.plotsomething.setText(QCoreApplication.translate("MainWindow", u"Plot Values", None))
        self.generatedPlots.setText(QCoreApplication.translate("MainWindow", u"Pre-Generated Plots", None))
        self.createstudy.setText(QCoreApplication.translate("MainWindow", u"Create a New Study", None))
    # retranslateUi

