# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_rule_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 800)
        self.dialog_title = QLabel(Dialog)
        self.dialog_title.setObjectName(u"dialog_title")
        self.dialog_title.setGeometry(QRect(0, 0, 600, 51))
        font = QFont()
        font.setFamilies([u"MathJax_Main"])
        font.setPointSize(26)
        self.dialog_title.setFont(font)
        self.dialog_title.setStyleSheet(u"padding-left: 10px;\n"
"background: #404040;\n"
"color: #FFFFFF;")
        self.container = QWidget(Dialog)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(0, 52, 600, 749))
        self.container.setStyleSheet(u"background: #1F1F1F;\n"
"")
        self.name_label = QLabel(self.container)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(20, 50, 71, 21))
        font1 = QFont()
        font1.setFamilies([u"MathJax_Main"])
        font1.setPointSize(18)
        self.name_label.setFont(font1)
        self.name_label.setStyleSheet(u"color: #FFFFFF;")
        self.policy_label = QLabel(self.container)
        self.policy_label.setObjectName(u"policy_label")
        self.policy_label.setGeometry(QRect(20, 290, 71, 31))
        self.policy_label.setFont(font1)
        self.policy_label.setStyleSheet(u"color: #FFFFFF;")
        self.direction_label = QLabel(self.container)
        self.direction_label.setObjectName(u"direction_label")
        self.direction_label.setGeometry(QRect(20, 370, 111, 21))
        self.direction_label.setFont(font1)
        self.direction_label.setStyleSheet(u"color: #FFFFFF;")
        self.port_label = QLabel(self.container)
        self.port_label.setObjectName(u"port_label")
        self.port_label.setGeometry(QRect(20, 530, 71, 21))
        self.port_label.setFont(font1)
        self.port_label.setStyleSheet(u"color: #FFFFFF;")
        self.protocol_label = QLabel(self.container)
        self.protocol_label.setObjectName(u"protocol_label")
        self.protocol_label.setGeometry(QRect(20, 450, 101, 21))
        self.protocol_label.setFont(font1)
        self.protocol_label.setStyleSheet(u"color: #FFFFFF;")
        self.rule_name_field = QLineEdit(self.container)
        self.rule_name_field.setObjectName(u"rule_name_field")
        self.rule_name_field.setGeometry(QRect(200, 40, 381, 40))
        font2 = QFont()
        font2.setFamilies([u"MathJax_Main"])
        font2.setPointSize(15)
        self.rule_name_field.setFont(font2)
        self.rule_name_field.setStyleSheet(u"border: 0px;\n"
"background: #404040;\n"
"color: #FFFFFF;\n"
"border-radius: 10px;\n"
"padding-left: 15px;")
        self.port_number_field = QLineEdit(self.container)
        self.port_number_field.setObjectName(u"port_number_field")
        self.port_number_field.setGeometry(QRect(200, 520, 381, 40))
        self.port_number_field.setFont(font2)
        self.port_number_field.setStyleSheet(u"border: 0px;\n"
"background: #404040;\n"
"color: #FFFFFF;\n"
"border-radius: 10px;\n"
"padding-left: 15px;")
        self.policy_combobox = QComboBox(self.container)
        self.policy_combobox.addItem("")
        self.policy_combobox.addItem("")
        self.policy_combobox.addItem("")
        self.policy_combobox.addItem("")
        self.policy_combobox.setObjectName(u"policy_combobox")
        self.policy_combobox.setGeometry(QRect(200, 280, 381, 40))
        self.policy_combobox.setFont(font2)
        self.policy_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.policy_combobox.setStyleSheet(u"QComboBox {\n"
"border: 0px;\n"
"background: #404040;\n"
"color: #FFFFFF;\n"
"border-radius: 10px;\n"
"padding-left: 15px;\n"
"}\n"
"")
        self.policy_combobox.setEditable(False)
        self.policy_combobox.setIconSize(QSize(16, 16))
        self.direction_combobox = QComboBox(self.container)
        self.direction_combobox.addItem("")
        self.direction_combobox.addItem("")
        self.direction_combobox.addItem("")
        self.direction_combobox.setObjectName(u"direction_combobox")
        self.direction_combobox.setGeometry(QRect(200, 360, 381, 40))
        self.direction_combobox.setFont(font2)
        self.direction_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.direction_combobox.setStyleSheet(u"QComboBox {\n"
"border: 0px;\n"
"background: #404040;\n"
"color: #FFFFFF;\n"
"border-radius: 10px;\n"
"padding-left: 15px;\n"
"}\n"
"")
        self.direction_combobox.setEditable(False)
        self.direction_combobox.setIconSize(QSize(16, 16))
        self.protocol_combobox = QComboBox(self.container)
        self.protocol_combobox.addItem("")
        self.protocol_combobox.addItem("")
        self.protocol_combobox.addItem("")
        self.protocol_combobox.setObjectName(u"protocol_combobox")
        self.protocol_combobox.setGeometry(QRect(200, 440, 381, 40))
        self.protocol_combobox.setFont(font2)
        self.protocol_combobox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.protocol_combobox.setStyleSheet(u"QComboBox {\n"
"border: 0px;\n"
"background: #404040;\n"
"color: #FFFFFF;\n"
"border-radius: 10px;\n"
"padding-left: 15px;\n"
"}\n"
"")
        self.protocol_combobox.setEditable(False)
        self.protocol_combobox.setIconSize(QSize(16, 16))
        self.close_button = QPushButton(self.container)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(260, 680, 150, 50))
        font3 = QFont()
        font3.setFamilies([u"MathJax_Main"])
        font3.setPointSize(20)
        self.close_button.setFont(font3)
        self.close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_button.setStyleSheet(u"QPushButton \n"
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
        self.add_rule_button = QPushButton(self.container)
        self.add_rule_button.setObjectName(u"add_rule_button")
        self.add_rule_button.setGeometry(QRect(430, 680, 150, 50))
        self.add_rule_button.setFont(font3)
        self.add_rule_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_rule_button.setStyleSheet(u"QPushButton \n"
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
        self.star_2 = QLabel(self.container)
        self.star_2.setObjectName(u"star_2")
        self.star_2.setGeometry(QRect(100, 290, 16, 16))
        font4 = QFont()
        font4.setPointSize(16)
        self.star_2.setFont(font4)
        self.star_2.setStyleSheet(u"color: #FF0000;")
        self.star_3 = QLabel(self.container)
        self.star_3.setObjectName(u"star_3")
        self.star_3.setGeometry(QRect(130, 360, 16, 16))
        self.star_3.setFont(font4)
        self.star_3.setStyleSheet(u"color: #FF0000;")
        self.star_4 = QLabel(self.container)
        self.star_4.setObjectName(u"star_4")
        self.star_4.setGeometry(QRect(120, 440, 16, 16))
        self.star_4.setFont(font4)
        self.star_4.setStyleSheet(u"color: #FF0000;")
        self.star_5 = QLabel(self.container)
        self.star_5.setObjectName(u"star_5")
        self.star_5.setGeometry(QRect(80, 520, 16, 16))
        self.star_5.setFont(font4)
        self.star_5.setStyleSheet(u"color: #FF0000;")
        self.source_label = QLabel(self.container)
        self.source_label.setObjectName(u"source_label")
        self.source_label.setGeometry(QRect(20, 130, 81, 21))
        self.source_label.setFont(font1)
        self.source_label.setStyleSheet(u"color: #FFFFFF;")
        self.source_field = QLineEdit(self.container)
        self.source_field.setObjectName(u"source_field")
        self.source_field.setGeometry(QRect(200, 120, 381, 40))
        self.source_field.setFont(font2)
        self.source_field.setStyleSheet(u"border: 0px;\n"
"background: #404040;\n"
"color: #FFFFFF;\n"
"border-radius: 10px;\n"
"padding-left: 15px;")
        self.destination_label = QLabel(self.container)
        self.destination_label.setObjectName(u"destination_label")
        self.destination_label.setGeometry(QRect(20, 210, 131, 21))
        self.destination_label.setFont(font1)
        self.destination_label.setStyleSheet(u"color: #FFFFFF;")
        self.destination_field = QLineEdit(self.container)
        self.destination_field.setObjectName(u"destination_field")
        self.destination_field.setGeometry(QRect(200, 200, 381, 40))
        self.destination_field.setFont(font2)
        self.destination_field.setStyleSheet(u"border: 0px;\n"
"background: #404040;\n"
"color: #FFFFFF;\n"
"border-radius: 10px;\n"
"padding-left: 15px;")
        self.star_6 = QLabel(self.container)
        self.star_6.setObjectName(u"star_6")
        self.star_6.setGeometry(QRect(100, 120, 16, 16))
        self.star_6.setFont(font4)
        self.star_6.setStyleSheet(u"color: #FF0000;")
        self.star_7 = QLabel(self.container)
        self.star_7.setObjectName(u"star_7")
        self.star_7.setGeometry(QRect(150, 200, 16, 16))
        self.star_7.setFont(font4)
        self.star_7.setStyleSheet(u"color: #FF0000;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.dialog_title.setText(QCoreApplication.translate("Dialog", u"Add a Firewall Rule", None))
        self.name_label.setText(QCoreApplication.translate("Dialog", u"Name:", None))
        self.policy_label.setText(QCoreApplication.translate("Dialog", u"Policy:", None))
        self.direction_label.setText(QCoreApplication.translate("Dialog", u"Direction:", None))
        self.port_label.setText(QCoreApplication.translate("Dialog", u"Port:", None))
        self.protocol_label.setText(QCoreApplication.translate("Dialog", u"Protocol:", None))
        self.rule_name_field.setPlaceholderText(QCoreApplication.translate("Dialog", u"Rule Description", None))
        self.port_number_field.setPlaceholderText(QCoreApplication.translate("Dialog", u"Number: 443, 22, ...", None))
        self.policy_combobox.setItemText(0, QCoreApplication.translate("Dialog", u"Allow", None))
        self.policy_combobox.setItemText(1, QCoreApplication.translate("Dialog", u"Deny", None))
        self.policy_combobox.setItemText(2, QCoreApplication.translate("Dialog", u"Reject", None))
        self.policy_combobox.setItemText(3, QCoreApplication.translate("Dialog", u"Limit", None))

        self.direction_combobox.setItemText(0, QCoreApplication.translate("Dialog", u"In", None))
        self.direction_combobox.setItemText(1, QCoreApplication.translate("Dialog", u"Out", None))
        self.direction_combobox.setItemText(2, QCoreApplication.translate("Dialog", u"Both", None))

        self.protocol_combobox.setItemText(0, QCoreApplication.translate("Dialog", u"Both", None))
        self.protocol_combobox.setItemText(1, QCoreApplication.translate("Dialog", u"TCP", None))
        self.protocol_combobox.setItemText(2, QCoreApplication.translate("Dialog", u"UDP", None))

        self.close_button.setText(QCoreApplication.translate("Dialog", u"Close", None))
        self.add_rule_button.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.star_2.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.star_3.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.star_4.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.star_5.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.source_label.setText(QCoreApplication.translate("Dialog", u"Source:", None))
        self.source_field.setPlaceholderText(QCoreApplication.translate("Dialog", u"IP address, network address or any", None))
        self.destination_label.setText(QCoreApplication.translate("Dialog", u"Destination:", None))
        self.destination_field.setPlaceholderText(QCoreApplication.translate("Dialog", u"IP address, network address or any", None))
        self.star_6.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.star_7.setText(QCoreApplication.translate("Dialog", u"*", None))
    # retranslateUi

