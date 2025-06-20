# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Mainwindow(object):
    def setupUi(self, Mainwindow):
        if not Mainwindow.objectName():
            Mainwindow.setObjectName(u"Mainwindow")
        Mainwindow.resize(1920, 1200)
        Mainwindow.setStyleSheet(u"QWidget{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(222, 243, 102, 255), stop:1 rgba(48, 189, 105, 255))\n"
"}\n"
"QMessageBox{\n"
"background: #000000;\n"
"color: #FFFFFF;\n"
"}\n"
"QMessageBox QLabel {\n"
"background: #000000;\n"
"color: #FFFFFF;\n"
"}\n"
"QMessageBox QPushButton {\n"
"background: #000000;\n"
"color: #FFFFFF;\n"
"}")
        self.white_box = QWidget(Mainwindow)
        self.white_box.setObjectName(u"white_box")
        self.white_box.setGeometry(QRect(345, 170, 1230, 800))
        self.white_box.setStyleSheet(u"background: #FFFFFF;\n"
"border-radius: 12px;\n"
"")
        self.member_login_label = QLabel(self.white_box)
        self.member_login_label.setObjectName(u"member_login_label")
        self.member_login_label.setGeometry(QRect(580, 80, 491, 91))
        font = QFont()
        font.setFamilies([u"MathJax_Main"])
        font.setPointSize(58)
        self.member_login_label.setFont(font)
        self.member_login_label.setStyleSheet(u"color: #000000;")
        self.email_field = QLineEdit(self.white_box)
        self.email_field.setObjectName(u"email_field")
        self.email_field.setGeometry(QRect(500, 235, 661, 104))
        font1 = QFont()
        font1.setFamilies([u"MathJax_Main"])
        font1.setPointSize(24)
        self.email_field.setFont(font1)
        self.email_field.setAutoFillBackground(False)
        self.email_field.setStyleSheet(u"background: #D9D9D9;\n"
"color: #000000;\n"
"border-radius: 50%;\n"
"padding-left: 100px;\n"
"padding-right: 15px;")
        self.email_field.setClearButtonEnabled(False)
        self.password_field = QLineEdit(self.white_box)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setGeometry(QRect(500, 385, 661, 104))
        self.password_field.setFont(font1)
        self.password_field.setAutoFillBackground(False)
        self.password_field.setStyleSheet(u"background: #D9D9D9;\n"
"color: #000000;\n"
"border-radius: 50%;\n"
"padding-left: 100px;\n"
"padding-right: 100px;")
        self.password_field.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_field.setClearButtonEnabled(False)
        self.login_button = QPushButton(self.white_box)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(500, 640, 661, 104))
        self.login_button.setFont(font1)
        self.login_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_button.setStyleSheet(u"QPushButton \n"
"{\n"
"        background-color: #2BCC6C; \n"
"        color: #FFFFFF;\n"
"        border-radius: 50%;\n"
" }\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #279A51;\n"
"}\n"
"")
        self.login_button.setCheckable(False)
        self.login_button.setChecked(False)
        self.login_button.setAutoExclusive(False)
        self.login_button.setAutoDefault(False)
        self.login_button.setFlat(False)
        self.email_icon = QLabel(self.white_box)
        self.email_icon.setObjectName(u"email_icon")
        self.email_icon.setGeometry(QRect(520, 255, 70, 65))
        self.email_icon.setStyleSheet(u"background: #D9D9D9;")
        self.email_icon.setPixmap(QPixmap(u"icons/email.png"))
        self.email_icon.setScaledContents(True)
        self.password_icon = QLabel(self.white_box)
        self.password_icon.setObjectName(u"password_icon")
        self.password_icon.setGeometry(QRect(520, 400, 70, 65))
        self.password_icon.setStyleSheet(u"background: #D9D9D9;")
        self.password_icon.setPixmap(QPixmap(u"icons/password.png"))
        self.password_icon.setScaledContents(True)
        self.login_icon = QLabel(self.white_box)
        self.login_icon.setObjectName(u"login_icon")
        self.login_icon.setGeometry(QRect(90, 240, 316, 289))
        self.login_icon.setPixmap(QPixmap(u"icons/login.png"))
        self.login_icon.setScaledContents(True)
        self.hide_show_button = QPushButton(self.white_box)
        self.hide_show_button.setObjectName(u"hide_show_button")
        self.hide_show_button.setGeometry(QRect(1070, 410, 61, 51))
        self.hide_show_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.hide_show_button.setStyleSheet(u"QPushButton{\n"
"background: #D9D9D9;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #C0C0C0;\n"
"}")
        self.hide_show_button.setIconSize(QSize(55, 55))
        self.hide_show_button.setCheckable(True)
        self.Dont_have_an_account_label = QLabel(self.white_box)
        self.Dont_have_an_account_label.setObjectName(u"Dont_have_an_account_label")
        self.Dont_have_an_account_label.setGeometry(QRect(520, 580, 291, 31))
        font2 = QFont()
        font2.setFamilies([u"MathJax_Main"])
        font2.setPointSize(20)
        self.Dont_have_an_account_label.setFont(font2)
        self.Dont_have_an_account_label.setStyleSheet(u"color: #666666;")
        self.forget_password_button = QPushButton(self.white_box)
        self.forget_password_button.setObjectName(u"forget_password_button")
        self.forget_password_button.setGeometry(QRect(520, 520, 231, 31))
        font3 = QFont()
        font3.setFamilies([u"MathJax_Main"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.forget_password_button.setFont(font3)
        self.forget_password_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.forget_password_button.setStyleSheet(u"color: #2980B9;")
        self.sign_up_button = QPushButton(self.white_box)
        self.sign_up_button.setObjectName(u"sign_up_button")
        self.sign_up_button.setGeometry(QRect(810, 580, 111, 31))
        self.sign_up_button.setFont(font3)
        self.sign_up_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sign_up_button.setStyleSheet(u"color: #000000;\n"
"")
        self.skip = QPushButton(self.white_box)
        self.skip.setObjectName(u"skip")
        self.skip.setGeometry(QRect(790, 760, 80, 23))
        self.skip.setStyleSheet(u"background: #000000;")

        self.retranslateUi(Mainwindow)

        self.login_button.setDefault(False)


        QMetaObject.connectSlotsByName(Mainwindow)
    # setupUi

    def retranslateUi(self, Mainwindow):
        Mainwindow.setWindowTitle(QCoreApplication.translate("Mainwindow", u"Mainwindow", None))
        self.member_login_label.setText(QCoreApplication.translate("Mainwindow", u"Member Login", None))
        self.email_field.setInputMask("")
        self.email_field.setText("")
        self.email_field.setPlaceholderText(QCoreApplication.translate("Mainwindow", u"Email", None))
        self.password_field.setInputMask("")
        self.password_field.setText("")
        self.password_field.setPlaceholderText(QCoreApplication.translate("Mainwindow", u"Password", None))
        self.login_button.setText(QCoreApplication.translate("Mainwindow", u"Login", None))
        self.email_icon.setText("")
        self.password_icon.setText("")
        self.login_icon.setText("")
        self.hide_show_button.setText("")
        self.Dont_have_an_account_label.setText(QCoreApplication.translate("Mainwindow", u"Don't have an account?", None))
        self.forget_password_button.setText(QCoreApplication.translate("Mainwindow", u"Forget Password", None))
        self.sign_up_button.setText(QCoreApplication.translate("Mainwindow", u"Sign up", None))
        self.skip.setText(QCoreApplication.translate("Mainwindow", u"skip", None))
    # retranslateUi

