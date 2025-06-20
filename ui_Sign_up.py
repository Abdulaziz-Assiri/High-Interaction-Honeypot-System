# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sign_up.ui'
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

class Ui_Sign_Up(object):
    def setupUi(self, Sign_Up):
        if not Sign_Up.objectName():
            Sign_Up.setObjectName(u"Sign_Up")
        Sign_Up.resize(1920, 1200)
        Sign_Up.setStyleSheet(u"QWidget{\n"
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
        self.sign_up_white_box = QWidget(Sign_Up)
        self.sign_up_white_box.setObjectName(u"sign_up_white_box")
        self.sign_up_white_box.setGeometry(QRect(330, 160, 1230, 721))
        self.sign_up_white_box.setStyleSheet(u"background: #FFFFFF;\n"
"border-radius: 12px;\n"
"")
        self.member_sign_up_label = QLabel(self.sign_up_white_box)
        self.member_sign_up_label.setObjectName(u"member_sign_up_label")
        self.member_sign_up_label.setGeometry(QRect(560, 70, 551, 91))
        font = QFont()
        font.setFamilies([u"MathJax_Main"])
        font.setPointSize(58)
        self.member_sign_up_label.setFont(font)
        self.member_sign_up_label.setStyleSheet(u"color: #000000;")
        self.sign_up_email_field = QLineEdit(self.sign_up_white_box)
        self.sign_up_email_field.setObjectName(u"sign_up_email_field")
        self.sign_up_email_field.setGeometry(QRect(500, 235, 661, 104))
        font1 = QFont()
        font1.setFamilies([u"MathJax_Main"])
        font1.setPointSize(24)
        self.sign_up_email_field.setFont(font1)
        self.sign_up_email_field.setAutoFillBackground(False)
        self.sign_up_email_field.setStyleSheet(u"background: #D9D9D9;\n"
"color: #000000;\n"
"border-radius: 50%;\n"
"padding-left: 100px;\n"
"padding-right: 15px;")
        self.sign_up_email_field.setClearButtonEnabled(False)
        self.sign_up_password_field = QLineEdit(self.sign_up_white_box)
        self.sign_up_password_field.setObjectName(u"sign_up_password_field")
        self.sign_up_password_field.setGeometry(QRect(500, 385, 661, 104))
        self.sign_up_password_field.setFont(font1)
        self.sign_up_password_field.setAutoFillBackground(False)
        self.sign_up_password_field.setStyleSheet(u"background: #D9D9D9;\n"
"color: #000000;\n"
"border-radius: 50%;\n"
"padding-left: 100px;\n"
"padding-right: 100px;")
        self.sign_up_password_field.setEchoMode(QLineEdit.EchoMode.Password)
        self.sign_up_password_field.setClearButtonEnabled(False)
        self.sign_up_button = QPushButton(self.sign_up_white_box)
        self.sign_up_button.setObjectName(u"sign_up_button")
        self.sign_up_button.setGeometry(QRect(500, 550, 661, 104))
        self.sign_up_button.setFont(font1)
        self.sign_up_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sign_up_button.setStyleSheet(u"QPushButton \n"
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
        self.sign_up_button.setCheckable(False)
        self.sign_up_button.setChecked(False)
        self.sign_up_button.setAutoExclusive(False)
        self.sign_up_button.setAutoDefault(False)
        self.sign_up_button.setFlat(False)
        self.sign_up_email_icon = QLabel(self.sign_up_white_box)
        self.sign_up_email_icon.setObjectName(u"sign_up_email_icon")
        self.sign_up_email_icon.setGeometry(QRect(520, 255, 70, 65))
        self.sign_up_email_icon.setStyleSheet(u"background: #D9D9D9;")
        self.sign_up_email_icon.setPixmap(QPixmap(u"icons/email.png"))
        self.sign_up_email_icon.setScaledContents(True)
        self.sign_up_password_icon = QLabel(self.sign_up_white_box)
        self.sign_up_password_icon.setObjectName(u"sign_up_password_icon")
        self.sign_up_password_icon.setGeometry(QRect(520, 400, 70, 65))
        self.sign_up_password_icon.setStyleSheet(u"background: #D9D9D9;")
        self.sign_up_password_icon.setPixmap(QPixmap(u"icons/password.png"))
        self.sign_up_password_icon.setScaledContents(True)
        self.sign_up_icon = QLabel(self.sign_up_white_box)
        self.sign_up_icon.setObjectName(u"sign_up_icon")
        self.sign_up_icon.setGeometry(QRect(20, 100, 470, 470))
        self.sign_up_icon.setPixmap(QPixmap(u"icons/sgin up.png"))
        self.sign_up_icon.setScaledContents(True)
        self.sign_up_hide_show_button = QPushButton(self.sign_up_white_box)
        self.sign_up_hide_show_button.setObjectName(u"sign_up_hide_show_button")
        self.sign_up_hide_show_button.setGeometry(QRect(1070, 410, 61, 51))
        self.sign_up_hide_show_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sign_up_hide_show_button.setStyleSheet(u"QPushButton{\n"
"background: #D9D9D9;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #C0C0C0;\n"
"}")
        self.sign_up_hide_show_button.setIconSize(QSize(55, 55))
        self.sign_up_hide_show_button.setCheckable(True)
        self.welcoming_label = QLabel(self.sign_up_white_box)
        self.welcoming_label.setObjectName(u"welcoming_label")
        self.welcoming_label.setGeometry(QRect(720, 170, 211, 51))
        font2 = QFont()
        font2.setFamilies([u"MathJax_Main"])
        font2.setPointSize(20)
        self.welcoming_label.setFont(font2)
        self.welcoming_label.setStyleSheet(u"color: #2BCC6C;")
        self.sign_up_back_button = QPushButton(self.sign_up_white_box)
        self.sign_up_back_button.setObjectName(u"sign_up_back_button")
        self.sign_up_back_button.setGeometry(QRect(100, 550, 350, 104))
        self.sign_up_back_button.setFont(font1)
        self.sign_up_back_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sign_up_back_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #C0C0C0;\n"
"border-radius: 50%;\n"
"color: #FFFFFF; \n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #999999;\n"
"}\n"
"")

        self.retranslateUi(Sign_Up)

        self.sign_up_button.setDefault(False)


        QMetaObject.connectSlotsByName(Sign_Up)
    # setupUi

    def retranslateUi(self, Sign_Up):
        Sign_Up.setWindowTitle(QCoreApplication.translate("Sign_Up", u"Form", None))
        self.member_sign_up_label.setText(QCoreApplication.translate("Sign_Up", u"Member Sign up", None))
        self.sign_up_email_field.setInputMask("")
        self.sign_up_email_field.setText("")
        self.sign_up_email_field.setPlaceholderText(QCoreApplication.translate("Sign_Up", u"Email", None))
        self.sign_up_password_field.setInputMask("")
        self.sign_up_password_field.setText("")
        self.sign_up_password_field.setPlaceholderText(QCoreApplication.translate("Sign_Up", u"Password", None))
        self.sign_up_button.setText(QCoreApplication.translate("Sign_Up", u"Sign up", None))
        self.sign_up_email_icon.setText("")
        self.sign_up_password_icon.setText("")
        self.sign_up_icon.setText("")
        self.sign_up_hide_show_button.setText("")
        self.welcoming_label.setText(QCoreApplication.translate("Sign_Up", u"Let's get started!", None))
        self.sign_up_back_button.setText(QCoreApplication.translate("Sign_Up", u"Back", None))
    # retranslateUi

