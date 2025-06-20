# This Python file uses the following encoding: utf-8
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

import sys
import os
import os.path
import threading

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit
from PySide6.QtGui import QIcon, QRegularExpressionValidator, QPixmap
from PySide6.QtCore import QRegularExpression, QThread, Signal, Slot

# Database classes
from DatabaseConnection import *
from DatabaseOperations import *

# Project classes
# from RPC_Client import RPC_Client
from DatabaseHealth import DatabaseHealth
from IPInvestigator import *
from PDFReportGeneration import *
from Dashboard_Connections import *
from Dashboard_Unique_IP import *
from Dashboard_Top_Attacking_IPs import *
from Dashboard_Opened_Ports import *
from Dashboard_Protocol_Type import *

# User Interface classes
from ui_Sign_up import Ui_Sign_Up
from ui_Login import Ui_Mainwindow
from ui_Main_User_Interface import Ui_Form
from ui_add_rule_dialog import Ui_Dialog
from ui_Reset_Password import Ui_ResetPassword
from ui_report_ip_dialog import Ui_report_Dialog
from ui_delete_rule_dialog import Ui_Delete_Dialog

class Mainwindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Mainwindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Honeypot - Login")

        # Objects
        self.sign_up_window = SignUpWindow()
        self.welcome_window = WelcomeWindow()
        self.reset_password_window = ResetPasswordWindow()
        self.rpc_client = RPC_Client()

        self.show_icon = QIcon("icons/opened eye.png")
        self.hide_icon = QIcon("icons/closed eye.png")
        self.ui.hide_show_button.setCheckable(True)
        self.ui.hide_show_button.setIcon(self.hide_icon)

        # Normal Buttons
        self.ui.forget_password_button.clicked.connect(self.open_reset_password_window)
        self.ui.sign_up_button.clicked.connect(self.open_sign_up_window)
        self.ui.hide_show_button.clicked.connect(self.toggle_password_visibility)
        self.ui.login_button.clicked.connect(self.check_fields)
        self.ui.skip.clicked.connect(self.open_secondary_window)

        self.sign_up_window.hide()
        self.reset_password_window.hide()
        self.welcome_window.hide()


    def toggle_password_visibility(self):
        if self.ui.hide_show_button.isChecked():
            self.ui.hide_show_button.setIcon(self.show_icon)
            self.ui.password_field.setEchoMode(QLineEdit.EchoMode.Normal)

        else:
            self.ui.password_field.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.hide_show_button.setIcon(self.hide_icon)

    # buttons actions
    def open_reset_password_window(self):
        self.ui.email_field.clear()
        self.ui.password_field.clear()
        self.hide()
        self.reset_password_window.show()

    def open_sign_up_window(self):
        self.ui.email_field.clear()
        self.ui.password_field.clear()
        self.hide()
        self.sign_up_window.show()

    def open_secondary_window(self):
        self.ui.email_field.clear()
        self.ui.password_field.clear()
        self.hide()
        self.welcome_window.show()

    def check_fields(self):
        email_field_text = self.ui.email_field.text().strip()
        password_field_text = self.ui.password_field.text().strip()

        if not email_field_text or not password_field_text:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
        else:
            self.validate_email()

    def validate_email(self):
        email_regex = QRegularExpression("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        email_field_content = self.ui.email_field.text()
        email_validator = QRegularExpressionValidator(email_regex)
        self.ui.email_field.setValidator(email_validator)
        match = email_regex.match(email_field_content)
        if not match.hasMatch():
            QMessageBox.critical(self, "Error", f"Invalid email format.")
        else:
            email = self.ui.email_field.text()
            password = self.ui.password_field.text()
            status = DatabaseOperations.login(email, password)
            if status == True:
                self.open_secondary_window()

class SignUpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Sign_Up()
        self.ui.setupUi(self)
        self.setWindowTitle("Honeypot - Sign Up")


        self.signup_show_icon = QIcon("icons/opened eye.png")
        self.signup_hide_icon = QIcon("icons/closed eye.png")
        self.ui.sign_up_hide_show_button.setCheckable(True)
        self.ui.sign_up_hide_show_button.setIcon(self.signup_hide_icon)

        # Normal Buttons
        self.ui.sign_up_hide_show_button.clicked.connect(self.sign_up_toggle_password_visibility)
        self.ui.sign_up_button.clicked.connect(self.check_fields)
        self.ui.sign_up_back_button.clicked.connect(self.open_login_window)

    def sign_up_toggle_password_visibility(self):
        if self.ui.sign_up_hide_show_button.isChecked():
            self.ui.sign_up_hide_show_button.setIcon(self.signup_show_icon)
            self.ui.sign_up_password_field.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui.sign_up_password_field.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.sign_up_hide_show_button.setIcon(self.signup_hide_icon)

    def validate_email(self):
        email_regex = QRegularExpression("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        email_field_content = self.ui.sign_up_email_field.text()
        email_validator = QRegularExpressionValidator(email_regex)
        self.ui.sign_up_email_field.setValidator(email_validator)
        match = email_regex.match(email_field_content)
        if not match.hasMatch():
            QMessageBox.critical(self, "Error", f"Invalid email format.")
        else:
            email = self.ui.sign_up_email_field.text()
            password = self.ui.sign_up_password_field.text()
            status = DatabaseOperations.sign_up(email, password)
            if status == True:
                self.open_login_window()

    def check_fields(self):
        email_field_text = self.ui.sign_up_email_field.text().strip()
        password_field_text = self.ui.sign_up_password_field.text().strip()
        if not email_field_text or not password_field_text:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
        else:
            self.validate_email()

    def open_login_window(self):
        self.ui.sign_up_email_field.clear()
        self.ui.sign_up_password_field.clear()
        self.hide()
        mainwindow.show()

class ResetPasswordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ResetPassword()
        self.ui.setupUi(self)
        self.setWindowTitle("Honeypot - Reset Password Page")

        self.reset_password_show_icon = QIcon("icons/opened eye.png")
        self.reset_password_hide_icon = QIcon("icons/closed eye.png")
        self.ui.reset_password_hide_show_button.setCheckable(True)
        self.ui.reset_password_hide_show_button.setIcon(self.reset_password_hide_icon)
        self.ui.confirm_password_hide_show_button.setCheckable(True)
        self.ui.confirm_password_hide_show_button.setIcon(self.reset_password_hide_icon)

        # Regular Expresssion
        numbers_only_regex = QRegularExpression("[0-9]")
        number_validator = QRegularExpressionValidator(numbers_only_regex)
        self.ui.first_field.setValidator(number_validator)
        self.ui.second_field.setValidator(number_validator)
        self.ui.third_field.setValidator(number_validator)
        self.ui.forth_field.setValidator(number_validator)
        self.ui.fifth_field.setValidator(number_validator)
        self.ui.sixth_field.setValidator(number_validator)

        # Pages
        self.ui.code_back_button.clicked.connect(lambda: self.ui.reset_processes.setCurrentWidget(self.ui.email_page))
        self.ui.reset_password_back_button.clicked.connect(lambda: self.ui.reset_processes.setCurrentWidget(self.ui.code_page))


        # Normal Buttons
        self.ui.continue_button.clicked.connect(self.check_email_field)
        self.ui.email_cancel_button.clicked.connect(self.open_login_window)
        self.ui.code_cancel_button.clicked.connect(self.open_login_window)
        self.ui.verify_button.clicked.connect(self.verify_code)
        self.ui.reset_password_cancel_button.clicked.connect(self.open_login_window)
        self.ui.reset_password_button.clicked.connect(self.check_password_fields)
        self.ui.reset_password_hide_show_button.clicked.connect(self.reset_password_toggle_password_visibility)
        self.ui.confirm_password_hide_show_button.clicked.connect(self.confirm_password_toggle_password_visibility)

        # Buttons Actions
    def open_login_window(self):
        self.ui.reset_password_email_field.clear()
        self.ui.first_field.clear()
        self.ui.second_field.clear()
        self.ui.third_field.clear()
        self.ui.forth_field.clear()
        self.ui.fifth_field.clear()
        self.ui.sixth_field.clear()
        self.ui.reset_password_field.clear()
        self.ui.confirm_password_field.clear()
        self.ui.reset_processes.setCurrentWidget(self.ui.email_page)
        self.hide()
        mainwindow.show()

    def validate_email(self):
        email_regex = QRegularExpression("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        email_field_content = self.ui.reset_password_email_field.text()
        email_validator = QRegularExpressionValidator(email_regex)
        self.ui.reset_password_email_field.setValidator(email_validator)
        match = email_regex.match(email_field_content)
        if not match.hasMatch():
            QMessageBox.critical(self, "Error", "Invalid email format.")
        else:
            self.email = self.ui.reset_password_email_field.text()
            status, self.reset_code = DatabaseOperations.reset_password(self.email)
            if status == True:
                self.ui.reset_processes.setCurrentWidget(self.ui.code_page)
                self.ui.message2_label.setText(f"Please enter the code sent to {self.email} to reset your password.")



    def verify_code(self):
        fields_content = ""
        fields_content += self.ui.first_field.text()
        fields_content += self.ui.second_field.text()
        fields_content += self.ui.third_field.text()
        fields_content += self.ui.forth_field.text()
        fields_content += self.ui.fifth_field.text()
        fields_content += self.ui.sixth_field.text()
        status = DatabaseOperations.check_code(fields_content, self.reset_code)
        if status == True:
            self.ui.reset_processes.setCurrentWidget(self.ui.reset_password_page)


    def check_email_field(self):
        email_field_content = self.ui.reset_password_email_field.text().strip()
        if not email_field_content:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
        else:
            self.validate_email()

    def validate_password(self):
        password_content = self.ui.reset_password_field.text()
        confirm_password_content = self.ui.confirm_password_field.text()
        if password_content != confirm_password_content:
            QMessageBox.critical(self, "Error", "Passwords do not match.")
        else:
            DatabaseOperations.set_new_password(self.email, password_content)
            self.open_login_window()

    def check_password_fields(self):
        password_field_content = self.ui.reset_password_field.text().strip()
        confirm_field_content = self.ui.confirm_password_field.text().strip()
        if not password_field_content or not confirm_field_content:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
        else:
            self.validate_password()

    def reset_password_toggle_password_visibility(self):
        if self.ui.reset_password_hide_show_button.isChecked():
            self.ui.reset_password_hide_show_button.setIcon(self.reset_password_show_icon)
            self.ui.reset_password_field.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui.reset_password_field.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.reset_password_hide_show_button.setIcon(self.reset_password_hide_icon)

    def confirm_password_toggle_password_visibility(self):
        if self.ui.confirm_password_hide_show_button.isChecked():
            self.ui.confirm_password_hide_show_button.setIcon(self.reset_password_show_icon)
            self.ui.confirm_password_field.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui.confirm_password_field.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.confirm_password_hide_show_button.setIcon(self.reset_password_hide_icon)



class WelcomeWindow(QWidget):
    from scapy.all import sniff, Packet
    from scapy.layers.inet import IP, TCP, UDP
    import ipaddress

    output_received = Signal(str)
    unique_ip_output_received = Signal(str)
    attack_attempts_received = Signal(str)
    opened_ports_received = Signal(str)
    protocol_type_received = Signal(str)

    def __init__(self):
        import itertools
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Honeypot")
        self.ui.workstation.setCurrentWidget(self.ui.welcome_page)
        self.ui.welcome_button.setChecked(True)
        self.add_rule_dialog = FirewallRules()
        self.delete_rule_dialog = DeleteFirwallRule()
        self.report_ip_address = ReportIPAddress()

        self.connections_thread = None
        self.connections_obj = None

        self.unique_ip_thread = None
        self.unique_ip_obj = None

        self.top_attacking_ips_thread = None
        self.top_attacking_ips_obj = None

        self.opened_ports_thread = None
        self.opened_ports_obj = None

        self.protocol_type_thread = None
        self.protocol_type_obj = None

        self.output_received.connect(self.append_connections_output)
        self.unique_ip_output_received.connect(self.append_unique_ip)
        self.attack_attempts_received.connect(self.append_top_attacking_ips)
        self.opened_ports_received.connect(self.append_opened_ports)
        self.protocol_type_received.connect(self.append_protocol_type)
        self.start_connection_process()
        self.start_unique_process()
        self.start_top_attacking_ips_process()
        self.start_opened_ports_process()
        self.start_protocol_type_process()

        # functionality
        self.setup_validation()
        self.client = None

        # images
        self.connected = QPixmap("icons/connected.png")
        self.disconnected = QPixmap("icons/disconnected.png")
        self.ui.ssh_server_status.setPixmap(self.disconnected)


        process = os.popen("sudo ufw status numbered")
        output = process.read()
        process.close()
        if output.strip() == "Status: inactive":
            self.ui.disable_button.click()
            self.ui.current_firewall_rules_field.setPlainText("Status: inactive")
        else:
            output_rule = ""
            for i in itertools.count(3):
                rule = os.popen("sudo ufw status numbered | awk 'NR=={}'".format(i))
                rules = rule.read()
                output_rule += rules
                if rules == "":
                    self.ui.current_firewall_rules_field.setPlainText(output_rule)
                    rule.close()
                    break

        self.ui.add_button.clicked.connect(self.open_add_rule_dialog)
        self.ui.delete_button.clicked.connect(self.open_delete_rule_dialog)
        self.ui.refresh_button.clicked.connect(self.refresh_firewall_rules)
        self.ui.ip_address_search_button.clicked.connect(self.check_search_field)
        self.ui.report_an_ip_button.clicked.connect(self.open_report_ip_address_dialog)


        self.ui.connect_to_ssh_server_button.clicked.connect(self.connect_to_shell)
        self.ui.close_ssh_connection_button.clicked.connect(self.close_connection_to_shell)
        self.ui.send_button.clicked.connect(self.send_button_action)


        self.ui.upload_attributes_button.clicked.connect(self.upload_attributes)
        self.ui.apply_attributes_button.clicked.connect(self.apply_attributes)

        # Pages
        self.ui.welcome_button.clicked.connect(lambda: self.ui.workstation.setCurrentWidget(self.ui.welcome_page))
        self.ui.dashboard_button.clicked.connect(lambda: self.ui.workstation.setCurrentWidget(self.ui.dashboard_page))
        self.ui.network_monitor_button.clicked.connect(lambda: self.ui.workstation.setCurrentWidget(self.ui.network_monitor_page))
        self.ui.firewall_setting_button.clicked.connect(lambda: self.ui.workstation.setCurrentWidget(self.ui.firewall_setting_page))
        self.ui.database_health_button.clicked.connect(lambda: self.ui.workstation.setCurrentWidget(self.ui.database_health_page))
        self.ui.remote_shell_button.clicked.connect(lambda: self.ui.workstation.setCurrentWidget(self.ui.remote_shell_page))
        self.ui.file_security_button.clicked.connect(lambda: self.ui.workstation.setCurrentWidget(self.ui.file_security_page))
        self.ui.ip_investigator_button.clicked.connect(lambda: self.ui.workstation.setCurrentWidget(self.ui.ip_investigator_page))
        self.ui.capture_evidence_button.clicked.connect(lambda: self.ui.workstation.setCurrentWidget(self.ui.capture_evidence_page))

        # Normal Buttons
        self.ui.logout_button.clicked.connect(self.open_main_window)
        self.ui.get_started_button.clicked.connect(self.get_started_action)
        self.ui.start_button.clicked.connect(self.start_button_action)
        self.ui.download_button.clicked.connect(self.download_button_action)
        self.ui.enable_button.clicked.connect(self.enable_button_action)
        self.ui.disable_button.clicked.connect(self.disable_button_action)
        self.ui.reload_button.clicked.connect(self.reload_button_action)
        self.ui.add_hash_to_database_button.clicked.connect(self.add_hash_to_database_action)
        self.ui.check_button.clicked.connect(self.check_button_action)
        self.ui.generate_evidence_file_button.clicked.connect(self.generate_evidence_file)

    # Buttons Actions
    def open_main_window(self):
        self.ui.workstation.setCurrentWidget(self.ui.welcome_page)
        self.ui.welcome_button.setChecked(True)
        self.hide()
        mainwindow.show()



# ---------------------------------------------------------(Welcome)---------------------------------------------------------
    def get_started_action(self):
        self.ui.dashboard_button.setChecked(True)
        self.ui.workstation.setCurrentWidget(self.ui.dashboard_page)
# ---------------------------------------------------------(Dashboard)---------------------------------------------------------

    @Slot(str)
    def append_connections_output(self, text):
        self.ui.connections_output_field.append(text)


    def start_connection_process(self):
        if self.connections_thread is None:
            self.connections_obj = Dashboard_Connections(self.output_received)
            self.connections_thread = QThread()
            self.connections_obj.moveToThread(self.connections_thread)
            self.connections_thread.started.connect(self.connections_obj.start_sniffing)
            self.connections_obj.finished.connect(self.connections_thread.quit)
            self.connections_obj.finished.connect(self.connections_obj.deleteLater)
            self.connections_thread.finished.connect(self.connections_thread.deleteLater)
            self.connections_thread.start()
        else:
            print("Dashboard already running.")

    @Slot(str)
    def append_unique_ip(self, text):
        self.ui.unique_detected_traffic_field.clear()
        self.ui.unique_detected_traffic_field.setPlainText(text)


    def start_unique_process(self):
        if self.unique_ip_thread is None:
            self.unique_ip_obj = Dashboard_Unique_IP(self.unique_ip_output_received)
            self.unique_ip_thread = QThread()
            self.unique_ip_obj.moveToThread(self.unique_ip_thread)
            self.unique_ip_thread.started.connect(self.unique_ip_obj.start_sniffing)
            self.unique_ip_obj.finished.connect(self.unique_ip_thread.quit)
            self.unique_ip_obj.finished.connect(self.unique_ip_obj.deleteLater)
            self.unique_ip_thread.finished.connect(self.unique_ip_thread.deleteLater)
            self.unique_ip_thread.start()
        else:
            print("Dashboard already running.")

    @Slot(str)
    def append_top_attacking_ips(self, text):
        self.ui.top_attacking_ips_field.clear()
        self.ui.top_attacking_ips_field.setPlainText(text)


    def start_top_attacking_ips_process(self):
        if self.top_attacking_ips_thread is None:
            self.top_attacking_ips_obj = Dashboard_Top_Attacking_IPs(self.attack_attempts_received)
            self.top_attacking_ips_thread = QThread()
            self.top_attacking_ips_obj.moveToThread(self.top_attacking_ips_thread)
            self.top_attacking_ips_thread.started.connect(self.top_attacking_ips_obj.start_sniffing)
            self.top_attacking_ips_obj.finished.connect(self.top_attacking_ips_thread.quit)
            self.top_attacking_ips_obj.finished.connect(self.top_attacking_ips_obj.deleteLater)
            self.top_attacking_ips_thread.finished.connect(self.top_attacking_ips_thread.deleteLater)
            self.top_attacking_ips_thread.start()
        else:
            print("Dashboard already running.")

    @Slot(str)
    def append_opened_ports(self, text):
        self.ui.opened_ports_field.clear()
        self.ui.opened_ports_field.setPlainText(text)


    def start_opened_ports_process(self):
        if self.opened_ports_thread is None:
            self.opened_ports_obj = Dashboard_Opened_Ports(self.opened_ports_received)
            self.opened_ports_thread = QThread()
            self.opened_ports_obj.moveToThread(self.opened_ports_thread)
            self.opened_ports_thread.started.connect(self.opened_ports_obj.start_sniffing)
            self.opened_ports_obj.finished.connect(self.opened_ports_thread.quit)
            self.opened_ports_obj.finished.connect(self.opened_ports_obj.deleteLater)
            self.opened_ports_thread.finished.connect(self.opened_ports_thread.deleteLater)
            self.opened_ports_thread.start()
        else:
            print("Dashboard already running.")

    @Slot(str)
    def append_protocol_type(self, text):
        self.ui.protocol_type_field.clear()
        self.ui.protocol_type_field.setPlainText(text)


    def start_protocol_type_process(self):
        if self.protocol_type_thread is None:
            self.protocol_type_obj = Dashboard_Protocol_Type(self.protocol_type_received)
            self.protocol_type_thread = QThread()
            self.protocol_type_obj.moveToThread(self.protocol_type_thread)
            self.protocol_type_thread.started.connect(self.protocol_type_obj.start_sniffing)
            self.protocol_type_obj.finished.connect(self.protocol_type_thread.quit)
            self.protocol_type_obj.finished.connect(self.protocol_type_obj.deleteLater)
            self.protocol_type_thread.finished.connect(self.protocol_type_thread.deleteLater)
            self.protocol_type_thread.start()
        else:
            print("Dashboard already running.")

    def closeEvent(self, event):
        if self.connections_obj:
            self.connections_obj.stop_sniffing()
            if self.connections_thread and self.connections_thread.isRunning():
                self.connections_thread.quit()
                self.connections_thread.wait()
                self.connections_obj.deleteLater()
                self.connections_thread.deleteLater()
                self.connections_obj = None
                self.connections_thread = None

            if self.unique_ip_obj:
                self.unique_ip_obj.stop_sniffing()
                if self.unique_ip_thread and self.unique_ip_thread.isRunning():
                    self.unique_ip_thread.quit()
                    self.unique_ip_thread.wait()
                    self.unique_ip_obj.deleteLater()
                    self.unique_ip_thread.deleteLater()
                    self.unique_ip_obj = None
                    self.unique_ip_thread = None

            if self.top_attacking_ips_obj:
                self.top_attacking_ips_obj.stop_sniffing()
                if self.top_attacking_ips_thread and self.top_attacking_ips_thread.isRunning():
                    self.top_attacking_ips_thread.quit()
                    self.top_attacking_ips_thread.wait()
                    self.top_attacking_ips_obj.deleteLater()
                    self.top_attacking_ips_thread.deleteLater()
                    self.top_attacking_ips_obj = None
                    self.top_attacking_ips_thread = None

            if self.opened_ports_obj:
                self.opened_ports_obj.stop_sniffing()
                if self.opened_ports_thread and self.opened_ports_thread.isRunning():
                    self.opened_ports_thread.quit()
                    self.opened_ports_thread.wait()
                    self.opened_ports_obj.deleteLater()
                    self.opened_ports_thread.deleteLater()
                    self.opened_ports_obj = None
                    self.opened_ports_thread = None

            if self.protocol_type_obj:
                self.protocol_type_obj.stop_sniffing()
                if self.protocol_type_thread and self.protocol_type_thread.isRunning():
                    self.protocol_type_thread.quit()
                    self.protocol_type_thread.wait()
                    self.protocol_type_obj.deleteLater()
                    self.protocol_type_thread.deleteLater()
                    self.protocol_type_obj = None
                    self.protocol_type_thread = None

            event.accept()



# ---------------------------------------------------------(Network Monitor)---------------------------------------------------------
    def check_interface_field(self):
        interface = self.ui.interface_field.text().strip()
        if not interface:
            QMessageBox.warning(self, "Error", "Please fill the interface field.")
        else:
            self.start_button_action()

    def start_button_action(self):
        self.ui.output_field.clear()
        interface = self.ui.interface_field.text()
        duration = self.ui.duration_time_field.text()
        if duration == "":
            output = self.capture_packets(interface)
        else:
            output = self.capture_packets(interface, int(duration))
        self.update_output_field(output)

    def update_output_field(self, output):
        self.ui.output_field.clear()
        self.ui.output_field.setPlainText(output)

    def capture_packets(self, interface="eth0", duration=10):
        import subprocess
        output_file = ""
        try:
            command = [
                "tshark",
                "-i", interface,
                "-a", f"duration:{duration}",
                "-w", "path/packet_captured.pcap",
                "-Tfields",
                "-e", "frame.number",
                "-e", "frame.time",
                "-e", "eth.src",
                "-e", "eth.dst",
                "-e", "ip.src",
                "-e", "ip.dst",
                "-e", "tcp.srcport",
                "-e", "tcp.dstport",
                "-e", "udp.srcport",
                "-e", "udp.dstport","-i", interface,
                "-e", "frame.len",
                "-E", "separator=,",
                "-E", "occurrence=a",
                "-E", "header=y",
                ]
            remove_file_thread = threading.Thread(target=self.delete_captured_file)
            remove_file_thread.start()
            QMessageBox.information(self, "Note", "Packet Capturing Start...")
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()

            if process.returncode == 0:
                return stdout
            else:
                QMessageBox.warning(self, "Error", f"Error capturing packets: {stderr}")
                return None

        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "tshark not found. Make sure it's installed and in your PATH.")
            return None
        except Exception as e:
            QMessageBox.warning(self, "Error", f"An unexpected error occurred: {e}")
            return None

    def download_button_action(self):
        from PySide6.QtWidgets import QFileDialog
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getSaveFileName(self, "Select File", "", "All Files (*);;Text Files (*.txt)")
        command = "cp path/packet_captured.pcap " + file_path
        os.system(command)

    def delete_captured_file(self):
        time.sleep(300)
        os.system("rm path/packet_captured.pcap")

# ---------------------------------------------------------(Firewall Rules)---------------------------------------------------------
    def current_rules(self):
        import itertools
        process = os.popen("sudo ufw status numbered")
        output = process.read()
        process.close()
        if output.strip() == "Status: inactive":
            self.ui.current_firewall_rules_field.setPlainText("Status: inactive")
        elif output.strip() == "Status: active":
            default = os.popen("sudo ufw status verbose | sed '1d'")
            default_output = default.read()
            self.ui.current_firewall_rules_field.setPlainText(default_output)
        else:
            output_rule = ""
            for i in itertools.count(3):
                rule = os.popen("sudo ufw status numbered | awk 'NR=={}'".format(i))
                rules = rule.read()
                output_rule += rules
                if rules == "":
                    self.ui.current_firewall_rules_field.setPlainText(output_rule)
                    rule.close()
                    break

    def enable_button_action(self):
        self.ui.current_firewall_rules_field.clear()
        os.system("sudo ufw enable")
        self.current_rules()

    def disable_button_action(self):
        self.ui.current_firewall_rules_field.clear()
        os.system("sudo ufw disable")
        self.current_rules()

    def reload_button_action(self):
        status = os.popen("sudo ufw status | awk 'NR==1'")
        output = status.read()
        if output.strip() == "Status: active":
            self.ui.enable_button.setChecked(True)
            os.system("sudo ufw reload")
        else:
            self.ui.disable_button.setChecked(True)
            os.system("sudo ufw reload")

    def refresh_firewall_rules(self):
        self.current_rules()

    def open_add_rule_dialog(self):
        self.add_rule_dialog.show()
        self.add_rule_dialog.move(700, 250)

    def open_delete_rule_dialog(self):
        self.delete_rule_dialog.show()
        self.delete_rule_dialog.move(700, 250)
# ---------------------------------------------------------(Database Health)---------------------------------------------------------
    def add_hash_to_database_action(self):
        path = self.ui.path_field.text()
        self.ui.path_field.clear()
        obj = DatabaseHealth()
        obj.check_for_path(self, path)

    def check_button_action(self):
        path = self.ui.path_field.text()
        self.ui.path_field.clear()
        obj = DatabaseHealth()
        obj.check_hash(self, path)

# ---------------------------------------------------------(Remote Shell)---------------------------------------------------------
    def check_empty_command_fields(self):
        command_content = self.ui.command_field.text().strip()

        if not command_content:
            QMessageBox.warning(self, "Error", "Please fill command fields.")
        else:
            self.send_button_action()

    def connect_to_shell(self):
        import paramiko
        hostname = 'your honeypot ip address'
        port = 22
        username = 'honeypot username'
        password = 'honeypot password'

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self.client.connect(hostname, port, username, password)
            self.ui.ssh_server_status.setPixmap(self.connected)
        except paramiko.AuthenticationException:
            QMessageBox.warning(self, "Error", "Authentication failed.")
        except paramiko.SSHException as e:
            QMessageBox.warning(self, "Error", f"Could not establish SSH connection: {e}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"An error occurred: {e}")

    def close_connection_to_shell(self):
        import paramiko
        self.client.close()
        self.ui.ssh_server_status.setPixmap(self.disconnected)


    def send_button_action(self):
        import paramiko
        try:
            command = self.ui.command_field.text()
            stdin, stdout, stderr = self.client.exec_command(command)
            if stdout.channel.recv_exit_status() == 0:
                self.ui.remote_shell_output_field.setPlainText(stdout.read().decode("utf8"))
            else:
                self.ui.remote_shell_output_field.setPlainText(stderr.read().decode("utf8"))

        except paramiko.AuthenticationException:
            QMessageBox.warning(self, "Error", "Authentication failed.")
        except paramiko.SSHException as e:
            QMessageBox.warning(self, "Error", f"Could not establish SSH connection: {e}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"An error occurred: {e}")


# ---------------------------------------------------------(File Security)---------------------------------------------------------
    def upload_attributes(self):
        path = self.ui.file_security_path_field.text()
        if os.path.exists(path):
            if os.path.isfile(path):
                process = os.popen("lsattr {} | awk '{{print $1}}'".format(path))
                output = process.read()
                process.close()

                self.ui.append_only_checkbox.setChecked(False)
                self.ui.no_atime_updates_checkbox.setChecked(False)
                self.ui.compressed_checkbox.setChecked(False)
                self.ui.secure_deletion_checkbox.setChecked(False)
                self.ui.undeletable_checkbox.setChecked(False)
                self.ui.no_dump_checkbox.setChecked(False)
                self.ui.do_not_compress_checkbox.setChecked(False)
                self.ui.synchronous_updates_checkbox.setChecked(False)
                self.ui.no_tail_merging_checkbox.setChecked(False)
                self.ui.immutable_checkbox.setChecked(False)
                self.ui.journaled_data_checkbox.setChecked(False)

                for i in output:
                    if i == "-":
                        continue
                    elif i == "a":
                        self.ui.append_only_checkbox.setChecked(True)
                    elif i == "A":
                        self.ui.no_atime_updates_checkbox.setChecked(True)
                    elif i == "c":
                        self.ui.compressed_checkbox.setChecked(True)
                    elif i == "s":
                        self.ui.secure_deletion_checkbox.setChecked(True)
                    elif i == "u":
                        self.ui.undeletable_checkbox.setChecked(True)
                    elif i == "d":
                        self.ui.no_dump_checkbox.setChecked(True)
                    elif i == "m":
                        self.ui.do_not_compress_checkbox.setChecked(True)
                    elif i == "S":
                        self.ui.synchronous_updates_checkbox.setChecked(True)
                    elif i == "t":
                        self.ui.no_tail_merging_checkbox.setChecked(True)
                    elif i == "i":
                        self.ui.immutable_checkbox.setChecked(True)
                    elif i == "j":
                        self.ui.journaled_data_checkbox.setChecked(True)

                QMessageBox.information(self, "Note", "File attributes uploaded.")
            elif os.path.isdir(path):
                QMessageBox.critical(self, "Error", f"The path provided ('{path}') is a directory. Please specify a file path.")
        else:
            QMessageBox.critical(self, "Error", "The specified path does not exist.")

    def apply_attributes(self):
        path = self.ui.file_security_path_field.text()
        process = os.popen("lsattr {} | awk '{{print $1}}'".format(path))
        output = process.read()
        process.close()
        for i in output:
            if i == "-":
                continue
            if self.ui.append_only_checkbox.isChecked():
                os.popen("sudo chattr +a {}".format(path))
            if not self.ui.append_only_checkbox.isChecked():
                os.popen("sudo chattr -a {}".format(path))
            if self.ui.no_atime_updates_checkbox.isChecked():
                os.popen("sudo chattr +A {}".format(path))
            if not self.ui.no_atime_updates_checkbox.isChecked():
                os.popen("sudo chattr -A {}".format(path))
            if self.ui.compressed_checkbox.isChecked():
                os.popen("sudo chattr +c {}".format(path))
            if not self.ui.compressed_checkbox.isChecked():
                os.popen("sudo chattr -c {}".format(path))
            if self.ui.secure_deletion_checkbox.isChecked():
                os.popen("sudo chattr +s {}".format(path))
            if not self.ui.secure_deletion_checkbox.isChecked():
                os.popen("sudo chattr -s {}".format(path))
            if self.ui.undeletable_checkbox.isChecked():
                os.popen("sudo chattr +u {}".format(path))
            if not self.ui.undeletable_checkbox.isChecked():
                os.popen("sudo chattr -u {}".format(path))
            if self.ui.no_dump_checkbox.isChecked():
                os.popen("sudo chattr +d {}".format(path))
            if not self.ui.no_dump_checkbox.isChecked():
                os.popen("sudo chattr -d {}".format(path))
            if self.ui.do_not_compress_checkbox.isChecked():
                os.popen("sudo chattr +m {}".format(path))
            if not self.ui.do_not_compress_checkbox.isChecked():
                os.popen("sudo chattr -m {}".format(path))
            if self.ui.synchronous_updates_checkbox.isChecked():
                os.popen("sudo chattr +S {}".format(path))
            if not self.ui.synchronous_updates_checkbox.isChecked():
                os.popen("sudo chattr -S {}".format(path))
            if self.ui.no_tail_merging_checkbox.isChecked():
                os.popen("sudo chattr +t {}".format(path))
            if not self.ui.no_tail_merging_checkbox.isChecked():
                os.popen("sudo chattr -t {}".format(path))
            if self.ui.immutable_checkbox.isChecked():
                os.popen("sudo chattr +i {}".format(path))
            if not self.ui.immutable_checkbox.isChecked():
                os.popen("sudo chattr -i {}".format(path))
            if self.ui.journaled_data_checkbox.isChecked():
                os.popen("sudo chattr +j {}".format(path))
            if not self.ui.journaled_data_checkbox.isChecked():
                os.popen("sudo chattr -j {}".format(path))
        QMessageBox.information(self, "Note", "File attributes updated!")

# ---------------------------------------------------------(IP Investigator)---------------------------------------------------------
    def open_report_ip_address_dialog(self):
        self.report_ip_address.show()
        self.report_ip_address.move(500, 290)

    def check_search_field(self):
        ip_field_content = self.ui.search_text_field.text().strip()
        if not ip_field_content:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
        else:
            self.search_ip_address()

    def setup_validation(self):
        ipv4_regex = QRegularExpression("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
        ip_validator = QRegularExpressionValidator(ipv4_regex)
        self.ui.search_text_field.setValidator(ip_validator)

    def search_ip_address(self):
        self.ui.search_output_textedit.clear()
        ip_address = self.ui.search_text_field.text()
        status = IPInvestigator.check_ip(ip_address)
        if not status == None:
            data = ""
            data += "IP Address: " + str(status['data']['ipAddress']) + "\n"
            data += "Public IP: " + str(status['data']['isPublic']) + "\n"
            data += "IP Version: " + str(status['data']['ipVersion']) + "\n"
            data += "Whitelisted: " + str(status['data']['isWhitelisted']) + "\n"
            data += "Abuse Confidence Score: " + str(status['data']['abuseConfidenceScore']) + "\n"
            country_name = self.translate_country_code(str(status['data']['countryCode']))
            data += "Country Name: " + str(country_name) + "\n"
            data += "Usage Type: " + str(status['data']['usageType']) + "\n"
            data += "ISP: " + str(status['data']['isp']) + "\n"
            data += "Domain: " + str(status['data']['domain']) + "\n"
            data += "Hostnames: " + str(status['data']['hostnames']) + "\n"
            data += "Tor Exit Node: " + str(status['data']['isTor']) + "\n"
            data += "Total Reports: " + str(status['data']['totalReports']) + "\n"
            data += "Distinct Users Reporting: " + str(status['data']['numDistinctUsers']) + "\n"
            data += "Last Reported At: " + str(status['data']['lastReportedAt']) + "\n"
            self.ui.search_output_textedit.setPlainText(data)
            self.ui.search_text_field.clear()
        else:
            QMessageBox.critical(self, "Error", "Invalid IP Address format.")

    def translate_country_code(self, country_code):
        country_name = {
        "AF": "Afghanistan",
        "AL": "Albania",
        "DZ": "Algeria",
        "AD": "Andorra",
        "AO": "Angola",
        "AG": "Antigua and Barbuda",
        "AR": "Argentina",
        "AM": "Armenia",
        "AU": "Australia",
        "AT": "Austria",
        "AZ": "Azerbaijan",
        "BS": "Bahamas",
        "BH": "Bahrain",
        "BD": "Bangladesh",
        "BB": "Barbados",
        "BY": "Belarus",
        "BE": "Belgium",
        "BZ": "Belize",
        "BJ": "Benin",
        "BT": "Bhutan",
        "BO": "Bolivia",
        "BA": "Bosnia and Herzegovina",
        "BW": "Botswana",
        "BR": "Brazil",
        "BN": "Brunei",
        "BG": "Bulgaria",
        "BF": "Burkina Faso",
        "BI": "Burundi",
        "CV": "Cabo Verde",
        "KH": "Cambodia",
        "CM": "Cameroon",
        "CA": "Canada",
        "CF": "Central African Republic",
        "TD": "Chad",
        "CL": "Chile",
        "CN": "China",
        "CO": "Colombia",
        "KM": "Comoros",
        "CG": "Congo",
        "CD": "Congo, Democratic Republic of the",
        "CR": "Costa Rica",
        "CI": "Côte d'Ivoire",
        "HR": "Croatia",
        "CU": "Cuba",
        "CY": "Cyprus",
        "CZ": "Czechia",
        "DK": "Denmark",
        "DJ": "Djibouti",
        "DM": "Dominica",
        "DO": "Dominican Republic",
        "EC": "Ecuador",
        "EG": "Egypt",
        "SV": "El Salvador",
        "GQ": "Equatorial Guinea",
        "ER": "Eritrea",
        "EE": "Estonia",
        "SZ": "Eswatini",
        "ET": "Ethiopia",
        "FJ": "Fiji",
        "FI": "Finland",
        "FR": "France",
        "GA": "Gabon",
        "GM": "Gambia",
        "GE": "Georgia",
        "DE": "Germany",
        "GH": "Ghana",
        "GR": "Greece",
        "GD": "Grenada",
        "GT": "Guatemala",
        "GN": "Guinea",
        "GW": "Guinea-Bissau",
        "GY": "Guyana",
        "HT": "Haiti",
        "HN": "Honduras",
        "HU": "Hungary",
        "IS": "Iceland",
        "IN": "India",
        "ID": "Indonesia",
        "IR": "Iran",
        "IQ": "Iraq",
        "IE": "Ireland",
        "IL": "Israel",
        "IT": "Italy",
        "JM": "Jamaica",
        "JP": "Japan",
        "JO": "Jordan",
        "KZ": "Kazakhstan",
        "KE": "Kenya",
        "KI": "Kiribati",
        "KP": "Korea, North",
        "KR": "Korea, South",
        "KW": "Kuwait",
        "KG": "Kyrgyzstan",
        "LA": "Laos",
        "LV": "Latvia",
        "LB": "Lebanon",
        "LS": "Lesotho",
        "LR": "Liberia",
        "LY": "Libya",
        "LI": "Liechtenstein",
        "LT": "Lithuania",
        "LU": "Luxembourg",
        "MG": "Madagascar",
        "MW": "Malawi",
        "MY": "Malaysia",
        "MV": "Maldives",
        "ML": "Mali",
        "MT": "Malta",
        "MH": "Marshall Islands",
        "MR": "Mauritania",
        "MU": "Mauritius",
        "MX": "Mexico",
        "FM": "Micronesia",
        "MD": "Moldova",
        "MC": "Monaco",
        "MN": "Mongolia",
        "ME": "Montenegro",
        "MA": "Morocco",
        "MZ": "Mozambique",
        "MM": "Myanmar",
        "NA": "Namibia",
        "NR": "Nauru",
        "NP": "Nepal",
        "NL": "Netherlands",
        "NZ": "New Zealand",
        "NI": "Nicaragua",
        "NE": "Niger",
        "NG": "Nigeria",
        "MK": "North Macedonia",
        "NO": "Norway",
        "OM": "Oman",
        "PK": "Pakistan",
        "PW": "Palau",
        "PS": "Palestine, State of",
        "PA": "Panama",
        "PG": "Papua New Guinea",
        "PY": "Paraguay",
        "PE": "Peru",
        "PH": "Philippines",
        "PL": "Poland",
        "PT": "Portugal",
        "QA": "Qatar",
        "RO": "Romania",
        "RU": "Russia",
        "RW": "Rwanda",
        "KN": "Saint Kitts and Nevis",
        "LC": "Saint Lucia",
        "VC": "Saint Vincent and the Grenadines",
        "WS": "Samoa",
        "SM": "San Marino",
        "ST": "Sao Tome and Principe",
        "SA": "Saudi Arabia",
        "SN": "Senegal",
        "RS": "Serbia",
        "SC": "Seychelles",
        "SL": "Sierra Leone",
        "SG": "Singapore",
        "SK": "Slovakia",
        "SI": "Slovenia",
        "SB": "Solomon Islands",
        "SO": "Somalia",
        "ZA": "South Africa",
        "SS": "South Sudan",
        "ES": "Spain",
        "LK": "Sri Lanka",
        "SD": "Sudan",
        "SR": "Suriname",
        "SE": "Sweden",
        "CH": "Switzerland",
        "SY": "Syria",
        "TW": "Taiwan",
        "TJ": "Tajikistan",
        "TZ": "Tanzania",
        "TH": "Thailand",
        "TL": "Timor-Leste",
        "TG": "Togo",
        "TO": "Tonga",
        "TT": "Trinidad and Tobago",
        "TN": "Tunisia",
        "TR": "Turkey",
        "TM": "Turkmenistan",
        "TV": "Tuvalu",
        "UG": "Uganda",
        "UA": "Ukraine",
        "AE": "United Arab Emirates",
        "GB": "United Kingdom",
        "US": "United States",
        "UY": "Uruguay",
        "UZ": "Uzbekistan",
        "VU": "Vanuatu",
        "VA": "Vatican City",
        "VE": "Venezuela",
        "VN": "Vietnam",
        "YE": "Yemen",
        "ZM": "Zambia",
        "ZW": "Zimbabwe",
        }
        return country_name.get(country_code.upper(), "Unknown Country")


# ---------------------------------------------------------(Capture Evidence)---------------------------------------------------------
    def generate_evidence_file(self):
        from PySide6.QtWidgets import QFileDialog
        company_or_client_name = self.ui.company_or_client_name_field.text()
        if company_or_client_name == "":
            obj = PDFReportGeneration()
            file_dialog = QFileDialog(self)
            file_path, _ = file_dialog.getSaveFileName(self, "Select File", "", "All Files (*);;Text Files (*.txt)")
            obj.main(company_or_client_name=" ")
            command = "mv path/Evidence.pdf " + file_path
            os.system(command)

        else:
            obj = PDFReportGeneration()
            file_dialog = QFileDialog(self)
            file_path, _ = file_dialog.getSaveFileName(self, "Select File", "", "All Files (*);;Text Files (*.txt)")
            obj.main(company_or_client_name)
            command = "mv path/Evidence.pdf " + file_path
            os.system(command)

# ---------------------------------------------------------(Firewall Rules Add Dialog)---------------------------------------------------------
class FirewallRules(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Honeypot - Add Rule")

        self.ui.policy_combobox.setCurrentText("Allow")
        self.ui.direction_combobox.setCurrentText("In")
        self.ui.protocol_combobox.setCurrentText("Both")

        # Normal Buttons
        self.ui.close_button.clicked.connect(self.close)
        self.ui.add_rule_button.clicked.connect(self.check_empty_fields)

    def check_empty_fields(self):
        source_content = self.ui.source_field.text().strip()
        destination_content = self.ui.destination_field.text().strip()
        port_content = self.ui.port_number_field.text().strip()

        if not source_content or not destination_content or not port_content:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
        else:
            self.add_rule()

    def add_rule(self):
        source = self.ui.source_field.text()
        destination = self.ui.destination_field.text()
        rule_description = self.ui.rule_name_field.text()
        policy = self.ui.policy_combobox.currentText()
        direction = self.ui.direction_combobox.currentText()
        protocol = self.ui.protocol_combobox.currentText()
        port = self.ui.port_number_field.text()
        if direction == "Both" and protocol == "Both":
            command = "sudo ufw " + policy.lower() + " in" + " from " + source.lower() + " to " + destination.lower() + " port " + port.lower() + " proto tcp comment '" + rule_description + "'"
            try:
                os.system(command)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"{e}")
            command = "sudo ufw " + policy.lower() + " in" + " from " + source.lower() + " to " + destination.lower() + " port " + port.lower() + " proto udp comment '" + rule_description + "'"
            try:
                os.system(command)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"{e}")
            command = "sudo ufw " + policy.lower() + " out" + " from " + source.lower() + " to " + destination.lower() + " port " + port.lower() + " proto tcp comment '" + rule_description + "'"
            try:
                os.system(command)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"{e}")
            command = "sudo ufw " + policy.lower() + " out" + " from " + source.lower() + " to " + destination.lower() + " port " + port.lower() + " proto udp comment '" + rule_description + "'"
            try:
                os.system(command)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"{e}")
            QMessageBox.information(self, "Note", "Rules added successfully.")

        elif direction == "Both":
            command = "sudo ufw " + policy.lower() + " in from " + source.lower() + " to " + destination.lower() + " port " + port.lower() + " proto " + protocol.lower() + " comment '" + rule_description + "'"
            try:
                os.system(command)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"{e}")
            command = "sudo ufw " + policy.lower() + " out from " + source.lower() + " to " + destination.lower() + " port " + port.lower() + " proto " + protocol.lower() + " comment '" + rule_description + "'"
            try:
                os.system(command)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"{e}")
            QMessageBox.information(self, "Note", "Rules added successfully.")
        elif protocol == "Both":
            command = "sudo ufw " + policy.lower() + " " + direction.lower() + " from " + source.lower() + " to " + destination.lower() + " port " + port.lower() + " proto tcp comment '" + rule_description + "'"
            try:
                os.system(command)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"{e}")
            command = "sudo ufw " + policy.lower() + " " + direction.lower() + " from " + source.lower() + " to " + destination.lower() + " port " + port.lower() + " proto udp comment '" + rule_description + "'"
            try:
                os.system(command)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"{e}")
            QMessageBox.information(self, "Note", "Rules added successfully.")
        else:
            command = "sudo ufw " + policy.lower() + " " + direction.lower() + " from " + source.lower() + " to " + destination.lower() + " port " + port.lower() + " proto " + protocol.lower() + " comment '" + rule_description + "'"
            try:
                os.system(command)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"{e}")
            QMessageBox.information(self, "Note", "Rules added successfully.")


class DeleteFirwallRule(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Delete_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Honeypot - Delete Rule")

        self.ui.delete_rule_close_button.clicked.connect(self.close)
        self.ui.delete_rule_button.clicked.connect(self.check_empty_fields)

    def check_empty_fields(self):
        delete_rule_content = self.ui.delete_rule_number_field.text().strip()

        if not delete_rule_content:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
        else:
            self.delete_rule()

    def delete_rule(self, accept=True):
        import subprocess
        delete_rule_content = self.ui.delete_rule_number_field.text()
        confirmation = "y\n" if accept else "n\n"
        command = ["sudo", "ufw", "delete", str(delete_rule_content)]

        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=confirmation)
        QMessageBox.information(self, "Note", "Rule deleted successfully!")




# ---------------------------------------------------------(IP Investigator Report Dialog)---------------------------------------------------------
class ReportIPAddress(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_report_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Honeypot - Report IP")
        self.setup_validation()

        # Normal Buttons
        self.ui.ip_report_close_button.clicked.connect(self.close_report)
        self.ui.report_ip_address_button.clicked.connect(self.check_report_field)

    def close_report(self):
        self.ui.reported_ip_field.clear()
        self.ui.dns_compromise_checkbox.setChecked(False)
        self.ui.dns_poisoning_checkbox.setChecked(False)
        self.ui.fraud_orders_checkbox.setChecked(False)
        self.ui.ddos_attack_checkbox.setChecked(False)
        self.ui.ftp_brute_force_checkbox.setChecked(False)
        self.ui.ping_of_death_checkbox.setChecked(False)
        self.ui.phishing_checkbox.setChecked(False)
        self.ui.fraud_voip_checkbox.setChecked(False)
        self.ui.open_proxy_checkbox.setChecked(False)
        self.ui.web_spam_checkbox.setChecked(False)
        self.ui.email_spam_checkbox.setChecked(False)
        self.ui.blog_spam_checkbox.setChecked(False)
        self.ui.vpn_ip_checkbox.setChecked(False)
        self.ui.port_scan_checkbox.setChecked(False)
        self.ui.hacking_checkbox.setChecked(False)
        self.ui.sql_injection_checkbox.setChecked(False)
        self.ui.spoofing_checkbox.setChecked(False)
        self.ui.brute_force_checkbox.setChecked(False)
        self.ui.bad_web_bot_checkbox.setChecked(False)
        self.ui.exploited_host_checkbox.setChecked(False)
        self.ui.web_app_attack_checkbox.setChecked(False)
        self.ui.ssh_checkbox.setChecked(False)
        self.ui.iot_targeted_checkbox.setChecked(False)
        self.close()

    def check_report_field(self):
        ip_field_content = self.ui.reported_ip_field.text().strip()
        if not ip_field_content:
            QMessageBox.warning(self, "Error", "Please fill in IP Address field at least.")
        else:
            self.report_ip_address()

    def report_ip_address(self):
        ip_address = self.ui.reported_ip_field.text()
        categories = []
        if self.ui.dns_compromise_checkbox.isChecked():
            categories.append(1)
        if self.ui.dns_poisoning_checkbox.isChecked():
            categories.append(2)
        if self.ui.fraud_orders_checkbox.isChecked():
            categories.append(3)
        if self.ui.ddos_attack_checkbox.isChecked():
            categories.append(4)
        if self.ui.ftp_brute_force_checkbox.isChecked():
            categories.append(5)
        if self.ui.ping_of_death_checkbox.isChecked():
            categories.append(6)
        if self.ui.phishing_checkbox.isChecked():
            categories.append(7)
        if self.ui.fraud_voip_checkbox.isChecked():
            categories.append(8)
        if self.ui.open_proxy_checkbox.isChecked():
            categories.append(9)
        if self.ui.web_spam_checkbox.isChecked():
            categories.append(10)
        if self.ui.email_spam_checkbox.isChecked():
            categories.append(11)
        if self.ui.blog_spam_checkbox.isChecked():
            categories.append(12)
        if self.ui.vpn_ip_checkbox.isChecked():
            categories.append(13)
        if self.ui.port_scan_checkbox.isChecked():
            categories.append(14)
        if self.ui.hacking_checkbox.isChecked():
            categories.append(15)
        if self.ui.sql_injection_checkbox.isChecked():
            categories.append(16)
        if self.ui.spoofing_checkbox.isChecked():
            categories.append(17)
        if self.ui.brute_force_checkbox.isChecked():
            categories.append(18)
        if self.ui.bad_web_bot_checkbox.isChecked():
            categories.append(19)
        if self.ui.exploited_host_checkbox.isChecked():
            categories.append(20)
        if self.ui.web_app_attack_checkbox.isChecked():
            categories.append(21)
        if self.ui.ssh_checkbox.isChecked():
            categories.append(22)
        if self.ui.iot_targeted_checkbox.isChecked():
            categories.append(23)

        comment = self.ui.ip_report_comment_field.toPlainText()
        if comment.strip() == "":
            comment = "Reported via API"

        status = IPInvestigator.report_ip(ip_address, categories, comment)
        if not status == None:
            QMessageBox.information(self, "Note", f"{ip_address} IP reported successfully.")
        else:
            QMessageBox.critical(self, "Error", "Invalid IP Address format.")

    def setup_validation(self):
        ipv4_regex = QRegularExpression("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
        ip_validator = QRegularExpressionValidator(ipv4_regex)
        self.ui.reported_ip_field.setValidator(ip_validator)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    mainwindow.show()
    sys.exit(app.exec())
