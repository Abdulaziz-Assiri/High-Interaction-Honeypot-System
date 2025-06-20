# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_User_Interface.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QStackedWidget, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1113)
        self.sidebar = QWidget(Form)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setGeometry(QRect(0, 0, 335, 1120))
        self.sidebar.setStyleSheet(u"background: #404142;\n"
"")
        self.logo_icon = QLabel(self.sidebar)
        self.logo_icon.setObjectName(u"logo_icon")
        self.logo_icon.setGeometry(QRect(5, 10, 96, 82))
        self.logo_icon.setPixmap(QPixmap(u"icons/logo.jpeg"))
        self.logo_icon.setScaledContents(True)
        self.project_title = QLabel(self.sidebar)
        self.project_title.setObjectName(u"project_title")
        self.project_title.setGeometry(QRect(110, 30, 201, 61))
        font = QFont()
        font.setFamilies([u"MathJax_Main"])
        font.setPointSize(36)
        self.project_title.setFont(font)
        self.project_title.setStyleSheet(u"color: #F8F8F8;")
        self.first_line = QFrame(self.sidebar)
        self.first_line.setObjectName(u"first_line")
        self.first_line.setGeometry(QRect(0, 100, 335, 16))
        self.first_line.setFrameShape(QFrame.Shape.HLine)
        self.first_line.setFrameShadow(QFrame.Shadow.Sunken)
        self.dashboard_button = QPushButton(self.sidebar)
        self.dashboard_button.setObjectName(u"dashboard_button")
        self.dashboard_button.setGeometry(QRect(0, 190, 335, 40))
        font1 = QFont()
        font1.setFamilies([u"MathJax_Main"])
        font1.setPointSize(18)
        self.dashboard_button.setFont(font1)
        self.dashboard_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dashboard_button.setStyleSheet(u"QPushButton {\n"
"background: #404142;\n"
"color: #F8F8F8;\n"
"text-align: left;\n"
"padding-left: 10px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #2BCC6C;\n"
"}\n"
"QPushButton:checked { \n"
"background: #30BD69; \n"
"}\n"
"QPushButton:disabled {\n"
"background: #FFFFFF;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"icons/dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dashboard_button.setIcon(icon)
        self.dashboard_button.setIconSize(QSize(36, 36))
        self.dashboard_button.setCheckable(True)
        self.dashboard_button.setAutoRepeat(False)
        self.dashboard_button.setAutoExclusive(True)
        self.dashboard_button.setFlat(True)
        self.capture_evidence_button = QPushButton(self.sidebar)
        self.capture_evidence_button.setObjectName(u"capture_evidence_button")
        self.capture_evidence_button.setGeometry(QRect(0, 610, 335, 40))
        self.capture_evidence_button.setFont(font1)
        self.capture_evidence_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.capture_evidence_button.setStyleSheet(u"QPushButton {\n"
"background: #404142;\n"
"color: #F8F8F8;\n"
"text-align: left;\n"
"padding-left: 10px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #2BCC6C;\n"
"}\n"
"QPushButton:checked { \n"
"background: #30BD69; \n"
"}\n"
"QPushButton:disabled {\n"
"background: #FFFFFF;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/capture evidence.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.capture_evidence_button.setIcon(icon1)
        self.capture_evidence_button.setIconSize(QSize(36, 36))
        self.capture_evidence_button.setCheckable(True)
        self.capture_evidence_button.setAutoExclusive(True)
        self.capture_evidence_button.setFlat(True)
        self.network_monitor_button = QPushButton(self.sidebar)
        self.network_monitor_button.setObjectName(u"network_monitor_button")
        self.network_monitor_button.setGeometry(QRect(0, 250, 335, 40))
        self.network_monitor_button.setFont(font1)
        self.network_monitor_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.network_monitor_button.setStyleSheet(u"QPushButton {\n"
"background: #404142;\n"
"color: #F8F8F8;\n"
"text-align: left;\n"
"padding-left: 10px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #2BCC6C;\n"
"}\n"
"QPushButton:checked { \n"
"background: #30BD69; \n"
"}\n"
"QPushButton:disabled {\n"
"background: #FFFFFF;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"icons/wifi.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.network_monitor_button.setIcon(icon2)
        self.network_monitor_button.setIconSize(QSize(36, 36))
        self.network_monitor_button.setCheckable(True)
        self.network_monitor_button.setAutoExclusive(True)
        self.network_monitor_button.setFlat(True)
        self.firewall_setting_button = QPushButton(self.sidebar)
        self.firewall_setting_button.setObjectName(u"firewall_setting_button")
        self.firewall_setting_button.setGeometry(QRect(0, 310, 335, 40))
        self.firewall_setting_button.setFont(font1)
        self.firewall_setting_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.firewall_setting_button.setStyleSheet(u"QPushButton {\n"
"background: #404142;\n"
"color: #F8F8F8;\n"
"text-align: left;\n"
"padding-left: 10px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #2BCC6C;\n"
"}\n"
"QPushButton:checked { \n"
"background: #30BD69; \n"
"}\n"
"QPushButton:disabled {\n"
"background: #FFFFFF;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/firewall.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.firewall_setting_button.setIcon(icon3)
        self.firewall_setting_button.setIconSize(QSize(36, 36))
        self.firewall_setting_button.setCheckable(True)
        self.firewall_setting_button.setAutoExclusive(True)
        self.firewall_setting_button.setFlat(True)
        self.database_health_button = QPushButton(self.sidebar)
        self.database_health_button.setObjectName(u"database_health_button")
        self.database_health_button.setGeometry(QRect(0, 370, 335, 40))
        self.database_health_button.setFont(font1)
        self.database_health_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.database_health_button.setStyleSheet(u"QPushButton {\n"
"background: #404142;\n"
"color: #F8F8F8;\n"
"text-align: left;\n"
"padding-left: 10px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #2BCC6C;\n"
"}\n"
"QPushButton:checked { \n"
"background: #30BD69; \n"
"}\n"
"QPushButton:disabled {\n"
"background: #FFFFFF;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/database.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.database_health_button.setIcon(icon4)
        self.database_health_button.setIconSize(QSize(36, 36))
        self.database_health_button.setCheckable(True)
        self.database_health_button.setAutoExclusive(True)
        self.database_health_button.setFlat(True)
        self.remote_shell_button = QPushButton(self.sidebar)
        self.remote_shell_button.setObjectName(u"remote_shell_button")
        self.remote_shell_button.setGeometry(QRect(0, 430, 335, 40))
        self.remote_shell_button.setFont(font1)
        self.remote_shell_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.remote_shell_button.setStyleSheet(u"QPushButton {\n"
"background: #404142;\n"
"color: #F8F8F8;\n"
"text-align: left;\n"
"padding-left: 10px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #2BCC6C;\n"
"}\n"
"QPushButton:checked { \n"
"background: #30BD69; \n"
"}\n"
"QPushButton:disabled {\n"
"background: #FFFFFF;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/remote shell.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.remote_shell_button.setIcon(icon5)
        self.remote_shell_button.setIconSize(QSize(36, 36))
        self.remote_shell_button.setCheckable(True)
        self.remote_shell_button.setAutoExclusive(True)
        self.remote_shell_button.setFlat(True)
        self.file_security_button = QPushButton(self.sidebar)
        self.file_security_button.setObjectName(u"file_security_button")
        self.file_security_button.setGeometry(QRect(0, 490, 335, 40))
        self.file_security_button.setFont(font1)
        self.file_security_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.file_security_button.setStyleSheet(u"QPushButton {\n"
"background: #404142;\n"
"color: #F8F8F8;\n"
"text-align: left;\n"
"padding-left: 10px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #2BCC6C;\n"
"}\n"
"QPushButton:checked { \n"
"background: #30BD69; \n"
"}\n"
"QPushButton:disabled {\n"
"background: #FFFFFF;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/file security.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.file_security_button.setIcon(icon6)
        self.file_security_button.setIconSize(QSize(36, 36))
        self.file_security_button.setCheckable(True)
        self.file_security_button.setAutoExclusive(True)
        self.file_security_button.setFlat(True)
        self.ip_investigator_button = QPushButton(self.sidebar)
        self.ip_investigator_button.setObjectName(u"ip_investigator_button")
        self.ip_investigator_button.setGeometry(QRect(0, 550, 335, 40))
        self.ip_investigator_button.setFont(font1)
        self.ip_investigator_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ip_investigator_button.setStyleSheet(u"QPushButton {\n"
"background: #404142;\n"
"color: #F8F8F8;\n"
"text-align: left;\n"
"padding-left: 10px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #2BCC6C;\n"
"}\n"
"QPushButton:checked { \n"
"background: #30BD69; \n"
"}\n"
"QPushButton:disabled {\n"
"background: #FFFFFF;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/ip investigator.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ip_investigator_button.setIcon(icon7)
        self.ip_investigator_button.setIconSize(QSize(36, 36))
        self.ip_investigator_button.setCheckable(True)
        self.ip_investigator_button.setAutoExclusive(True)
        self.ip_investigator_button.setFlat(True)
        self.logout_button = QPushButton(self.sidebar)
        self.logout_button.setObjectName(u"logout_button")
        self.logout_button.setGeometry(QRect(0, 1030, 335, 40))
        self.logout_button.setFont(font1)
        self.logout_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logout_button.setStyleSheet(u"QPushButton {\n"
"background: #404142;\n"
"color: #F8F8F8;\n"
"text-align: left;\n"
"padding-left: 10px;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"icons/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logout_button.setIcon(icon8)
        self.logout_button.setIconSize(QSize(36, 36))
        self.logout_button.setCheckable(True)
        self.logout_button.setAutoExclusive(True)
        self.logout_button.setFlat(True)
        self.welcome_button = QPushButton(self.sidebar)
        self.welcome_button.setObjectName(u"welcome_button")
        self.welcome_button.setGeometry(QRect(0, 130, 335, 40))
        self.welcome_button.setFont(font1)
        self.welcome_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.welcome_button.setStyleSheet(u"QPushButton {\n"
"background: #404142;\n"
"color: #F8F8F8;\n"
"text-align: left;\n"
"padding-left: 10px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #2BCC6C;\n"
"}\n"
"QPushButton:checked { \n"
"background: #30BD69; \n"
"}\n"
"QPushButton:disabled {\n"
"background: #FFFFFF;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.welcome_button.setIcon(icon9)
        self.welcome_button.setIconSize(QSize(36, 36))
        self.welcome_button.setCheckable(True)
        self.welcome_button.setAutoExclusive(True)
        self.welcome_button.setAutoDefault(False)
        self.welcome_button.setFlat(True)
        self.second_line = QFrame(self.sidebar)
        self.second_line.setObjectName(u"second_line")
        self.second_line.setGeometry(QRect(0, 175, 335, 16))
        self.second_line.setFrameShape(QFrame.Shape.HLine)
        self.second_line.setFrameShadow(QFrame.Shadow.Sunken)
        self.third_line = QFrame(self.sidebar)
        self.third_line.setObjectName(u"third_line")
        self.third_line.setGeometry(QRect(0, 230, 335, 16))
        self.third_line.setFrameShape(QFrame.Shape.HLine)
        self.third_line.setFrameShadow(QFrame.Shadow.Sunken)
        self.forth_line = QFrame(self.sidebar)
        self.forth_line.setObjectName(u"forth_line")
        self.forth_line.setGeometry(QRect(0, 355, 335, 16))
        self.forth_line.setFrameShape(QFrame.Shape.HLine)
        self.forth_line.setFrameShadow(QFrame.Shadow.Sunken)
        self.fifth_line = QFrame(self.sidebar)
        self.fifth_line.setObjectName(u"fifth_line")
        self.fifth_line.setGeometry(QRect(0, 535, 335, 16))
        self.fifth_line.setFrameShape(QFrame.Shape.HLine)
        self.fifth_line.setFrameShadow(QFrame.Shadow.Sunken)
        self.logo_icon.raise_()
        self.project_title.raise_()
        self.first_line.raise_()
        self.second_line.raise_()
        self.third_line.raise_()
        self.forth_line.raise_()
        self.fifth_line.raise_()
        self.welcome_button.raise_()
        self.dashboard_button.raise_()
        self.network_monitor_button.raise_()
        self.firewall_setting_button.raise_()
        self.database_health_button.raise_()
        self.remote_shell_button.raise_()
        self.file_security_button.raise_()
        self.ip_investigator_button.raise_()
        self.capture_evidence_button.raise_()
        self.logout_button.raise_()
        self.workstation = QStackedWidget(Form)
        self.workstation.setObjectName(u"workstation")
        self.workstation.setGeometry(QRect(336, 0, 1585, 1111))
        font2 = QFont()
        font2.setFamilies([u"MathJax_Main"])
        self.workstation.setFont(font2)
        self.workstation.setToolTipDuration(2)
        self.workstation.setStyleSheet(u"background: #1F1F1F;\n"
"color: #FFFFFF;")
        self.welcome_page = QWidget()
        self.welcome_page.setObjectName(u"welcome_page")
        self.welcome_title = QLabel(self.welcome_page)
        self.welcome_title.setObjectName(u"welcome_title")
        self.welcome_title.setGeometry(QRect(0, 0, 1585, 121))
        font3 = QFont()
        font3.setFamilies([u"MathJax_Main"])
        font3.setPointSize(58)
        self.welcome_title.setFont(font3)
        self.welcome_title.setStyleSheet(u"color: #30BD69;\n"
"border-bottom: 0.5px solid #FFFFFF;\n"
"padding: 20px;")
        self.introduction_label = QLabel(self.welcome_page)
        self.introduction_label.setObjectName(u"introduction_label")
        self.introduction_label.setGeometry(QRect(160, 290, 1236, 144))
        font4 = QFont()
        font4.setFamilies([u"MathJax_Main"])
        font4.setPointSize(38)
        self.introduction_label.setFont(font4)
        self.introduction_label.setStyleSheet(u"color: #AEAEAE;")
        self.get_started_button = QPushButton(self.welcome_page)
        self.get_started_button.setObjectName(u"get_started_button")
        self.get_started_button.setGeometry(QRect(160, 540, 259, 60))
        font5 = QFont()
        font5.setFamilies([u"MathJax_Main"])
        font5.setPointSize(22)
        self.get_started_button.setFont(font5)
        self.get_started_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.get_started_button.setStyleSheet(u"QPushButton{\n"
"color: #FFFFFF;\n"
"background: #30BD69;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #279A51;\n"
"}")
        self.workstation.addWidget(self.welcome_page)
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.dashboard_title = QLabel(self.dashboard_page)
        self.dashboard_title.setObjectName(u"dashboard_title")
        self.dashboard_title.setGeometry(QRect(0, 0, 1585, 121))
        self.dashboard_title.setFont(font3)
        self.dashboard_title.setStyleSheet(u"color: #30BD69;\n"
"border-bottom: 0.5px solid #FFFFFF;\n"
"padding: 20px;")
        self.connections_output_field = QTextEdit(self.dashboard_page)
        self.connections_output_field.setObjectName(u"connections_output_field")
        self.connections_output_field.setGeometry(QRect(30, 150, 721, 391))
        self.connections_output_field.setFont(font1)
        self.connections_output_field.setToolTipDuration(2)
        self.connections_output_field.setStyleSheet(u"color: #F8F8F8;\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"padding-top: 50px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"padding-bottom: 20px;")
        self.connections_output_field.setReadOnly(True)
        self.connections_text = QLabel(self.dashboard_page)
        self.connections_text.setObjectName(u"connections_text")
        self.connections_text.setGeometry(QRect(55, 170, 141, 21))
        self.connections_text.setFont(font1)
        self.connections_text.setStyleSheet(u"background: #404040;\n"
"")
        self.unique_detected_traffic_text = QLabel(self.dashboard_page)
        self.unique_detected_traffic_text.setObjectName(u"unique_detected_traffic_text")
        self.unique_detected_traffic_text.setGeometry(QRect(815, 162, 261, 31))
        self.unique_detected_traffic_text.setFont(font1)
        self.unique_detected_traffic_text.setStyleSheet(u"background: #404040;\n"
"")
        self.unique_detected_traffic_field = QTextEdit(self.dashboard_page)
        self.unique_detected_traffic_field.setObjectName(u"unique_detected_traffic_field")
        self.unique_detected_traffic_field.setGeometry(QRect(790, 150, 721, 271))
        self.unique_detected_traffic_field.setFont(font1)
        self.unique_detected_traffic_field.setToolTipDuration(2)
        self.unique_detected_traffic_field.setStyleSheet(u"color: #F8F8F8;\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"padding-top: 50px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"padding-bottom: 20px;")
        self.unique_detected_traffic_field.setReadOnly(True)
        self.top_attacking_ips_field = QTextEdit(self.dashboard_page)
        self.top_attacking_ips_field.setObjectName(u"top_attacking_ips_field")
        self.top_attacking_ips_field.setGeometry(QRect(785, 570, 721, 521))
        self.top_attacking_ips_field.setFont(font1)
        self.top_attacking_ips_field.setToolTipDuration(2)
        self.top_attacking_ips_field.setStyleSheet(u"color: #F8F8F8;\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"padding-top: 50px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"padding-bottom: 20px;")
        self.top_attacking_ips_field.setReadOnly(True)
        self.top_attacking_ips_text = QLabel(self.dashboard_page)
        self.top_attacking_ips_text.setObjectName(u"top_attacking_ips_text")
        self.top_attacking_ips_text.setGeometry(QRect(810, 590, 461, 31))
        self.top_attacking_ips_text.setFont(font1)
        self.top_attacking_ips_text.setStyleSheet(u"background: #404040;\n"
"")
        self.opened_ports_field = QTextEdit(self.dashboard_page)
        self.opened_ports_field.setObjectName(u"opened_ports_field")
        self.opened_ports_field.setGeometry(QRect(30, 570, 721, 521))
        self.opened_ports_field.setFont(font1)
        self.opened_ports_field.setToolTipDuration(2)
        self.opened_ports_field.setStyleSheet(u"color: #F8F8F8;\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"padding-top: 50px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"padding-bottom: 20px;")
        self.opened_ports_field.setReadOnly(True)
        self.opened_ports_text = QLabel(self.dashboard_page)
        self.opened_ports_text.setObjectName(u"opened_ports_text")
        self.opened_ports_text.setGeometry(QRect(50, 590, 491, 31))
        self.opened_ports_text.setFont(font1)
        self.opened_ports_text.setStyleSheet(u"background: #404040;\n"
"")
        self.protocol_type_text = QLabel(self.dashboard_page)
        self.protocol_type_text.setObjectName(u"protocol_type_text")
        self.protocol_type_text.setGeometry(QRect(810, 450, 161, 31))
        self.protocol_type_text.setFont(font1)
        self.protocol_type_text.setStyleSheet(u"background: #404040;\n"
"")
        self.protocol_type_field = QTextEdit(self.dashboard_page)
        self.protocol_type_field.setObjectName(u"protocol_type_field")
        self.protocol_type_field.setGeometry(QRect(790, 440, 721, 111))
        self.protocol_type_field.setFont(font1)
        self.protocol_type_field.setToolTipDuration(2)
        self.protocol_type_field.setStyleSheet(u"color: #F8F8F8;\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"padding-top: 50px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"padding-bottom: 20px;")
        self.protocol_type_field.setReadOnly(True)
        self.workstation.addWidget(self.dashboard_page)
        self.dashboard_title.raise_()
        self.connections_output_field.raise_()
        self.connections_text.raise_()
        self.unique_detected_traffic_field.raise_()
        self.unique_detected_traffic_text.raise_()
        self.top_attacking_ips_field.raise_()
        self.top_attacking_ips_text.raise_()
        self.opened_ports_field.raise_()
        self.opened_ports_text.raise_()
        self.protocol_type_field.raise_()
        self.protocol_type_text.raise_()
        self.network_monitor_page = QWidget()
        self.network_monitor_page.setObjectName(u"network_monitor_page")
        self.network_monitor_title = QLabel(self.network_monitor_page)
        self.network_monitor_title.setObjectName(u"network_monitor_title")
        self.network_monitor_title.setGeometry(QRect(0, 0, 1585, 121))
        self.network_monitor_title.setFont(font3)
        self.network_monitor_title.setStyleSheet(u"color: #30BD69;\n"
"border-bottom: 0.5px solid #FFFFFF;\n"
"padding: 20px;")
        self.start_button = QPushButton(self.network_monitor_page)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(100, 220, 75, 75))
        self.start_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.start_button.setToolTipDuration(-1)
        self.start_button.setStyleSheet(u"QPushButton{\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #606060;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"icons/start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_button.setIcon(icon10)
        self.start_button.setIconSize(QSize(40, 40))
        self.output_field = QTextEdit(self.network_monitor_page)
        self.output_field.setObjectName(u"output_field")
        self.output_field.setGeometry(QRect(100, 320, 1360, 675))
        font6 = QFont()
        font6.setFamilies([u"MathJax_Main"])
        font6.setPointSize(25)
        self.output_field.setFont(font6)
        self.output_field.setToolTipDuration(2)
        self.output_field.setStyleSheet(u"color: #F8F8F8;\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"padding: 20px;")
        self.output_field.setReadOnly(True)
        self.download_button = QPushButton(self.network_monitor_page)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setGeometry(QRect(100, 1020, 300, 65))
        self.download_button.setFont(font5)
        self.download_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.download_button.setStyleSheet(u"QPushButton{\n"
"color: #F8F8F8;\n"
"border-radius: 10px;\n"
"background: #404040;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #606060;\n"
"}")
        self.download_button.setIconSize(QSize(50, 50))
        self.download_icon = QLabel(self.network_monitor_page)
        self.download_icon.setObjectName(u"download_icon")
        self.download_icon.setGeometry(QRect(110, 1030, 45, 45))
        self.download_icon.setStyleSheet(u"background: #404040;\n"
"")
        self.download_icon.setPixmap(QPixmap(u"icons/download.png"))
        self.download_icon.setScaledContents(True)
        self.duration_label = QLabel(self.network_monitor_page)
        self.duration_label.setObjectName(u"duration_label")
        self.duration_label.setGeometry(QRect(840, 240, 151, 31))
        font7 = QFont()
        font7.setFamilies([u"MathJax_Main"])
        font7.setPointSize(26)
        self.duration_label.setFont(font7)
        self.duration_time_field = QLineEdit(self.network_monitor_page)
        self.duration_time_field.setObjectName(u"duration_time_field")
        self.duration_time_field.setGeometry(QRect(1010, 230, 291, 60))
        font8 = QFont()
        font8.setFamilies([u"MathJax_Main"])
        font8.setPointSize(20)
        self.duration_time_field.setFont(font8)
        self.duration_time_field.setStyleSheet(u"border: 0px;\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"color: #FFFFFF;")
        self.interface_field = QLineEdit(self.network_monitor_page)
        self.interface_field.setObjectName(u"interface_field")
        self.interface_field.setGeometry(QRect(410, 230, 291, 60))
        self.interface_field.setFont(font8)
        self.interface_field.setStyleSheet(u"border: 0px;\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"color: #FFFFFF;")
        self.interface_label = QLabel(self.network_monitor_page)
        self.interface_label.setObjectName(u"interface_label")
        self.interface_label.setGeometry(QRect(240, 240, 151, 31))
        self.interface_label.setFont(font7)
        self.star = QLabel(self.network_monitor_page)
        self.star.setObjectName(u"star")
        self.star.setGeometry(QRect(390, 230, 16, 16))
        font9 = QFont()
        font9.setPointSize(16)
        self.star.setFont(font9)
        self.star.setStyleSheet(u"color: #FF0000;")
        self.workstation.addWidget(self.network_monitor_page)
        self.firewall_setting_page = QWidget()
        self.firewall_setting_page.setObjectName(u"firewall_setting_page")
        self.firewall_setting_title = QLabel(self.firewall_setting_page)
        self.firewall_setting_title.setObjectName(u"firewall_setting_title")
        self.firewall_setting_title.setGeometry(QRect(0, 0, 1585, 121))
        self.firewall_setting_title.setFont(font3)
        self.firewall_setting_title.setStyleSheet(u"color: #30BD69;\n"
"border-bottom: 0.5px solid #FFFFFF;\n"
"padding: 20px;")
        self.status_label = QLabel(self.firewall_setting_page)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(90, 200, 111, 31))
        self.status_label.setFont(font7)
        self.horizontalLayoutWidget = QWidget(self.firewall_setting_page)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(230, 200, 551, 42))
        self.status_button_layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.status_button_layout.setSpacing(0)
        self.status_button_layout.setObjectName(u"status_button_layout")
        self.status_button_layout.setContentsMargins(0, 0, 0, 0)
        self.enable_button = QPushButton(self.horizontalLayoutWidget)
        self.firewall_status_button_group = QButtonGroup(Form)
        self.firewall_status_button_group.setObjectName(u"firewall_status_button_group")
        self.firewall_status_button_group.addButton(self.enable_button)
        self.enable_button.setObjectName(u"enable_button")
        self.enable_button.setFont(font8)
        self.enable_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.enable_button.setStyleSheet(u"QPushButton{\n"
"background: #404040;\n"
"}\n"
"QPushButton:checked { \n"
"background: #30BD69; \n"
"}\n"
"QPushButton:disabled {\n"
"background: #FFFFFF;\n"
"}\n"
"QPushButton:pressed{\n"
"background: #279A51;\n"
"}")
        self.enable_button.setCheckable(True)
        self.enable_button.setChecked(True)
        self.enable_button.setAutoDefault(False)
        self.enable_button.setFlat(False)

        self.status_button_layout.addWidget(self.enable_button)

        self.disable_button = QPushButton(self.horizontalLayoutWidget)
        self.firewall_status_button_group.addButton(self.disable_button)
        self.disable_button.setObjectName(u"disable_button")
        self.disable_button.setFont(font8)
        self.disable_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.disable_button.setStyleSheet(u"QPushButton{\n"
"background: #404040;\n"
"}\n"
"QPushButton:checked { /* For checkable buttons */\n"
"background-color: #30BD69; /* Green when checked */\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #FFFFFF;\n"
"}\n"
"QPushButton:pressed{\n"
"background: #279A51;\n"
"}")
        self.disable_button.setCheckable(True)
        self.disable_button.setFlat(False)

        self.status_button_layout.addWidget(self.disable_button)

        self.reload_button = QPushButton(self.horizontalLayoutWidget)
        self.firewall_status_button_group.addButton(self.reload_button)
        self.reload_button.setObjectName(u"reload_button")
        self.reload_button.setFont(font8)
        self.reload_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reload_button.setStyleSheet(u"QPushButton{\n"
"background: #404040;\n"
"}\n"
"QPushButton:checked { /* For checkable buttons */\n"
"background-color: #30BD69; /* Green when checked */\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #FFFFFF;\n"
"}\n"
"QPushButton:pressed{\n"
"background: #279A51;\n"
"}")
        self.reload_button.setCheckable(True)
        self.reload_button.setChecked(False)

        self.status_button_layout.addWidget(self.reload_button)

        self.current_rules_label = QLabel(self.firewall_setting_page)
        self.current_rules_label.setObjectName(u"current_rules_label")
        self.current_rules_label.setGeometry(QRect(90, 310, 231, 31))
        self.current_rules_label.setFont(font7)
        self.add_button = QPushButton(self.firewall_setting_page)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(1080, 1040, 220, 50))
        self.add_button.setFont(font5)
        self.add_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_button.setStyleSheet(u"QPushButton \n"
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
        self.delete_button = QPushButton(self.firewall_setting_page)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(1330, 1040, 220, 50))
        self.delete_button.setFont(font5)
        self.delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #FF0707;\n"
"border-radius: 10px;\n"
"color: #FFFFFF; \n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #CC0505;\n"
"}\n"
"\n"
"")
        self.current_firewall_rules_field = QTextEdit(self.firewall_setting_page)
        self.current_firewall_rules_field.setObjectName(u"current_firewall_rules_field")
        self.current_firewall_rules_field.setGeometry(QRect(90, 365, 1460, 650))
        self.current_firewall_rules_field.setFont(font6)
        self.current_firewall_rules_field.setToolTipDuration(2)
        self.current_firewall_rules_field.setStyleSheet(u"color: #F8F8F8;\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"padding: 20px;")
        self.current_firewall_rules_field.setReadOnly(True)
        self.refresh_button = QPushButton(self.firewall_setting_page)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setGeometry(QRect(1470, 270, 75, 75))
        self.refresh_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.refresh_button.setToolTipDuration(-1)
        self.refresh_button.setStyleSheet(u"QPushButton{\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #616161;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"icons/refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refresh_button.setIcon(icon11)
        self.refresh_button.setIconSize(QSize(40, 40))
        self.workstation.addWidget(self.firewall_setting_page)
        self.database_health_page = QWidget()
        self.database_health_page.setObjectName(u"database_health_page")
        self.database_health_title = QLabel(self.database_health_page)
        self.database_health_title.setObjectName(u"database_health_title")
        self.database_health_title.setGeometry(QRect(0, 0, 1585, 121))
        self.database_health_title.setFont(font3)
        self.database_health_title.setStyleSheet(u"color: #30BD69;\n"
"border-bottom: 0.5px solid #FFFFFF;\n"
"padding: 20px;")
        self.path_label = QLabel(self.database_health_page)
        self.path_label.setObjectName(u"path_label")
        self.path_label.setGeometry(QRect(90, 200, 91, 31))
        self.path_label.setFont(font7)
        self.path_field = QLineEdit(self.database_health_page)
        self.path_field.setObjectName(u"path_field")
        self.path_field.setGeometry(QRect(215, 190, 1101, 60))
        self.path_field.setFont(font8)
        self.path_field.setStyleSheet(u"border: 0px;\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"color: #FFFFFF;")
        self.note_message_label = QLabel(self.database_health_page)
        self.note_message_label.setObjectName(u"note_message_label")
        self.note_message_label.setGeometry(QRect(90, 300, 1346, 123))
        self.note_message_label.setFont(font7)
        self.note_message_label.setStyleSheet(u"padding-left: 80px;\n"
"background: #AEAEAE;\n"
"border-radius: 10px;\n"
"color: #000000;")
        self.note_message_label.setWordWrap(True)
        self.warning_icon = QLabel(self.database_health_page)
        self.warning_icon.setObjectName(u"warning_icon")
        self.warning_icon.setGeometry(QRect(100, 305, 64, 64))
        self.warning_icon.setStyleSheet(u"background: #AEAEAE;")
        self.warning_icon.setPixmap(QPixmap(u"icons/Warning.png"))
        self.warning_icon.setScaledContents(True)
        self.check_button = QPushButton(self.database_health_page)
        self.check_button.setObjectName(u"check_button")
        self.check_button.setGeometry(QRect(1035, 1020, 180, 65))
        self.check_button.setFont(font5)
        self.check_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.check_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #30BD69;\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #279A51;\n"
"}\n"
"")
        self.add_hash_to_database_button = QPushButton(self.database_health_page)
        self.add_hash_to_database_button.setObjectName(u"add_hash_to_database_button")
        self.add_hash_to_database_button.setGeometry(QRect(1239, 1020, 180, 65))
        self.add_hash_to_database_button.setFont(font5)
        self.add_hash_to_database_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_hash_to_database_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #30BD69;\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #279A51;\n"
"}\n"
"")
        self.star_2 = QLabel(self.database_health_page)
        self.star_2.setObjectName(u"star_2")
        self.star_2.setGeometry(QRect(180, 190, 16, 16))
        self.star_2.setFont(font9)
        self.star_2.setStyleSheet(u"color: #FF0000;")
        self.workstation.addWidget(self.database_health_page)
        self.remote_shell_page = QWidget()
        self.remote_shell_page.setObjectName(u"remote_shell_page")
        self.remote_shell_title = QLabel(self.remote_shell_page)
        self.remote_shell_title.setObjectName(u"remote_shell_title")
        self.remote_shell_title.setGeometry(QRect(0, 0, 1585, 121))
        self.remote_shell_title.setFont(font3)
        self.remote_shell_title.setStyleSheet(u"color: #30BD69;\n"
"border-bottom: 0.5px solid #FFFFFF;\n"
"padding: 20px;")
        self.command_label = QLabel(self.remote_shell_page)
        self.command_label.setObjectName(u"command_label")
        self.command_label.setGeometry(QRect(90, 200, 171, 31))
        self.command_label.setFont(font7)
        self.command_field = QLineEdit(self.remote_shell_page)
        self.command_field.setObjectName(u"command_field")
        self.command_field.setGeometry(QRect(300, 190, 1111, 60))
        self.command_field.setFont(font8)
        self.command_field.setStyleSheet(u"border: 0px;\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"color: #FFFFFF;")
        self.output_label = QLabel(self.remote_shell_page)
        self.output_label.setObjectName(u"output_label")
        self.output_label.setGeometry(QRect(90, 275, 131, 41))
        self.output_label.setFont(font7)
        self.remote_shell_output_field = QTextEdit(self.remote_shell_page)
        self.remote_shell_output_field.setObjectName(u"remote_shell_output_field")
        self.remote_shell_output_field.setGeometry(QRect(90, 335, 1451, 670))
        self.remote_shell_output_field.setFont(font6)
        self.remote_shell_output_field.setStyleSheet(u"color: #F8F8F8;\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"padding: 20px;")
        self.remote_shell_output_field.setReadOnly(True)
        self.send_button = QPushButton(self.remote_shell_page)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setGeometry(QRect(1279, 1030, 260, 65))
        self.send_button.setFont(font5)
        self.send_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.send_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #616161;\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #424242;\n"
"}\n"
"")
        self.star_3 = QLabel(self.remote_shell_page)
        self.star_3.setObjectName(u"star_3")
        self.star_3.setGeometry(QRect(260, 190, 16, 16))
        self.star_3.setFont(font9)
        self.star_3.setStyleSheet(u"color: #FF0000;")
        self.connect_to_ssh_server_button = QPushButton(self.remote_shell_page)
        self.connect_to_ssh_server_button.setObjectName(u"connect_to_ssh_server_button")
        self.connect_to_ssh_server_button.setGeometry(QRect(670, 1030, 311, 65))
        self.connect_to_ssh_server_button.setFont(font5)
        self.connect_to_ssh_server_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.connect_to_ssh_server_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #30BD69;\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #279A51;\n"
"}\n"
"")
        self.close_ssh_connection_button = QPushButton(self.remote_shell_page)
        self.close_ssh_connection_button.setObjectName(u"close_ssh_connection_button")
        self.close_ssh_connection_button.setGeometry(QRect(1000, 1030, 260, 65))
        self.close_ssh_connection_button.setFont(font5)
        self.close_ssh_connection_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_ssh_connection_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #FF0707;\n"
"border-radius: 10px;\n"
"color: #FFFFFF; \n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #CC0505;\n"
"}\n"
"\n"
"")
        self.ssh_server_status = QLabel(self.remote_shell_page)
        self.ssh_server_status.setObjectName(u"ssh_server_status")
        self.ssh_server_status.setGeometry(QRect(1460, 195, 50, 50))
        self.ssh_server_status.setPixmap(QPixmap(u"icons/disconnected.png"))
        self.ssh_server_status.setScaledContents(True)
        self.workstation.addWidget(self.remote_shell_page)
        self.file_security_page = QWidget()
        self.file_security_page.setObjectName(u"file_security_page")
        self.file_security_title = QLabel(self.file_security_page)
        self.file_security_title.setObjectName(u"file_security_title")
        self.file_security_title.setGeometry(QRect(0, 0, 1585, 121))
        self.file_security_title.setFont(font3)
        self.file_security_title.setStyleSheet(u"color: #30BD69;\n"
"border-bottom: 0.5px solid #FFFFFF;\n"
"padding: 20px;")
        self.file_security_path_label = QLabel(self.file_security_page)
        self.file_security_path_label.setObjectName(u"file_security_path_label")
        self.file_security_path_label.setGeometry(QRect(90, 200, 91, 31))
        self.file_security_path_label.setFont(font7)
        self.file_security_path_field = QLineEdit(self.file_security_page)
        self.file_security_path_field.setObjectName(u"file_security_path_field")
        self.file_security_path_field.setGeometry(QRect(215, 190, 1101, 60))
        self.file_security_path_field.setFont(font8)
        self.file_security_path_field.setStyleSheet(u"border: 0px;\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"color: #FFFFFF;")
        self.upload_attributes_button = QPushButton(self.file_security_page)
        self.upload_attributes_button.setObjectName(u"upload_attributes_button")
        self.upload_attributes_button.setGeometry(QRect(1330, 190, 241, 65))
        self.upload_attributes_button.setFont(font5)
        self.upload_attributes_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.upload_attributes_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #30BD69;\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #279A51;\n"
"}\n"
"")
        self.upload_attributes_button.setIconSize(QSize(50, 50))
        self.apply_attributes_button = QPushButton(self.file_security_page)
        self.apply_attributes_button.setObjectName(u"apply_attributes_button")
        self.apply_attributes_button.setGeometry(QRect(1310, 1010, 241, 65))
        self.apply_attributes_button.setFont(font5)
        self.apply_attributes_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.apply_attributes_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #30BD69;\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #279A51;\n"
"}\n"
"")
        self.apply_attributes_button.setIconSize(QSize(50, 50))
        self.append_only_info = QLabel(self.file_security_page)
        self.append_only_info.setObjectName(u"append_only_info")
        self.append_only_info.setGeometry(QRect(280, 340, 31, 31))
        self.append_only_info.setToolTipDuration(-1)
        self.append_only_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.append_only_info.setScaledContents(True)
        self.append_only_checkbox = QCheckBox(self.file_security_page)
        self.append_only_checkbox.setObjectName(u"append_only_checkbox")
        self.append_only_checkbox.setGeometry(QRect(90, 340, 221, 31))
        self.append_only_checkbox.setFont(font8)
        self.append_only_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.append_only_checkbox.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 16px;\n"
"height: 16px;\n"
"border: 1px solid gray;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"background-color: #30BD69;\n"
"}")
        self.no_atime_updates_info = QLabel(self.file_security_page)
        self.no_atime_updates_info.setObjectName(u"no_atime_updates_info")
        self.no_atime_updates_info.setGeometry(QRect(340, 430, 31, 31))
        self.no_atime_updates_info.setToolTipDuration(-1)
        self.no_atime_updates_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.no_atime_updates_info.setScaledContents(True)
        self.no_atime_updates_checkbox = QCheckBox(self.file_security_page)
        self.no_atime_updates_checkbox.setObjectName(u"no_atime_updates_checkbox")
        self.no_atime_updates_checkbox.setGeometry(QRect(90, 430, 281, 31))
        self.no_atime_updates_checkbox.setFont(font8)
        self.no_atime_updates_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.no_atime_updates_checkbox.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 16px;\n"
"height: 16px;\n"
"border: 1px solid gray;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"background-color: #30BD69;\n"
"}")
        self.compressed_info = QLabel(self.file_security_page)
        self.compressed_info.setObjectName(u"compressed_info")
        self.compressed_info.setGeometry(QRect(270, 520, 31, 31))
        self.compressed_info.setToolTipDuration(-1)
        self.compressed_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.compressed_info.setScaledContents(True)
        self.compressed_checkbox = QCheckBox(self.file_security_page)
        self.compressed_checkbox.setObjectName(u"compressed_checkbox")
        self.compressed_checkbox.setGeometry(QRect(90, 520, 211, 31))
        self.compressed_checkbox.setFont(font8)
        self.compressed_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.compressed_checkbox.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 16px;\n"
"height: 16px;\n"
"border: 1px solid gray;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"background-color: #30BD69;\n"
"}")
        self.undeletable_info = QLabel(self.file_security_page)
        self.undeletable_info.setObjectName(u"undeletable_info")
        self.undeletable_info.setGeometry(QRect(730, 340, 31, 31))
        self.undeletable_info.setToolTipDuration(-1)
        self.undeletable_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.undeletable_info.setScaledContents(True)
        self.undeletable_checkbox = QCheckBox(self.file_security_page)
        self.undeletable_checkbox.setObjectName(u"undeletable_checkbox")
        self.undeletable_checkbox.setGeometry(QRect(550, 340, 211, 31))
        self.undeletable_checkbox.setFont(font8)
        self.undeletable_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.undeletable_checkbox.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 16px;\n"
"height: 16px;\n"
"border: 1px solid gray;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"background-color: #30BD69;\n"
"}")
        self.no_dump_info = QLabel(self.file_security_page)
        self.no_dump_info.setObjectName(u"no_dump_info")
        self.no_dump_info.setGeometry(QRect(710, 430, 31, 31))
        self.no_dump_info.setToolTipDuration(-1)
        self.no_dump_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.no_dump_info.setScaledContents(True)
        self.no_dump_checkbox = QCheckBox(self.file_security_page)
        self.no_dump_checkbox.setObjectName(u"no_dump_checkbox")
        self.no_dump_checkbox.setGeometry(QRect(550, 430, 191, 31))
        self.no_dump_checkbox.setFont(font8)
        self.no_dump_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.no_dump_checkbox.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 16px;\n"
"height: 16px;\n"
"border: 1px solid gray;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"background-color: #30BD69;\n"
"}")
        self.do_not_compress_info = QLabel(self.file_security_page)
        self.do_not_compress_info.setObjectName(u"do_not_compress_info")
        self.do_not_compress_info.setGeometry(QRect(780, 520, 31, 31))
        self.do_not_compress_info.setToolTipDuration(-1)
        self.do_not_compress_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.do_not_compress_info.setScaledContents(True)
        self.do_not_compress_checkbox = QCheckBox(self.file_security_page)
        self.do_not_compress_checkbox.setObjectName(u"do_not_compress_checkbox")
        self.do_not_compress_checkbox.setGeometry(QRect(550, 520, 261, 31))
        self.do_not_compress_checkbox.setFont(font8)
        self.do_not_compress_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.do_not_compress_checkbox.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 16px;\n"
"height: 16px;\n"
"border: 1px solid gray;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"background-color: #30BD69;\n"
"}")
        self.no_tail_merging_info = QLabel(self.file_security_page)
        self.no_tail_merging_info.setObjectName(u"no_tail_merging_info")
        self.no_tail_merging_info.setGeometry(QRect(1320, 340, 31, 31))
        self.no_tail_merging_info.setToolTipDuration(-1)
        self.no_tail_merging_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.no_tail_merging_info.setScaledContents(True)
        self.no_tail_merging_checkbox = QCheckBox(self.file_security_page)
        self.no_tail_merging_checkbox.setObjectName(u"no_tail_merging_checkbox")
        self.no_tail_merging_checkbox.setGeometry(QRect(1090, 340, 261, 31))
        self.no_tail_merging_checkbox.setFont(font8)
        self.no_tail_merging_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.no_tail_merging_checkbox.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 16px;\n"
"height: 16px;\n"
"border: 1px solid gray;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"background-color: #30BD69;\n"
"}")
        self.immutable_info = QLabel(self.file_security_page)
        self.immutable_info.setObjectName(u"immutable_info")
        self.immutable_info.setGeometry(QRect(1260, 430, 31, 31))
        self.immutable_info.setToolTipDuration(-1)
        self.immutable_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.immutable_info.setScaledContents(True)
        self.immutable_checkbox = QCheckBox(self.file_security_page)
        self.immutable_checkbox.setObjectName(u"immutable_checkbox")
        self.immutable_checkbox.setGeometry(QRect(1090, 430, 201, 31))
        self.immutable_checkbox.setFont(font8)
        self.immutable_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.immutable_checkbox.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 16px;\n"
"height: 16px;\n"
"border: 1px solid gray;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"background-color: #30BD69;\n"
"}")
        self.journaled_data_info = QLabel(self.file_security_page)
        self.journaled_data_info.setObjectName(u"journaled_data_info")
        self.journaled_data_info.setGeometry(QRect(1310, 520, 31, 31))
        self.journaled_data_info.setToolTipDuration(-1)
        self.journaled_data_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.journaled_data_info.setScaledContents(True)
        self.journaled_data_checkbox = QCheckBox(self.file_security_page)
        self.journaled_data_checkbox.setObjectName(u"journaled_data_checkbox")
        self.journaled_data_checkbox.setGeometry(QRect(1090, 520, 251, 31))
        self.journaled_data_checkbox.setFont(font8)
        self.journaled_data_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.journaled_data_checkbox.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 16px;\n"
"height: 16px;\n"
"border: 1px solid gray;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"background-color: #30BD69;\n"
"}")
        self.secure_deletion_checkbox = QCheckBox(self.file_security_page)
        self.secure_deletion_checkbox.setObjectName(u"secure_deletion_checkbox")
        self.secure_deletion_checkbox.setGeometry(QRect(90, 610, 251, 31))
        self.secure_deletion_checkbox.setFont(font8)
        self.secure_deletion_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.secure_deletion_checkbox.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 16px;\n"
"height: 16px;\n"
"border: 1px solid gray;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"background-color: #30BD69;\n"
"}")
        self.secure_deletion_info = QLabel(self.file_security_page)
        self.secure_deletion_info.setObjectName(u"secure_deletion_info")
        self.secure_deletion_info.setGeometry(QRect(310, 610, 31, 31))
        self.secure_deletion_info.setToolTipDuration(-1)
        self.secure_deletion_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.secure_deletion_info.setScaledContents(True)
        self.synchronous_updates_checkbox = QCheckBox(self.file_security_page)
        self.synchronous_updates_checkbox.setObjectName(u"synchronous_updates_checkbox")
        self.synchronous_updates_checkbox.setGeometry(QRect(550, 610, 321, 31))
        self.synchronous_updates_checkbox.setFont(font8)
        self.synchronous_updates_checkbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.synchronous_updates_checkbox.setStyleSheet(u"QCheckBox::indicator {\n"
"width: 16px;\n"
"height: 16px;\n"
"border: 1px solid gray;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"background-color: #30BD69;\n"
"}")
        self.synchronous_updates_info = QLabel(self.file_security_page)
        self.synchronous_updates_info.setObjectName(u"synchronous_updates_info")
        self.synchronous_updates_info.setGeometry(QRect(840, 610, 31, 31))
        self.synchronous_updates_info.setToolTipDuration(-1)
        self.synchronous_updates_info.setPixmap(QPixmap(u"icons/question_mark 1.png"))
        self.synchronous_updates_info.setScaledContents(True)
        self.star_4 = QLabel(self.file_security_page)
        self.star_4.setObjectName(u"star_4")
        self.star_4.setGeometry(QRect(180, 190, 16, 16))
        self.star_4.setFont(font9)
        self.star_4.setStyleSheet(u"color: #FF0000;")
        self.workstation.addWidget(self.file_security_page)
        self.file_security_title.raise_()
        self.file_security_path_label.raise_()
        self.file_security_path_field.raise_()
        self.upload_attributes_button.raise_()
        self.apply_attributes_button.raise_()
        self.append_only_checkbox.raise_()
        self.append_only_info.raise_()
        self.no_atime_updates_checkbox.raise_()
        self.compressed_checkbox.raise_()
        self.undeletable_checkbox.raise_()
        self.no_dump_checkbox.raise_()
        self.do_not_compress_checkbox.raise_()
        self.no_tail_merging_checkbox.raise_()
        self.immutable_checkbox.raise_()
        self.journaled_data_checkbox.raise_()
        self.no_atime_updates_info.raise_()
        self.compressed_info.raise_()
        self.no_dump_info.raise_()
        self.undeletable_info.raise_()
        self.do_not_compress_info.raise_()
        self.no_tail_merging_info.raise_()
        self.immutable_info.raise_()
        self.journaled_data_info.raise_()
        self.secure_deletion_checkbox.raise_()
        self.secure_deletion_info.raise_()
        self.synchronous_updates_checkbox.raise_()
        self.synchronous_updates_info.raise_()
        self.star_4.raise_()
        self.ip_investigator_page = QWidget()
        self.ip_investigator_page.setObjectName(u"ip_investigator_page")
        self.ip_inbestigator_title = QLabel(self.ip_investigator_page)
        self.ip_inbestigator_title.setObjectName(u"ip_inbestigator_title")
        self.ip_inbestigator_title.setGeometry(QRect(0, 0, 1585, 121))
        self.ip_inbestigator_title.setFont(font3)
        self.ip_inbestigator_title.setStyleSheet(u"color: #30BD69;\n"
"border-bottom: 0.5px solid #FFFFFF;\n"
"padding: 20px;")
        self.search_label = QLabel(self.ip_investigator_page)
        self.search_label.setObjectName(u"search_label")
        self.search_label.setGeometry(QRect(50, 160, 111, 51))
        self.search_label.setFont(font7)
        self.search_text_field = QLineEdit(self.ip_investigator_page)
        self.search_text_field.setObjectName(u"search_text_field")
        self.search_text_field.setGeometry(QRect(190, 150, 1101, 60))
        self.search_text_field.setFont(font8)
        self.search_text_field.setStyleSheet(u"border: 0px;\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"color: #FFFFFF;")
        self.search_output_textedit = QTextEdit(self.ip_investigator_page)
        self.search_output_textedit.setObjectName(u"search_output_textedit")
        self.search_output_textedit.setGeometry(QRect(40, 250, 1491, 711))
        self.search_output_textedit.setFont(font6)
        self.search_output_textedit.setStyleSheet(u"color: #F8F8F8;\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"padding: 20px;")
        self.search_output_textedit.setReadOnly(True)
        self.report_an_ip_button = QPushButton(self.ip_investigator_page)
        self.report_an_ip_button.setObjectName(u"report_an_ip_button")
        self.report_an_ip_button.setGeometry(QRect(340, 1010, 491, 65))
        self.report_an_ip_button.setFont(font5)
        self.report_an_ip_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.report_an_ip_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #FF8800;\n"
"border-radius: 10px;\n"
"color: #FFFFFF;\n"
" }\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #CC6600;\n"
"}\n"
"\n"
"")
        self.report_an_ip_button.setIconSize(QSize(50, 50))
        self.ip_address_search_button = QPushButton(self.ip_investigator_page)
        self.ip_address_search_button.setObjectName(u"ip_address_search_button")
        self.ip_address_search_button.setGeometry(QRect(40, 1010, 271, 65))
        self.ip_address_search_button.setFont(font5)
        self.ip_address_search_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ip_address_search_button.setStyleSheet(u"QPushButton \n"
"{\n"
"background: #30BD69;\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:pressed\n"
"{\n"
"background-color: #279A51;\n"
"}\n"
"")
        self.ip_address_search_button.setIconSize(QSize(50, 50))
        self.star_5 = QLabel(self.ip_investigator_page)
        self.star_5.setObjectName(u"star_5")
        self.star_5.setGeometry(QRect(170, 160, 16, 16))
        self.star_5.setFont(font9)
        self.star_5.setStyleSheet(u"color: #FF0000;")
        self.workstation.addWidget(self.ip_investigator_page)
        self.capture_evidence_page = QWidget()
        self.capture_evidence_page.setObjectName(u"capture_evidence_page")
        self.capture_evidence_title = QLabel(self.capture_evidence_page)
        self.capture_evidence_title.setObjectName(u"capture_evidence_title")
        self.capture_evidence_title.setGeometry(QRect(0, 0, 1585, 121))
        self.capture_evidence_title.setFont(font3)
        self.capture_evidence_title.setStyleSheet(u"color: #30BD69;\n"
"border-bottom: 0.5px solid #FFFFFF;\n"
"padding: 20px;")
        self.file_icon = QLabel(self.capture_evidence_page)
        self.file_icon.setObjectName(u"file_icon")
        self.file_icon.setGeometry(QRect(1060, 1000, 51, 51))
        self.file_icon.setStyleSheet(u"background: #404040;\n"
"")
        self.file_icon.setPixmap(QPixmap(u"icons/file.png"))
        self.file_icon.setScaledContents(True)
        self.generate_evidence_file_button = QPushButton(self.capture_evidence_page)
        self.generate_evidence_file_button.setObjectName(u"generate_evidence_file_button")
        self.generate_evidence_file_button.setGeometry(QRect(1040, 990, 491, 75))
        self.generate_evidence_file_button.setFont(font7)
        self.generate_evidence_file_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.generate_evidence_file_button.setStyleSheet(u"QPushButton{\n"
"color: #F8F8F8;\n"
"border-radius: 10px;\n"
"background: #404040;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"     background-color: #606060;\n"
"}")
        self.generate_evidence_file_button.setIconSize(QSize(50, 50))
        self.company_or_client_name_label = QLabel(self.capture_evidence_page)
        self.company_or_client_name_label.setObjectName(u"company_or_client_name_label")
        self.company_or_client_name_label.setGeometry(QRect(60, 200, 501, 51))
        self.company_or_client_name_label.setFont(font7)
        self.company_or_client_name_field = QLineEdit(self.capture_evidence_page)
        self.company_or_client_name_field.setObjectName(u"company_or_client_name_field")
        self.company_or_client_name_field.setGeometry(QRect(60, 280, 1101, 71))
        self.company_or_client_name_field.setFont(font8)
        self.company_or_client_name_field.setStyleSheet(u"border: 0px;\n"
"background: #404040;\n"
"border-radius: 10px;\n"
"padding: 15px;\n"
"color: #FFFFFF;")
        self.workstation.addWidget(self.capture_evidence_page)
        self.capture_evidence_title.raise_()
        self.generate_evidence_file_button.raise_()
        self.file_icon.raise_()
        self.company_or_client_name_label.raise_()
        self.company_or_client_name_field.raise_()

        self.retranslateUi(Form)

        self.dashboard_button.setDefault(False)
        self.welcome_button.setDefault(False)
        self.workstation.setCurrentIndex(3)
        self.enable_button.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logo_icon.setText("")
        self.project_title.setText(QCoreApplication.translate("Form", u"Honeypot", None))
        self.dashboard_button.setText(QCoreApplication.translate("Form", u"      Dashboard", None))
        self.capture_evidence_button.setText(QCoreApplication.translate("Form", u"      Capture Evidence", None))
        self.network_monitor_button.setText(QCoreApplication.translate("Form", u"      Network Monitor", None))
        self.firewall_setting_button.setText(QCoreApplication.translate("Form", u"      Firewall Management", None))
        self.database_health_button.setText(QCoreApplication.translate("Form", u"      File Integrity", None))
        self.remote_shell_button.setText(QCoreApplication.translate("Form", u"      Remote Shell", None))
        self.file_security_button.setText(QCoreApplication.translate("Form", u"      File Security", None))
        self.ip_investigator_button.setText(QCoreApplication.translate("Form", u"      IP Investigator", None))
        self.logout_button.setText(QCoreApplication.translate("Form", u"      Logout", None))
        self.welcome_button.setText(QCoreApplication.translate("Form", u"      Welcome", None))
        self.welcome_title.setText(QCoreApplication.translate("Form", u"Welcome", None))
        self.introduction_label.setText(QCoreApplication.translate("Form", u"Welcome to Honeypot panel,\n"
"Are you ready to explore cyber war threats?", None))
        self.get_started_button.setText(QCoreApplication.translate("Form", u"Get Started!", None))
        self.dashboard_title.setText(QCoreApplication.translate("Form", u"Dashboard", None))
#if QT_CONFIG(tooltip)
        self.connections_output_field.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.connections_output_field.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'MathJax_Main'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:25pt;\"><br /></p></body></html>", None))
        self.connections_text.setText(QCoreApplication.translate("Form", u"Connections:", None))
        self.unique_detected_traffic_text.setText(QCoreApplication.translate("Form", u"Unique Detected Traffic:", None))
#if QT_CONFIG(tooltip)
        self.unique_detected_traffic_field.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.unique_detected_traffic_field.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'MathJax_Main'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:25pt;\"><br /></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.top_attacking_ips_field.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.top_attacking_ips_field.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'MathJax_Main'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:25pt;\"><br /></p></body></html>", None))
        self.top_attacking_ips_text.setText(QCoreApplication.translate("Form", u"Top Attacking IPs (IP Address, Attempts):", None))
#if QT_CONFIG(tooltip)
        self.opened_ports_field.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.opened_ports_field.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'MathJax_Main'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:25pt;\"><br /></p></body></html>", None))
        self.opened_ports_text.setText(QCoreApplication.translate("Form", u"Opened Ports (Port number, Number of times):", None))
        self.protocol_type_text.setText(QCoreApplication.translate("Form", u"Protocol Type:", None))
#if QT_CONFIG(tooltip)
        self.protocol_type_field.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.protocol_type_field.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'MathJax_Main'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:25pt;\"><br /></p></body></html>", None))
        self.network_monitor_title.setText(QCoreApplication.translate("Form", u"Network Monitor", None))
#if QT_CONFIG(tooltip)
        self.start_button.setToolTip(QCoreApplication.translate("Form", u"Start", None))
#endif // QT_CONFIG(tooltip)
        self.start_button.setText("")
#if QT_CONFIG(tooltip)
        self.output_field.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.output_field.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'MathJax_Main'; font-size:25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.download_button.setText(QCoreApplication.translate("Form", u"Download", None))
        self.download_icon.setText("")
        self.duration_label.setText(QCoreApplication.translate("Form", u"Duration:", None))
        self.duration_time_field.setText("")
        self.duration_time_field.setPlaceholderText(QCoreApplication.translate("Form", u"10 Sec. by default", None))
        self.interface_field.setText("")
        self.interface_field.setPlaceholderText(QCoreApplication.translate("Form", u"eth0", None))
        self.interface_label.setText(QCoreApplication.translate("Form", u"Interface:", None))
        self.star.setText(QCoreApplication.translate("Form", u"*", None))
#if QT_CONFIG(tooltip)
        self.firewall_setting_title.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.firewall_setting_title.setText(QCoreApplication.translate("Form", u"Firewall Management", None))
        self.status_label.setText(QCoreApplication.translate("Form", u"Status:", None))
        self.enable_button.setText(QCoreApplication.translate("Form", u"Enable", None))
        self.disable_button.setText(QCoreApplication.translate("Form", u"Disable", None))
        self.reload_button.setText(QCoreApplication.translate("Form", u"Reload", None))
        self.current_rules_label.setText(QCoreApplication.translate("Form", u"Current Rules:", None))
        self.add_button.setText(QCoreApplication.translate("Form", u"Add", None))
        self.delete_button.setText(QCoreApplication.translate("Form", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.current_firewall_rules_field.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.current_firewall_rules_field.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'MathJax_Main'; font-size:25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.refresh_button.setToolTip(QCoreApplication.translate("Form", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.refresh_button.setText("")
        self.database_health_title.setText(QCoreApplication.translate("Form", u"File Integrity", None))
        self.path_label.setText(QCoreApplication.translate("Form", u"Path:", None))
        self.path_field.setText("")
        self.path_field.setPlaceholderText(QCoreApplication.translate("Form", u"Ex. : /home/user/file", None))
        self.note_message_label.setText(QCoreApplication.translate("Form", u"Note: To check file integrity, this feature must be used before any changes made to file.", None))
        self.warning_icon.setText("")
        self.check_button.setText(QCoreApplication.translate("Form", u"Check", None))
        self.add_hash_to_database_button.setText(QCoreApplication.translate("Form", u"Add", None))
        self.star_2.setText(QCoreApplication.translate("Form", u"*", None))
        self.remote_shell_title.setText(QCoreApplication.translate("Form", u"Remote Shell", None))
        self.command_label.setText(QCoreApplication.translate("Form", u"Command:", None))
        self.command_field.setText("")
        self.command_field.setPlaceholderText("")
        self.output_label.setText(QCoreApplication.translate("Form", u"Output:", None))
        self.send_button.setText(QCoreApplication.translate("Form", u"Send", None))
        self.star_3.setText(QCoreApplication.translate("Form", u"*", None))
        self.connect_to_ssh_server_button.setText(QCoreApplication.translate("Form", u"Connect to SSH Server", None))
        self.close_ssh_connection_button.setText(QCoreApplication.translate("Form", u"Close connection", None))
        self.ssh_server_status.setText("")
        self.file_security_title.setText(QCoreApplication.translate("Form", u"File Security", None))
        self.file_security_path_label.setText(QCoreApplication.translate("Form", u"Path:", None))
        self.file_security_path_field.setText("")
        self.file_security_path_field.setPlaceholderText(QCoreApplication.translate("Form", u"Ex. : /home/user/file", None))
        self.upload_attributes_button.setText(QCoreApplication.translate("Form", u"Upload Attributes", None))
        self.apply_attributes_button.setText(QCoreApplication.translate("Form", u"Apply Attributes", None))
#if QT_CONFIG(tooltip)
        self.append_only_info.setToolTip(QCoreApplication.translate("Form", u"Allows files to be opened in\n"
"append mode only.", None))
#endif // QT_CONFIG(tooltip)
        self.append_only_info.setText("")
        self.append_only_checkbox.setText(QCoreApplication.translate("Form", u"Append Only", None))
#if QT_CONFIG(tooltip)
        self.no_atime_updates_info.setToolTip(QCoreApplication.translate("Form", u"Prevents the access time\n"
"of a file from being\n"
"updated when it's accessed.", None))
#endif // QT_CONFIG(tooltip)
        self.no_atime_updates_info.setText("")
        self.no_atime_updates_checkbox.setText(QCoreApplication.translate("Form", u"No Atime Updates", None))
#if QT_CONFIG(tooltip)
        self.compressed_info.setToolTip(QCoreApplication.translate("Form", u"Enables automatic\n"
"compression of \n"
"files on the disk.\n"
"(not support ext2,\n"
"ext3, and ext4\n"
"filesystems).", None))
#endif // QT_CONFIG(tooltip)
        self.compressed_info.setText("")
        self.compressed_checkbox.setText(QCoreApplication.translate("Form", u"Compressed", None))
#if QT_CONFIG(tooltip)
        self.undeletable_info.setToolTip(QCoreApplication.translate("Form", u"When a file is deleted,\n"
"its contents are saved.\n"
"(not support ext2,\n"
"ext3, and ext4\n"
"filesystems).", None))
#endif // QT_CONFIG(tooltip)
        self.undeletable_info.setText("")
        self.undeletable_checkbox.setText(QCoreApplication.translate("Form", u"Undeletable", None))
#if QT_CONFIG(tooltip)
        self.no_dump_info.setToolTip(QCoreApplication.translate("Form", u"Excludes files from\n"
"backups made by\n"
"the dump command.", None))
#endif // QT_CONFIG(tooltip)
        self.no_dump_info.setText("")
        self.no_dump_checkbox.setText(QCoreApplication.translate("Form", u"No Dump", None))
#if QT_CONFIG(tooltip)
        self.do_not_compress_info.setToolTip(QCoreApplication.translate("Form", u"Excluded file from compression\n"
"on file systems that support\n"
"per-file compression.\n"
"(not support ext2, ext3, and ext4\n"
"filesystems).", None))
#endif // QT_CONFIG(tooltip)
        self.do_not_compress_info.setText("")
        self.do_not_compress_checkbox.setText(QCoreApplication.translate("Form", u"Don't Compress", None))
#if QT_CONFIG(tooltip)
        self.no_tail_merging_info.setToolTip(QCoreApplication.translate("Form", u"file system optimization\n"
"technique that aims to\n"
"improve storage efficiency\n"
"by addressing the issue\n"
"of wasted space at the\n"
"end of files. (not support\n"
"ext2, ext3, and ext4\n"
"filesystems).", None))
#endif // QT_CONFIG(tooltip)
        self.no_tail_merging_info.setText("")
#if QT_CONFIG(tooltip)
        self.no_tail_merging_checkbox.setToolTip(QCoreApplication.translate("Form", u"file system optimization technique that aims to improve storage efficiency by addressing the issue of wasted space at the end of files.", None))
#endif // QT_CONFIG(tooltip)
        self.no_tail_merging_checkbox.setText(QCoreApplication.translate("Form", u"No Tail-merging", None))
#if QT_CONFIG(tooltip)
        self.immutable_info.setToolTip(QCoreApplication.translate("Form", u"Makes files immutable,\n"
"meaning they cannot be\n"
"modified, deleted,\n"
"renamed, or linked.", None))
#endif // QT_CONFIG(tooltip)
        self.immutable_info.setText("")
        self.immutable_checkbox.setText(QCoreApplication.translate("Form", u"Immutable", None))
#if QT_CONFIG(tooltip)
        self.journaled_data_info.setToolTip(QCoreApplication.translate("Form", u"Enables data journaling\n"
"for files, ensuring data\n"
"consistency in case of\n"
"system crashes. Only\n"
"work with ext3 and ext4\n"
"filesystems.", None))
#endif // QT_CONFIG(tooltip)
        self.journaled_data_info.setText("")
        self.journaled_data_checkbox.setText(QCoreApplication.translate("Form", u"Journaled Data", None))
        self.secure_deletion_checkbox.setText(QCoreApplication.translate("Form", u"Secure Deletion", None))
#if QT_CONFIG(tooltip)
        self.secure_deletion_info.setToolTip(QCoreApplication.translate("Form", u"Causes files to be overwritten\n"
"with zeros when deleted.\n"
"(not support ext2, ext3,\n"
"and ext4 filesystems).", None))
#endif // QT_CONFIG(tooltip)
        self.secure_deletion_info.setText("")
        self.synchronous_updates_checkbox.setText(QCoreApplication.translate("Form", u"Synchronous Updates", None))
#if QT_CONFIG(tooltip)
        self.synchronous_updates_info.setToolTip(QCoreApplication.translate("Form", u"Makes file updates\n"
"synchronous. All changes\n"
"are written to the\n"
"disk immediately.", None))
#endif // QT_CONFIG(tooltip)
        self.synchronous_updates_info.setText("")
        self.star_4.setText(QCoreApplication.translate("Form", u"*", None))
        self.ip_inbestigator_title.setText(QCoreApplication.translate("Form", u"IP Investigator", None))
        self.search_label.setText(QCoreApplication.translate("Form", u"Search:", None))
        self.search_text_field.setText("")
        self.search_text_field.setPlaceholderText(QCoreApplication.translate("Form", u"IPv4", None))
        self.report_an_ip_button.setText(QCoreApplication.translate("Form", u"Report an IP Address", None))
        self.ip_address_search_button.setText(QCoreApplication.translate("Form", u"Search", None))
        self.star_5.setText(QCoreApplication.translate("Form", u"*", None))
        self.capture_evidence_title.setText(QCoreApplication.translate("Form", u"Capture Evidence", None))
        self.file_icon.setText("")
        self.generate_evidence_file_button.setText(QCoreApplication.translate("Form", u"    Generate Evidence File", None))
        self.company_or_client_name_label.setText(QCoreApplication.translate("Form", u"Company Name or Client Name:", None))
        self.company_or_client_name_field.setText("")
        self.company_or_client_name_field.setPlaceholderText("")
    # retranslateUi

