# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(430, 382)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(84, 84, 84);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tb_in = QLineEdit(self.centralwidget)
        self.tb_in.setObjectName(u"tb_in")
        self.tb_in.setGeometry(QRect(30, 200, 161, 41))
        self.tb_in.setStyleSheet(u"background-color: rgb(185, 185, 185);\n"
"color: rgb(0, 0, 0);")
        self.tb_out = QLineEdit(self.centralwidget)
        self.tb_out.setObjectName(u"tb_out")
        self.tb_out.setGeometry(QRect(250, 200, 161, 41))
        self.tb_out.setStyleSheet(u"background-color: rgb(185, 185, 185);\n"
"color: rgb(0, 0, 0);")
        self.label_from = QLabel(self.centralwidget)
        self.label_from.setObjectName(u"label_from")
        self.label_from.setGeometry(QRect(30, 90, 91, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.label_from.setFont(font)
        self.lable_to = QLabel(self.centralwidget)
        self.lable_to.setObjectName(u"lable_to")
        self.lable_to.setGeometry(QRect(250, 90, 91, 31))
        self.lable_to.setFont(font)
        self.combo_from = QComboBox(self.centralwidget)
        self.combo_from.setObjectName(u"combo_from")
        self.combo_from.setGeometry(QRect(30, 140, 161, 31))
        self.combo_from.setStyleSheet(u"background-color: rgb(185, 185, 185);\n"
"color: rgb(0, 0, 0);")
        self.combo_to = QComboBox(self.centralwidget)
        self.combo_to.setObjectName(u"combo_to")
        self.combo_to.setGeometry(QRect(250, 140, 161, 31))
        self.combo_to.setStyleSheet(u"background-color: rgb(185, 185, 185);\n"
"color: rgb(0, 0, 0);")
        self.combo_change = QComboBox(self.centralwidget)
        self.combo_change.setObjectName(u"combo_change")
        self.combo_change.setGeometry(QRect(30, 10, 391, 41))
        self.combo_change.setStyleSheet(u"color: rgb(84, 84, 84);\n"
"background-color: rgb(255, 255, 255);")
        self.btn_convert = QPushButton(self.centralwidget)
        self.btn_convert.setObjectName(u"btn_convert")
        self.btn_convert.setGeometry(QRect(150, 270, 141, 41))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(True)
        self.btn_convert.setFont(font1)
        self.btn_convert.setStyleSheet(u"color: rgb(185, 185, 185);\n"
"background-color: rgb(0, 0, 0);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 430, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_from.setText(QCoreApplication.translate("MainWindow", u"from :", None))
        self.lable_to.setText(QCoreApplication.translate("MainWindow", u"to :", None))
        self.btn_convert.setText(QCoreApplication.translate("MainWindow", u"convert", None))
    # retranslateUi

