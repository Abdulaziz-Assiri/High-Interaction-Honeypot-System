# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Reset_Password.ui'
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
    QSizePolicy, QStackedWidget, QWidget)

class Ui_ResetPassword(object):
    def setupUi(self, ResetPassword):
        if not ResetPassword.objectName():
            ResetPassword.setObjectName(u"ResetPassword")
        ResetPassword.resize(1920, 1200)
        ResetPassword.setStyleSheet(u"QWidget{\n"
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
        self.reset_password_white_box = QWidget(ResetPassword)
        self.reset_password_white_box.setObjectName(u"reset_password_white_box")
        self.reset_password_white_box.setGeometry(QRect(345, 220, 1230, 600))
        self.reset_password_white_box.setStyleSheet(u"background: #FFFFFF;\n"
"border-radius: 12px;\n"
"")
        self.reset_password_label = QLabel(self.reset_password_white_box)
        self.reset_password_label.setObjectName(u"reset_password_label")
        self.reset_password_label.setGeometry(QRect(50, 50, 551, 91))
        font = QFont()
        font.setFamilies([u"MathJax_Main"])
        font.setPointSize(58)
        self.reset_password_label.setFont(font)
        self.reset_password_label.setStyleSheet(u"color: #000000;")
        self.reset_processes = QStackedWidget(self.reset_password_white_box)
        self.reset_processes.setObjectName(u"reset_processes")
        self.reset_processes.setGeometry(QRect(0, 150, 1231, 451))
        self.email_page = QWidget()
        self.email_page.setObjectName(u"email_page")
        self.continue_button = QPushButton(self.email_page)
        self.continue_button.setObjectName(u"continue_button")
        self.continue_button.setGeometry(QRect(438, 300, 721, 104))
        font1 = QFont()
        font1.setFamilies([u"MathJax_Main"])
        font1.setPointSize(24)
        self.continue_button.setFont(font1)
        self.continue_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.continue_button.setStyleSheet(u"QPushButton \n"
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
        self.continue_button.setCheckable(False)
        self.continue_button.setChecked(False)
        self.continue_button.setAutoExclusive(False)
        self.continue_button.setAutoDefault(False)
        self.continue_button.setFlat(False)
        self.message1_label = QLabel(self.email_page)
        self.message1_label.setObjectName(u"message1_label")
        self.message1_label.setGeometry(QRect(50, 20, 1081, 51))
        font2 = QFont()
        font2.setFamilies([u"MathJax_Main"])
        font2.setPointSize(20)
        self.message1_label.setFont(font2)
        self.message1_label.setStyleSheet(u"color: #2BCC6C;")
        self.reset_password_email_field = QLineEdit(self.email_page)
        self.reset_password_email_field.setObjectName(u"reset_password_email_field")
        self.reset_password_email_field.setGeometry(QRect(50, 120, 661, 104))
        self.reset_password_email_field.setFont(font1)
        self.reset_password_email_field.setAutoFillBackground(False)
        self.reset_password_email_field.setStyleSheet(u"background: #D9D9D9;\n"
"color: #000000;\n"
"border-radius: 50%;\n"
"padding-left: 100px;\n"
"padding-right: 15px;")
        self.reset_password_email_field.setClearButtonEnabled(False)
        self.reset_password_email_icon = QLabel(self.email_page)
        self.reset_password_email_icon.setObjectName(u"reset_password_email_icon")
        self.reset_password_email_icon.setGeometry(QRect(70, 140, 70, 65))
        self.reset_password_email_icon.setStyleSheet(u"background: #D9D9D9;")
        self.reset_password_email_icon.setPixmap(QPixmap(u"icons/email.png"))
        self.reset_password_email_icon.setScaledContents(True)
        self.email_cancel_button = QPushButton(self.email_page)
        self.email_cancel_button.setObjectName(u"email_cancel_button")
        self.email_cancel_button.setGeometry(QRect(50, 300, 350, 104))
        self.email_cancel_button.setFont(font1)
        self.email_cancel_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.email_cancel_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #FF0707;\n"
"border-radius: 50%;\n"
"color: #FFFFFF; \n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #CC0505;\n"
"}\n"
"")
        self.reset_processes.addWidget(self.email_page)
        self.code_page = QWidget()
        self.code_page.setObjectName(u"code_page")
        self.message2_label = QLabel(self.code_page)
        self.message2_label.setObjectName(u"message2_label")
        self.message2_label.setGeometry(QRect(50, 20, 1151, 71))
        self.message2_label.setFont(font2)
        self.message2_label.setStyleSheet(u"color: #2BCC6C;")
        self.first_field = QLineEdit(self.code_page)
        self.first_field.setObjectName(u"first_field")
        self.first_field.setGeometry(QRect(50, 130, 90, 100))
        font3 = QFont()
        font3.setFamilies([u"MathJax_Main"])
        font3.setPointSize(42)
        self.first_field.setFont(font3)
        self.first_field.setStyleSheet(u"background: #D9D9D9;\n"
"color: #000000;\n"
"border-radius: 20%;\n"
"padding-left: 20px;\n"
"padding-right: 20px;")
        self.first_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.second_field = QLineEdit(self.code_page)
        self.second_field.setObjectName(u"second_field")
        self.second_field.setGeometry(QRect(180, 130, 90, 100))
        self.second_field.setFont(font3)
        self.second_field.setStyleSheet(u"background: #D9D9D9;\n"
"color: #000000;\n"
"border-radius: 20%;\n"
"padding-left: 20px;\n"
"padding-right: 20px;")
        self.second_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.third_field = QLineEdit(self.code_page)
        self.third_field.setObjectName(u"third_field")
        self.third_field.setGeometry(QRect(310, 130, 90, 100))
        self.third_field.setFont(font3)
        self.third_field.setStyleSheet(u"background: #D9D9D9;\n"
"color: #000000;\n"
"border-radius: 20%;\n"
"padding-left: 20px;\n"
"padding-right: 20px;")
        self.third_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.forth_field = QLineEdit(self.code_page)
        self.forth_field.setObjectName(u"forth_field")
        self.forth_field.setGeometry(QRect(440, 130, 90, 100))
        self.forth_field.setFont(font3)
        self.forth_field.setStyleSheet(u"background: #D9D9D9;\n"
"color: #000000;\n"
"border-radius: 20%;\n"
"padding-left: 20px;\n"
"padding-right: 20px;")
        self.forth_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fifth_field = QLineEdit(self.code_page)
        self.fifth_field.setObjectName(u"fifth_field")
        self.fifth_field.setGeometry(QRect(570, 130, 90, 100))
        self.fifth_field.setFont(font3)
        self.fifth_field.setStyleSheet(u"background: #D9D9D9;\n"
"color: #000000;\n"
"border-radius: 20%;\n"
"padding-left: 20px;\n"
"padding-right: 20px;")
        self.fifth_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sixth_field = QLineEdit(self.code_page)
        self.sixth_field.setObjectName(u"sixth_field")
        self.sixth_field.setGeometry(QRect(700, 130, 90, 100))
        self.sixth_field.setFont(font3)
        self.sixth_field.setStyleSheet(u"background: #D9D9D9;\n"
"color: #000000;\n"
"border-radius: 20%;\n"
"padding-left: 20px;\n"
"padding-right: 20px;")
        self.sixth_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verify_button = QPushButton(self.code_page)
        self.verify_button.setObjectName(u"verify_button")
        self.verify_button.setGeometry(QRect(809, 300, 350, 104))
        self.verify_button.setFont(font1)
        self.verify_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.verify_button.setStyleSheet(u"QPushButton \n"
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
        self.verify_button.setCheckable(False)
        self.verify_button.setChecked(False)
        self.verify_button.setAutoExclusive(False)
        self.verify_button.setAutoDefault(False)
        self.verify_button.setFlat(False)
        self.code_cancel_button = QPushButton(self.code_page)
        self.code_cancel_button.setObjectName(u"code_cancel_button")
        self.code_cancel_button.setGeometry(QRect(50, 300, 350, 104))
        self.code_cancel_button.setFont(font1)
        self.code_cancel_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.code_cancel_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #FF0707;\n"
"border-radius: 50%;\n"
"color: #FFFFFF; \n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #CC0505;\n"
"}\n"
"")
        self.code_back_button = QPushButton(self.code_page)
        self.code_back_button.setObjectName(u"code_back_button")
        self.code_back_button.setGeometry(QRect(430, 300, 350, 104))
        self.code_back_button.setFont(font1)
        self.code_back_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.code_back_button.setStyleSheet(u"QPushButton \n"
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
        self.reset_processes.addWidget(self.code_page)
        self.reset_password_page = QWidget()
        self.reset_password_page.setObjectName(u"reset_password_page")
        self.reset_password_field = QLineEdit(self.reset_password_page)
        self.reset_password_field.setObjectName(u"reset_password_field")
        self.reset_password_field.setGeometry(QRect(50, 20, 661, 104))
        self.reset_password_field.setFont(font1)
        self.reset_password_field.setAutoFillBackground(False)
        self.reset_password_field.setStyleSheet(u"background: #D9D9D9;\n"
"color: #000000;\n"
"border-radius: 50%;\n"
"padding-left: 100px;\n"
"padding-right: 100px;")
        self.reset_password_field.setEchoMode(QLineEdit.EchoMode.Password)
        self.reset_password_field.setClearButtonEnabled(False)
        self.reset_password_icon = QLabel(self.reset_password_page)
        self.reset_password_icon.setObjectName(u"reset_password_icon")
        self.reset_password_icon.setGeometry(QRect(70, 40, 70, 65))
        self.reset_password_icon.setStyleSheet(u"background: #D9D9D9;")
        self.reset_password_icon.setPixmap(QPixmap(u"icons/password.png"))
        self.reset_password_icon.setScaledContents(True)
        self.reset_password_hide_show_button = QPushButton(self.reset_password_page)
        self.reset_password_hide_show_button.setObjectName(u"reset_password_hide_show_button")
        self.reset_password_hide_show_button.setGeometry(QRect(610, 50, 61, 51))
        self.reset_password_hide_show_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reset_password_hide_show_button.setStyleSheet(u"QPushButton{\n"
"background: #D9D9D9;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #C0C0C0;\n"
"}")
        self.reset_password_hide_show_button.setIconSize(QSize(55, 55))
        self.reset_password_hide_show_button.setCheckable(True)
        self.confirm_password_field = QLineEdit(self.reset_password_page)
        self.confirm_password_field.setObjectName(u"confirm_password_field")
        self.confirm_password_field.setGeometry(QRect(50, 160, 661, 104))
        self.confirm_password_field.setFont(font1)
        self.confirm_password_field.setAutoFillBackground(False)
        self.confirm_password_field.setStyleSheet(u"background: #D9D9D9;\n"
"color: #000000;\n"
"border-radius: 50%;\n"
"padding-left: 100px;\n"
"padding-right: 100px;")
        self.confirm_password_field.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_field.setClearButtonEnabled(False)
        self.reset_password_button = QPushButton(self.reset_password_page)
        self.reset_password_button.setObjectName(u"reset_password_button")
        self.reset_password_button.setGeometry(QRect(809, 300, 350, 104))
        self.reset_password_button.setFont(font1)
        self.reset_password_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reset_password_button.setStyleSheet(u"QPushButton \n"
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
        self.reset_password_button.setCheckable(False)
        self.reset_password_button.setChecked(False)
        self.reset_password_button.setAutoExclusive(False)
        self.reset_password_button.setAutoDefault(False)
        self.reset_password_button.setFlat(False)
        self.reset_password_cancel_button = QPushButton(self.reset_password_page)
        self.reset_password_cancel_button.setObjectName(u"reset_password_cancel_button")
        self.reset_password_cancel_button.setGeometry(QRect(50, 300, 350, 104))
        self.reset_password_cancel_button.setFont(font1)
        self.reset_password_cancel_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reset_password_cancel_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #FF0707;\n"
"border-radius: 50%;\n"
"color: #FFFFFF; \n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #CC0505;\n"
"}\n"
"")
        self.confirm_password_icon = QLabel(self.reset_password_page)
        self.confirm_password_icon.setObjectName(u"confirm_password_icon")
        self.confirm_password_icon.setGeometry(QRect(70, 180, 70, 65))
        self.confirm_password_icon.setStyleSheet(u"background: #D9D9D9;")
        self.confirm_password_icon.setPixmap(QPixmap(u"icons/password.png"))
        self.confirm_password_icon.setScaledContents(True)
        self.confirm_password_hide_show_button = QPushButton(self.reset_password_page)
        self.confirm_password_hide_show_button.setObjectName(u"confirm_password_hide_show_button")
        self.confirm_password_hide_show_button.setGeometry(QRect(620, 190, 61, 51))
        self.confirm_password_hide_show_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.confirm_password_hide_show_button.setStyleSheet(u"QPushButton{\n"
"background: #D9D9D9;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #C0C0C0;\n"
"}")
        self.confirm_password_hide_show_button.setIconSize(QSize(55, 55))
        self.confirm_password_hide_show_button.setCheckable(True)
        self.reset_password_back_button = QPushButton(self.reset_password_page)
        self.reset_password_back_button.setObjectName(u"reset_password_back_button")
        self.reset_password_back_button.setGeometry(QRect(430, 300, 350, 104))
        self.reset_password_back_button.setFont(font1)
        self.reset_password_back_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reset_password_back_button.setStyleSheet(u"QPushButton \n"
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
        self.reset_processes.addWidget(self.reset_password_page)

        self.retranslateUi(ResetPassword)

        self.reset_processes.setCurrentIndex(0)
        self.continue_button.setDefault(False)
        self.verify_button.setDefault(False)
        self.reset_password_button.setDefault(False)


        QMetaObject.connectSlotsByName(ResetPassword)
    # setupUi

    def retranslateUi(self, ResetPassword):
        ResetPassword.setWindowTitle(QCoreApplication.translate("ResetPassword", u"Form", None))
        self.reset_password_label.setText(QCoreApplication.translate("ResetPassword", u"Reset Password", None))
        self.continue_button.setText(QCoreApplication.translate("ResetPassword", u"Continue", None))
        self.message1_label.setText(QCoreApplication.translate("ResetPassword", u"Please ensure the email address is correct.  A password reset code will be sent to this address.", None))
        self.reset_password_email_field.setInputMask("")
        self.reset_password_email_field.setText("")
        self.reset_password_email_field.setPlaceholderText(QCoreApplication.translate("ResetPassword", u"Email", None))
        self.reset_password_email_icon.setText("")
        self.email_cancel_button.setText(QCoreApplication.translate("ResetPassword", u"Cancel", None))
        self.message2_label.setText("")
        self.verify_button.setText(QCoreApplication.translate("ResetPassword", u"Verify", None))
        self.code_cancel_button.setText(QCoreApplication.translate("ResetPassword", u"Cancel", None))
        self.code_back_button.setText(QCoreApplication.translate("ResetPassword", u"Back", None))
        self.reset_password_field.setInputMask("")
        self.reset_password_field.setText("")
        self.reset_password_field.setPlaceholderText(QCoreApplication.translate("ResetPassword", u"Password", None))
        self.reset_password_icon.setText("")
        self.reset_password_hide_show_button.setText("")
        self.confirm_password_field.setInputMask("")
        self.confirm_password_field.setText("")
        self.confirm_password_field.setPlaceholderText(QCoreApplication.translate("ResetPassword", u"Confirm Password", None))
        self.reset_password_button.setText(QCoreApplication.translate("ResetPassword", u"Reset Password", None))
        self.reset_password_cancel_button.setText(QCoreApplication.translate("ResetPassword", u"Cancel", None))
        self.confirm_password_icon.setText("")
        self.confirm_password_hide_show_button.setText("")
        self.reset_password_back_button.setText(QCoreApplication.translate("ResetPassword", u"Back", None))
    # retranslateUi

