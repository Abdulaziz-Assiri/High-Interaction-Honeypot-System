# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_rule_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Delete_Dialog(object):
    def setupUi(self, Delete_Dialog):
        if not Delete_Dialog.objectName():
            Delete_Dialog.setObjectName(u"Delete_Dialog")
        Delete_Dialog.resize(599, 369)
        self.container = QWidget(Delete_Dialog)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(0, 52, 600, 321))
        self.container.setStyleSheet(u"background: #1F1F1F;\n"
"")
        self.delete_number_label = QLabel(self.container)
        self.delete_number_label.setObjectName(u"delete_number_label")
        self.delete_number_label.setGeometry(QRect(20, 50, 301, 31))
        font = QFont()
        font.setFamilies([u"MathJax_Main"])
        font.setPointSize(18)
        self.delete_number_label.setFont(font)
        self.delete_number_label.setStyleSheet(u"color: #FFFFFF;")
        self.delete_rule_close_button = QPushButton(self.container)
        self.delete_rule_close_button.setObjectName(u"delete_rule_close_button")
        self.delete_rule_close_button.setGeometry(QRect(260, 250, 150, 50))
        font1 = QFont()
        font1.setFamilies([u"MathJax_Main"])
        font1.setPointSize(20)
        self.delete_rule_close_button.setFont(font1)
        self.delete_rule_close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_rule_close_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #FF0707;\n"
"border-radius: 10px;\n"
"color: #FFFFFF; \n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #CC0505;\n"
"}\n"
"")
        self.delete_rule_button = QPushButton(self.container)
        self.delete_rule_button.setObjectName(u"delete_rule_button")
        self.delete_rule_button.setGeometry(QRect(430, 250, 150, 50))
        self.delete_rule_button.setFont(font1)
        self.delete_rule_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_rule_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #30BD69;\n"
"border-radius: 10px;\n"
"color: #FFFFFF;\n"
" }\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #279A51;\n"
"}\n"
"")
        self.delete_rule_number_field = QLineEdit(self.container)
        self.delete_rule_number_field.setObjectName(u"delete_rule_number_field")
        self.delete_rule_number_field.setGeometry(QRect(20, 100, 551, 51))
        self.delete_rule_number_field.setFont(font)
        self.delete_rule_number_field.setStyleSheet(u"border: 0px;\n"
"background: #404040;\n"
"color: #FFFFFF;\n"
"border-radius: 10px;\n"
"padding-left: 15px;")
        self.star_6 = QLabel(self.container)
        self.star_6.setObjectName(u"star_6")
        self.star_6.setGeometry(QRect(330, 50, 16, 16))
        font2 = QFont()
        font2.setPointSize(16)
        self.star_6.setFont(font2)
        self.star_6.setStyleSheet(u"color: #FF0000;")
        self.delete_dialog_title = QLabel(Delete_Dialog)
        self.delete_dialog_title.setObjectName(u"delete_dialog_title")
        self.delete_dialog_title.setGeometry(QRect(0, 0, 600, 51))
        font3 = QFont()
        font3.setFamilies([u"MathJax_Main"])
        font3.setPointSize(26)
        self.delete_dialog_title.setFont(font3)
        self.delete_dialog_title.setStyleSheet(u"padding-left: 10px;\n"
"background: #404040;\n"
"color: #FFFFFF;")

        self.retranslateUi(Delete_Dialog)

        QMetaObject.connectSlotsByName(Delete_Dialog)
    # setupUi

    def retranslateUi(self, Delete_Dialog):
        Delete_Dialog.setWindowTitle(QCoreApplication.translate("Delete_Dialog", u"Dialog", None))
        self.delete_number_label.setText(QCoreApplication.translate("Delete_Dialog", u"Enter the number of the rule:", None))
        self.delete_rule_close_button.setText(QCoreApplication.translate("Delete_Dialog", u"Close", None))
        self.delete_rule_button.setText(QCoreApplication.translate("Delete_Dialog", u"Delete", None))
        self.delete_rule_number_field.setPlaceholderText(QCoreApplication.translate("Delete_Dialog", u"Number within the square brackets [ ]", None))
        self.star_6.setText(QCoreApplication.translate("Delete_Dialog", u"*", None))
        self.delete_dialog_title.setText(QCoreApplication.translate("Delete_Dialog", u"Delete a Firewall Rule", None))
    # retranslateUi

