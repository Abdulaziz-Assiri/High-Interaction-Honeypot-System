# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report_ip_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_report_Dialog(object):
    def setupUi(self, report_Dialog):
        if not report_Dialog.objectName():
            report_Dialog.setObjectName(u"report_Dialog")
        report_Dialog.resize(1100, 720)
        report_Dialog.setStyleSheet(u"")
        self.ip_address_label = QLabel(report_Dialog)
        self.ip_address_label.setObjectName(u"ip_address_label")
        self.ip_address_label.setGeometry(QRect(20, 20, 121, 21))
        font = QFont()
        font.setFamilies([u"MathJax_Main"])
        font.setPointSize(18)
        self.ip_address_label.setFont(font)
        self.ip_address_label.setStyleSheet(u"")
        self.ip_address_example = QLabel(report_Dialog)
        self.ip_address_example.setObjectName(u"ip_address_example")
        self.ip_address_example.setGeometry(QRect(150, 14, 131, 31))
        self.ip_address_example.setFont(font)
        self.ip_address_example.setStyleSheet(u"color: #999999;")
        self.reported_ip_field = QLineEdit(report_Dialog)
        self.reported_ip_field.setObjectName(u"reported_ip_field")
        self.reported_ip_field.setGeometry(QRect(20, 60, 1061, 60))
        self.reported_ip_field.setFont(font)
        self.reported_ip_field.setStyleSheet(u"border: 0px;\n"
"background: #2F2F2F;\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"color: #FFFFFF;")
        self.category_label = QLabel(report_Dialog)
        self.category_label.setObjectName(u"category_label")
        self.category_label.setGeometry(QRect(20, 140, 111, 31))
        self.category_label.setFont(font)
        self.category_label.setStyleSheet(u"")
        self.select_one_label = QLabel(report_Dialog)
        self.select_one_label.setObjectName(u"select_one_label")
        self.select_one_label.setGeometry(QRect(140, 140, 251, 31))
        self.select_one_label.setFont(font)
        self.select_one_label.setStyleSheet(u"color: #999999;")
        self.dns_compromise_checkbox = QCheckBox(report_Dialog)
        self.dns_compromise_checkbox.setObjectName(u"dns_compromise_checkbox")
        self.dns_compromise_checkbox.setGeometry(QRect(30, 200, 221, 21))
        font1 = QFont()
        font1.setFamilies([u"MathJax_Main"])
        font1.setPointSize(16)
        self.dns_compromise_checkbox.setFont(font1)
        self.dns_compromise_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dns_compromise_checkbox.setStyleSheet(u"")
        self.dns_poisoning_checkbox = QCheckBox(report_Dialog)
        self.dns_poisoning_checkbox.setObjectName(u"dns_poisoning_checkbox")
        self.dns_poisoning_checkbox.setGeometry(QRect(30, 240, 191, 21))
        self.dns_poisoning_checkbox.setFont(font1)
        self.dns_poisoning_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fraud_orders_checkbox = QCheckBox(report_Dialog)
        self.fraud_orders_checkbox.setObjectName(u"fraud_orders_checkbox")
        self.fraud_orders_checkbox.setGeometry(QRect(30, 280, 171, 21))
        self.fraud_orders_checkbox.setFont(font1)
        self.fraud_orders_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.web_spam_checkbox = QCheckBox(report_Dialog)
        self.web_spam_checkbox.setObjectName(u"web_spam_checkbox")
        self.web_spam_checkbox.setGeometry(QRect(290, 280, 151, 21))
        self.web_spam_checkbox.setFont(font1)
        self.web_spam_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.open_proxy_checkbox = QCheckBox(report_Dialog)
        self.open_proxy_checkbox.setObjectName(u"open_proxy_checkbox")
        self.open_proxy_checkbox.setGeometry(QRect(290, 240, 161, 21))
        self.open_proxy_checkbox.setFont(font1)
        self.open_proxy_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ddos_attack_checkbox = QCheckBox(report_Dialog)
        self.ddos_attack_checkbox.setObjectName(u"ddos_attack_checkbox")
        self.ddos_attack_checkbox.setGeometry(QRect(290, 200, 181, 21))
        self.ddos_attack_checkbox.setFont(font1)
        self.ddos_attack_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ddos_attack_checkbox.setStyleSheet(u"")
        self.spoofing_checkbox = QCheckBox(report_Dialog)
        self.spoofing_checkbox.setObjectName(u"spoofing_checkbox")
        self.spoofing_checkbox.setGeometry(QRect(550, 280, 131, 21))
        self.spoofing_checkbox.setFont(font1)
        self.spoofing_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.port_scan_checkbox = QCheckBox(report_Dialog)
        self.port_scan_checkbox.setObjectName(u"port_scan_checkbox")
        self.port_scan_checkbox.setGeometry(QRect(550, 240, 141, 21))
        self.port_scan_checkbox.setFont(font1)
        self.port_scan_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.email_spam_checkbox = QCheckBox(report_Dialog)
        self.email_spam_checkbox.setObjectName(u"email_spam_checkbox")
        self.email_spam_checkbox.setGeometry(QRect(550, 200, 171, 21))
        self.email_spam_checkbox.setFont(font1)
        self.email_spam_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exploited_host_checkbox = QCheckBox(report_Dialog)
        self.exploited_host_checkbox.setObjectName(u"exploited_host_checkbox")
        self.exploited_host_checkbox.setGeometry(QRect(810, 280, 181, 21))
        self.exploited_host_checkbox.setFont(font1)
        self.exploited_host_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bad_web_bot_checkbox = QCheckBox(report_Dialog)
        self.bad_web_bot_checkbox.setObjectName(u"bad_web_bot_checkbox")
        self.bad_web_bot_checkbox.setGeometry(QRect(810, 240, 181, 21))
        self.bad_web_bot_checkbox.setFont(font1)
        self.bad_web_bot_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.brute_force_checkbox = QCheckBox(report_Dialog)
        self.brute_force_checkbox.setObjectName(u"brute_force_checkbox")
        self.brute_force_checkbox.setGeometry(QRect(810, 200, 161, 21))
        self.brute_force_checkbox.setFont(font1)
        self.brute_force_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.iot_targeted_checkbox = QCheckBox(report_Dialog)
        self.iot_targeted_checkbox.setObjectName(u"iot_targeted_checkbox")
        self.iot_targeted_checkbox.setGeometry(QRect(30, 420, 171, 21))
        self.iot_targeted_checkbox.setFont(font1)
        self.iot_targeted_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ssh_checkbox = QCheckBox(report_Dialog)
        self.ssh_checkbox.setObjectName(u"ssh_checkbox")
        self.ssh_checkbox.setGeometry(QRect(30, 380, 91, 21))
        self.ssh_checkbox.setFont(font1)
        self.ssh_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.web_app_attack_checkbox = QCheckBox(report_Dialog)
        self.web_app_attack_checkbox.setObjectName(u"web_app_attack_checkbox")
        self.web_app_attack_checkbox.setGeometry(QRect(30, 340, 201, 21))
        self.web_app_attack_checkbox.setFont(font1)
        self.web_app_attack_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.web_app_attack_checkbox.setStyleSheet(u"")
        self.phishing_checkbox = QCheckBox(report_Dialog)
        self.phishing_checkbox.setObjectName(u"phishing_checkbox")
        self.phishing_checkbox.setGeometry(QRect(290, 420, 141, 21))
        self.phishing_checkbox.setFont(font1)
        self.phishing_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ping_of_death_checkbox = QCheckBox(report_Dialog)
        self.ping_of_death_checkbox.setObjectName(u"ping_of_death_checkbox")
        self.ping_of_death_checkbox.setGeometry(QRect(290, 380, 181, 21))
        self.ping_of_death_checkbox.setFont(font1)
        self.ping_of_death_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ftp_brute_force_checkbox = QCheckBox(report_Dialog)
        self.ftp_brute_force_checkbox.setObjectName(u"ftp_brute_force_checkbox")
        self.ftp_brute_force_checkbox.setGeometry(QRect(290, 340, 211, 21))
        self.ftp_brute_force_checkbox.setFont(font1)
        self.ftp_brute_force_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ftp_brute_force_checkbox.setStyleSheet(u"")
        self.vpn_ip_checkbox = QCheckBox(report_Dialog)
        self.vpn_ip_checkbox.setObjectName(u"vpn_ip_checkbox")
        self.vpn_ip_checkbox.setGeometry(QRect(550, 420, 131, 21))
        self.vpn_ip_checkbox.setFont(font1)
        self.vpn_ip_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.blog_spam_checkbox = QCheckBox(report_Dialog)
        self.blog_spam_checkbox.setObjectName(u"blog_spam_checkbox")
        self.blog_spam_checkbox.setGeometry(QRect(550, 380, 151, 21))
        self.blog_spam_checkbox.setFont(font1)
        self.blog_spam_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fraud_voip_checkbox = QCheckBox(report_Dialog)
        self.fraud_voip_checkbox.setObjectName(u"fraud_voip_checkbox")
        self.fraud_voip_checkbox.setGeometry(QRect(550, 340, 161, 21))
        self.fraud_voip_checkbox.setFont(font1)
        self.fraud_voip_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fraud_voip_checkbox.setStyleSheet(u"")
        self.sql_injection_checkbox = QCheckBox(report_Dialog)
        self.sql_injection_checkbox.setObjectName(u"sql_injection_checkbox")
        self.sql_injection_checkbox.setGeometry(QRect(810, 380, 171, 21))
        self.sql_injection_checkbox.setFont(font1)
        self.sql_injection_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.hacking_checkbox = QCheckBox(report_Dialog)
        self.hacking_checkbox.setObjectName(u"hacking_checkbox")
        self.hacking_checkbox.setGeometry(QRect(810, 340, 131, 21))
        self.hacking_checkbox.setFont(font1)
        self.hacking_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.hacking_checkbox.setStyleSheet(u"")
        self.ip_report_comment_label = QLabel(report_Dialog)
        self.ip_report_comment_label.setObjectName(u"ip_report_comment_label")
        self.ip_report_comment_label.setGeometry(QRect(20, 460, 111, 31))
        self.ip_report_comment_label.setFont(font)
        self.ip_report_comment_label.setStyleSheet(u"")
        self.ip_report_comment_field = QTextEdit(report_Dialog)
        self.ip_report_comment_field.setObjectName(u"ip_report_comment_field")
        self.ip_report_comment_field.setGeometry(QRect(20, 500, 1061, 91))
        self.ip_report_comment_field.setFont(font1)
        self.ip_report_comment_field.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.ip_report_comment_field.setStyleSheet(u"color: #FFFFFF;\n"
"background: #2F2F2F;\n"
"border-radius: 10px;\n"
"padding: 20px;")
        self.ip_report_comment_field.setReadOnly(False)
        self.ip_report_close_button = QPushButton(report_Dialog)
        self.ip_report_close_button.setObjectName(u"ip_report_close_button")
        self.ip_report_close_button.setGeometry(QRect(20, 630, 191, 61))
        font2 = QFont()
        font2.setFamilies([u"MathJax_Main"])
        font2.setPointSize(24)
        self.ip_report_close_button.setFont(font2)
        self.ip_report_close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ip_report_close_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #FF0707;\n"
"border-radius: 30%;\n"
"color: #FFFFFF; \n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #CC0505;\n"
"}")
        self.ip_report_close_button.setCheckable(False)
        self.ip_report_close_button.setChecked(False)
        self.ip_report_close_button.setAutoExclusive(False)
        self.ip_report_close_button.setAutoDefault(False)
        self.ip_report_close_button.setFlat(False)
        self.report_ip_address_button = QPushButton(report_Dialog)
        self.report_ip_address_button.setObjectName(u"report_ip_address_button")
        self.report_ip_address_button.setGeometry(QRect(235, 630, 301, 61))
        self.report_ip_address_button.setFont(font2)
        self.report_ip_address_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.report_ip_address_button.setStyleSheet(u"QPushButton \n"
"{\n"
"        background-color: #2BCC6C; \n"
"        color: #FFFFFF;\n"
"        border-radius: 30%;\n"
" }\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #279A51;\n"
"}\n"
"")
        self.report_ip_address_button.setCheckable(False)
        self.report_ip_address_button.setChecked(False)
        self.report_ip_address_button.setAutoExclusive(False)
        self.report_ip_address_button.setAutoDefault(False)
        self.report_ip_address_button.setFlat(False)
        self.dns_compromise_info = QLabel(report_Dialog)
        self.dns_compromise_info.setObjectName(u"dns_compromise_info")
        self.dns_compromise_info.setGeometry(QRect(220, 199, 25, 25))
        self.dns_compromise_info.setToolTipDuration(-1)
        self.dns_compromise_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.dns_compromise_info.setScaledContents(True)
        self.dns_poisoning_info = QLabel(report_Dialog)
        self.dns_poisoning_info.setObjectName(u"dns_poisoning_info")
        self.dns_poisoning_info.setGeometry(QRect(195, 240, 25, 25))
        self.dns_poisoning_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.dns_poisoning_info.setScaledContents(True)
        self.fraud_orders_info = QLabel(report_Dialog)
        self.fraud_orders_info.setObjectName(u"fraud_orders_info")
        self.fraud_orders_info.setGeometry(QRect(180, 280, 25, 25))
        self.fraud_orders_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.fraud_orders_info.setScaledContents(True)
        self.web_app_attack_info = QLabel(report_Dialog)
        self.web_app_attack_info.setObjectName(u"web_app_attack_info")
        self.web_app_attack_info.setGeometry(QRect(210, 340, 25, 25))
        self.web_app_attack_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.web_app_attack_info.setScaledContents(True)
        self.ssh_info = QLabel(report_Dialog)
        self.ssh_info.setObjectName(u"ssh_info")
        self.ssh_info.setGeometry(QRect(100, 380, 25, 25))
        self.ssh_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.ssh_info.setScaledContents(True)
        self.iot_targeted_info = QLabel(report_Dialog)
        self.iot_targeted_info.setObjectName(u"iot_targeted_info")
        self.iot_targeted_info.setGeometry(QRect(180, 420, 25, 25))
        self.iot_targeted_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.iot_targeted_info.setScaledContents(True)
        self.ddos_attack_info = QLabel(report_Dialog)
        self.ddos_attack_info.setObjectName(u"ddos_attack_info")
        self.ddos_attack_info.setGeometry(QRect(440, 200, 25, 25))
        self.ddos_attack_info.setToolTipDuration(-1)
        self.ddos_attack_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.ddos_attack_info.setScaledContents(True)
        self.web_spam_info = QLabel(report_Dialog)
        self.web_spam_info.setObjectName(u"web_spam_info")
        self.web_spam_info.setGeometry(QRect(415, 280, 25, 25))
        self.web_spam_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.web_spam_info.setScaledContents(True)
        self.phishing_info = QLabel(report_Dialog)
        self.phishing_info.setObjectName(u"phishing_info")
        self.phishing_info.setGeometry(QRect(400, 420, 25, 25))
        self.phishing_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.phishing_info.setScaledContents(True)
        self.ping_of_death_info = QLabel(report_Dialog)
        self.ping_of_death_info.setObjectName(u"ping_of_death_info")
        self.ping_of_death_info.setGeometry(QRect(440, 380, 25, 25))
        self.ping_of_death_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.ping_of_death_info.setScaledContents(True)
        self.ftp_brute_force_info = QLabel(report_Dialog)
        self.ftp_brute_force_info.setObjectName(u"ftp_brute_force_info")
        self.ftp_brute_force_info.setGeometry(QRect(475, 340, 25, 25))
        self.ftp_brute_force_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.ftp_brute_force_info.setScaledContents(True)
        self.open_proxy_info = QLabel(report_Dialog)
        self.open_proxy_info.setObjectName(u"open_proxy_info")
        self.open_proxy_info.setGeometry(QRect(425, 240, 25, 25))
        self.open_proxy_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.open_proxy_info.setScaledContents(True)
        self.vpn_ip_info = QLabel(report_Dialog)
        self.vpn_ip_info.setObjectName(u"vpn_ip_info")
        self.vpn_ip_info.setGeometry(QRect(650, 415, 25, 25))
        self.vpn_ip_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.vpn_ip_info.setScaledContents(True)
        self.email_spam_info = QLabel(report_Dialog)
        self.email_spam_info.setObjectName(u"email_spam_info")
        self.email_spam_info.setGeometry(QRect(685, 200, 25, 25))
        self.email_spam_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.email_spam_info.setScaledContents(True)
        self.fraud_voip_info = QLabel(report_Dialog)
        self.fraud_voip_info.setObjectName(u"fraud_voip_info")
        self.fraud_voip_info.setGeometry(QRect(683, 335, 25, 25))
        self.fraud_voip_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.fraud_voip_info.setScaledContents(True)
        self.blog_spam_info = QLabel(report_Dialog)
        self.blog_spam_info.setObjectName(u"blog_spam_info")
        self.blog_spam_info.setGeometry(QRect(675, 380, 25, 25))
        self.blog_spam_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.blog_spam_info.setScaledContents(True)
        self.spoofing_info = QLabel(report_Dialog)
        self.spoofing_info.setObjectName(u"spoofing_info")
        self.spoofing_info.setGeometry(QRect(655, 280, 25, 25))
        self.spoofing_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.spoofing_info.setScaledContents(True)
        self.port_scan_info = QLabel(report_Dialog)
        self.port_scan_info.setObjectName(u"port_scan_info")
        self.port_scan_info.setGeometry(QRect(665, 240, 25, 25))
        self.port_scan_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.port_scan_info.setScaledContents(True)
        self.exploited_host_info = QLabel(report_Dialog)
        self.exploited_host_info.setObjectName(u"exploited_host_info")
        self.exploited_host_info.setGeometry(QRect(970, 280, 25, 25))
        self.exploited_host_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.exploited_host_info.setScaledContents(True)
        self.hacking_info = QLabel(report_Dialog)
        self.hacking_info.setObjectName(u"hacking_info")
        self.hacking_info.setGeometry(QRect(910, 340, 25, 25))
        self.hacking_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.hacking_info.setScaledContents(True)
        self.sql_injection_info = QLabel(report_Dialog)
        self.sql_injection_info.setObjectName(u"sql_injection_info")
        self.sql_injection_info.setGeometry(QRect(960, 380, 25, 25))
        self.sql_injection_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.sql_injection_info.setScaledContents(True)
        self.brute_force_info = QLabel(report_Dialog)
        self.brute_force_info.setObjectName(u"brute_force_info")
        self.brute_force_info.setGeometry(QRect(945, 200, 25, 25))
        self.brute_force_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.brute_force_info.setScaledContents(True)
        self.bad_web_bot_info = QLabel(report_Dialog)
        self.bad_web_bot_info.setObjectName(u"bad_web_bot_info")
        self.bad_web_bot_info.setGeometry(QRect(960, 240, 25, 25))
        self.bad_web_bot_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.bad_web_bot_info.setScaledContents(True)
        self.star = QLabel(report_Dialog)
        self.star.setObjectName(u"star")
        self.star.setGeometry(QRect(140, 10, 16, 16))
        font3 = QFont()
        font3.setPointSize(16)
        self.star.setFont(font3)
        self.star.setStyleSheet(u"color: #FF0000;")
        self.star_2 = QLabel(report_Dialog)
        self.star_2.setObjectName(u"star_2")
        self.star_2.setGeometry(QRect(130, 130, 16, 16))
        self.star_2.setFont(font3)
        self.star_2.setStyleSheet(u"color: #FF0000;")

        self.retranslateUi(report_Dialog)

        self.ip_report_close_button.setDefault(False)
        self.report_ip_address_button.setDefault(False)


        QMetaObject.connectSlotsByName(report_Dialog)
    # setupUi

    def retranslateUi(self, report_Dialog):
        report_Dialog.setWindowTitle(QCoreApplication.translate("report_Dialog", u"Dialog", None))
        self.ip_address_label.setText(QCoreApplication.translate("report_Dialog", u"IP Address", None))
        self.ip_address_example.setText(QCoreApplication.translate("report_Dialog", u"(ex. 8.8.8.8)", None))
        self.reported_ip_field.setText("")
        self.reported_ip_field.setPlaceholderText(QCoreApplication.translate("report_Dialog", u"IPv4", None))
        self.category_label.setText(QCoreApplication.translate("report_Dialog", u"Categories", None))
        self.select_one_label.setText(QCoreApplication.translate("report_Dialog", u"(at least one is required)", None))
        self.dns_compromise_checkbox.setText(QCoreApplication.translate("report_Dialog", u"DNS Compromise", None))
        self.dns_poisoning_checkbox.setText(QCoreApplication.translate("report_Dialog", u"DNS Poisoning ", None))
        self.fraud_orders_checkbox.setText(QCoreApplication.translate("report_Dialog", u"Fraud Orders ", None))
        self.web_spam_checkbox.setText(QCoreApplication.translate("report_Dialog", u"Web Spam ", None))
        self.open_proxy_checkbox.setText(QCoreApplication.translate("report_Dialog", u"Open Proxy ", None))
        self.ddos_attack_checkbox.setText(QCoreApplication.translate("report_Dialog", u"DDoS Attack ", None))
        self.spoofing_checkbox.setText(QCoreApplication.translate("report_Dialog", u"Spoofing", None))
        self.port_scan_checkbox.setText(QCoreApplication.translate("report_Dialog", u"Port Scan ", None))
        self.email_spam_checkbox.setText(QCoreApplication.translate("report_Dialog", u"Email Spam ", None))
        self.exploited_host_checkbox.setText(QCoreApplication.translate("report_Dialog", u"Exploited Host ", None))
        self.bad_web_bot_checkbox.setText(QCoreApplication.translate("report_Dialog", u"Bad Web Bot ", None))
        self.brute_force_checkbox.setText(QCoreApplication.translate("report_Dialog", u"Brute-Force ", None))
        self.iot_targeted_checkbox.setText(QCoreApplication.translate("report_Dialog", u"IoT Targeted ", None))
        self.ssh_checkbox.setText(QCoreApplication.translate("report_Dialog", u"SSH", None))
        self.web_app_attack_checkbox.setText(QCoreApplication.translate("report_Dialog", u"Web App Attack ", None))
        self.phishing_checkbox.setText(QCoreApplication.translate("report_Dialog", u"Phishing", None))
        self.ping_of_death_checkbox.setText(QCoreApplication.translate("report_Dialog", u"Ping of Death ", None))
        self.ftp_brute_force_checkbox.setText(QCoreApplication.translate("report_Dialog", u"FTP Brute-Force\n"
"", None))
        self.vpn_ip_checkbox.setText(QCoreApplication.translate("report_Dialog", u"VPN IP", None))
        self.blog_spam_checkbox.setText(QCoreApplication.translate("report_Dialog", u"Blog Spam", None))
        self.fraud_voip_checkbox.setText(QCoreApplication.translate("report_Dialog", u"Fraud VoIP", None))
        self.sql_injection_checkbox.setText(QCoreApplication.translate("report_Dialog", u"SQL Injection", None))
        self.hacking_checkbox.setText(QCoreApplication.translate("report_Dialog", u"Hacking", None))
        self.ip_report_comment_label.setText(QCoreApplication.translate("report_Dialog", u"Comment", None))
        self.ip_report_comment_field.setPlaceholderText(QCoreApplication.translate("report_Dialog", u"Comment (server log snippets, abuse details, etc)", None))
        self.ip_report_close_button.setText(QCoreApplication.translate("report_Dialog", u"Close", None))
        self.report_ip_address_button.setText(QCoreApplication.translate("report_Dialog", u"Report IP Address", None))
#if QT_CONFIG(tooltip)
        self.dns_compromise_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Altering DNS records\n"
"resulting in improper\n"
"redirection.", None))
#endif // QT_CONFIG(tooltip)
        self.dns_compromise_info.setText("")
#if QT_CONFIG(tooltip)
        self.dns_poisoning_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Falsifying domain server\n"
"cache (cache poisoning).", None))
#endif // QT_CONFIG(tooltip)
        self.dns_poisoning_info.setText("")
#if QT_CONFIG(tooltip)
        self.fraud_orders_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Fraudulent orders.", None))
#endif // QT_CONFIG(tooltip)
        self.fraud_orders_info.setText("")
#if QT_CONFIG(tooltip)
        self.web_app_attack_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Attempts to probe for or\n"
"exploit installed web\n"
"applications such as a\n"
"CMS like\n"
"WordPress/Drupal, e-\n"
"commerce solutions,\n"
"forum software,\n"
"phpMyAdmin and\n"
"various other software\n"
"plugins/solutions.", None))
#endif // QT_CONFIG(tooltip)
        self.web_app_attack_info.setText("")
#if QT_CONFIG(tooltip)
        self.ssh_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Secure Shell (SSH) abuse.Use\n"
"this category in combination with\n"
"more specific categories.", None))
#endif // QT_CONFIG(tooltip)
        self.ssh_info.setText("")
#if QT_CONFIG(tooltip)
        self.iot_targeted_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Abuse was targeted at an\n"
"\"Internet of Things\" type\n"
"device. Include information\n"
"about what type of device\n"
"was targeted in the\n"
"comments.", None))
#endif // QT_CONFIG(tooltip)
        self.iot_targeted_info.setText("")
#if QT_CONFIG(tooltip)
        self.ddos_attack_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Participating in distributed\n"
"denial-of-service (usually\n"
"part of botnet).", None))
#endif // QT_CONFIG(tooltip)
        self.ddos_attack_info.setText("")
#if QT_CONFIG(tooltip)
        self.web_spam_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Comment/forum spam, HTTP\n"
"referer spam, or other CMS\n"
"spam.", None))
#endif // QT_CONFIG(tooltip)
        self.web_spam_info.setText("")
#if QT_CONFIG(tooltip)
        self.phishing_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Phishing websites and/or email.", None))
#endif // QT_CONFIG(tooltip)
        self.phishing_info.setText("")
#if QT_CONFIG(tooltip)
        self.ping_of_death_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Oversized IP packet.", None))
#endif // QT_CONFIG(tooltip)
        self.ping_of_death_info.setText("")
#if QT_CONFIG(tooltip)
        self.ftp_brute_force_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Attempting to gain unauthorized\n"
"access to an FTP server.", None))
#endif // QT_CONFIG(tooltip)
        self.ftp_brute_force_info.setText("")
#if QT_CONFIG(tooltip)
        self.open_proxy_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Open proxy, open relay, or\n"
"Tor exit node.", None))
#endif // QT_CONFIG(tooltip)
        self.open_proxy_info.setText("")
#if QT_CONFIG(tooltip)
        self.vpn_ip_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Conjunctive category.", None))
#endif // QT_CONFIG(tooltip)
        self.vpn_ip_info.setText("")
#if QT_CONFIG(tooltip)
        self.email_spam_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Spam email content, infected\n"
"attachments, and phishing\n"
"emails. Note: Limit comments\n"
"to only relevent information\n"
"(instead of log dumps) and\n"
"be sure to remove PII if you\n"
"want to remain anonymous.", None))
#endif // QT_CONFIG(tooltip)
        self.email_spam_info.setText("")
#if QT_CONFIG(tooltip)
        self.fraud_voip_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Unauthorized use of Voice over\n"
"Internet Protocol (VoIP) services\n"
"to make calls without paying or\n"
"to mask the caller's\n"
"true identity,\n"
"often for malicious purposes.", None))
#endif // QT_CONFIG(tooltip)
        self.fraud_voip_info.setText("")
#if QT_CONFIG(tooltip)
        self.blog_spam_info.setToolTip(QCoreApplication.translate("report_Dialog", u"CMS blog comment spam.", None))
#endif // QT_CONFIG(tooltip)
        self.blog_spam_info.setText("")
#if QT_CONFIG(tooltip)
        self.spoofing_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Email sender spoofing.", None))
#endif // QT_CONFIG(tooltip)
        self.spoofing_info.setText("")
#if QT_CONFIG(tooltip)
        self.port_scan_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Scanning for open ports and\n"
"vulnerable services. ", None))
#endif // QT_CONFIG(tooltip)
        self.port_scan_info.setText("")
#if QT_CONFIG(tooltip)
        self.exploited_host_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Host is likely infected with\n"
"malware and being used\n"
"for other attacks or to host\n"
"malicious content. The\n"
"host owner may not be\n"
"aware of the compromise.\n"
"This category is often\n"
"used in combination with\n"
"other attack categories.", None))
#endif // QT_CONFIG(tooltip)
        self.exploited_host_info.setText("")
#if QT_CONFIG(tooltip)
        self.hacking_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Unauthorized access to or\n"
"control over computer systems\n"
"or networks,\n"
"often with malicious intent,\n"
"to steal, modify, or disrupt data.", None))
#endif // QT_CONFIG(tooltip)
        self.hacking_info.setText("")
#if QT_CONFIG(tooltip)
        self.sql_injection_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Attempts at SQL\n"
"injection.", None))
#endif // QT_CONFIG(tooltip)
        self.sql_injection_info.setText("")
#if QT_CONFIG(tooltip)
        self.brute_force_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Credential brute-force attacks\n"
"on webpage logins and\n"
"services like SSH, FTP, SIP,\n"
"SMTP, RDP, etc. This\n"
"category is seperate from\n"
"DDoS attacks. ", None))
#endif // QT_CONFIG(tooltip)
        self.brute_force_info.setText("")
#if QT_CONFIG(tooltip)
        self.bad_web_bot_info.setToolTip(QCoreApplication.translate("report_Dialog", u"Webpage scraping (for\n"
"email addresses, content,\n"
"etc) and crawlers that do\n"
"not honor robots.txt.\n"
"Excessive requests and\n"
"user agent spoofing can\n"
"also be reported here. ", None))
#endif // QT_CONFIG(tooltip)
        self.bad_web_bot_info.setText("")
        self.star.setText(QCoreApplication.translate("report_Dialog", u"*", None))
        self.star_2.setText(QCoreApplication.translate("report_Dialog", u"*", None))
    # retranslateUi

