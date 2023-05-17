# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewStudy.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_newStudy(object):
    def setupUi(self, newStudy):
        if not newStudy.objectName():
            newStudy.setObjectName(u"newStudy")
        newStudy.resize(553, 340)
        self.bigFrame = QFrame(newStudy)
        self.bigFrame.setObjectName(u"bigFrame")
        self.bigFrame.setGeometry(QRect(13, 13, 527, 314))
        self.bigFrame.setFrameShape(QFrame.StyledPanel)
        self.bigFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.bigFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.propertyvaryframe = QFrame(self.bigFrame)
        self.propertyvaryframe.setObjectName(u"propertyvaryframe")
        self.propertyvaryframe.setFrameShape(QFrame.StyledPanel)
        self.propertyvaryframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.propertyvaryframe)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.propertyvaryframe)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(10)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.propertyToVary = QComboBox(self.propertyvaryframe)
        self.propertyToVary.addItem("")
        self.propertyToVary.setObjectName(u"propertyToVary")
        self.propertyToVary.setFont(font)

        self.verticalLayout.addWidget(self.propertyToVary)


        self.verticalLayout_6.addWidget(self.propertyvaryframe)

        self.minmaxstepframe = QFrame(self.bigFrame)
        self.minmaxstepframe.setObjectName(u"minmaxstepframe")
        self.minmaxstepframe.setFrameShape(QFrame.StyledPanel)
        self.minmaxstepframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.minmaxstepframe)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.minframe = QFrame(self.minmaxstepframe)
        self.minframe.setObjectName(u"minframe")
        self.minframe.setFrameShape(QFrame.StyledPanel)
        self.minframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.minframe)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.minlabel = QLabel(self.minframe)
        self.minlabel.setObjectName(u"minlabel")
        self.minlabel.setFont(font)

        self.verticalLayout_2.addWidget(self.minlabel)

        self.minedit = QLineEdit(self.minframe)
        self.minedit.setObjectName(u"minedit")
        self.minedit.setFont(font)

        self.verticalLayout_2.addWidget(self.minedit)


        self.horizontalLayout.addWidget(self.minframe)

        self.maxframe = QFrame(self.minmaxstepframe)
        self.maxframe.setObjectName(u"maxframe")
        self.maxframe.setFrameShape(QFrame.StyledPanel)
        self.maxframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.maxframe)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.maxlable = QLabel(self.maxframe)
        self.maxlable.setObjectName(u"maxlable")
        self.maxlable.setFont(font)

        self.verticalLayout_3.addWidget(self.maxlable)

        self.maxedit = QLineEdit(self.maxframe)
        self.maxedit.setObjectName(u"maxedit")
        self.maxedit.setFont(font)

        self.verticalLayout_3.addWidget(self.maxedit)


        self.horizontalLayout.addWidget(self.maxframe)

        self.stepframe = QFrame(self.minmaxstepframe)
        self.stepframe.setObjectName(u"stepframe")
        self.stepframe.setFrameShape(QFrame.StyledPanel)
        self.stepframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.stepframe)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.steplabel = QLabel(self.stepframe)
        self.steplabel.setObjectName(u"steplabel")
        self.steplabel.setFont(font)

        self.verticalLayout_4.addWidget(self.steplabel)

        self.stepedit = QLineEdit(self.stepframe)
        self.stepedit.setObjectName(u"stepedit")
        self.stepedit.setFont(font)

        self.verticalLayout_4.addWidget(self.stepedit)


        self.horizontalLayout.addWidget(self.stepframe)


        self.verticalLayout_6.addWidget(self.minmaxstepframe)

        self.runstudyframe = QFrame(self.bigFrame)
        self.runstudyframe.setObjectName(u"runstudyframe")
        self.runstudyframe.setFrameShape(QFrame.StyledPanel)
        self.runstudyframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.runstudyframe)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.runstudybutton = QPushButton(self.runstudyframe)
        self.runstudybutton.setObjectName(u"runstudybutton")
        self.runstudybutton.setFont(font)

        self.horizontalLayout_2.addWidget(self.runstudybutton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addWidget(self.runstudyframe)


        self.retranslateUi(newStudy)
        self.runstudybutton.clicked.connect(newStudy.runStudy)

        QMetaObject.connectSlotsByName(newStudy)
    # setupUi

    def retranslateUi(self, newStudy):
        newStudy.setWindowTitle(QCoreApplication.translate("newStudy", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("newStudy", u"What property would you like to vary?", None))
        self.propertyToVary.setItemText(0, QCoreApplication.translate("newStudy", u"Compression Ratio", None))

        self.minlabel.setText(QCoreApplication.translate("newStudy", u"Minimum", None))
        self.maxlable.setText(QCoreApplication.translate("newStudy", u"Maximum", None))
        self.steplabel.setText(QCoreApplication.translate("newStudy", u"Step", None))
        self.runstudybutton.setText(QCoreApplication.translate("newStudy", u"Run Study", None))
    # retranslateUi

