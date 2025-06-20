from fpdf import FPDF
import os

class PDFReportGeneration(FPDF):
    def main(self, company_or_client_name = ""):
        pdf = PDFReportGeneration("P", "mm", "A4")
        pdf.set_auto_page_break(auto=True, margin=25)
        pdf.add_page()
        pdf.add_font("DejaVuSans_bold", fname="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
        pdf.add_font("DejaVuSans", fname="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
        pdf.set_font(family="Times", style="B", size=36)
        pdf.image("path/icons/logo without background.png", 75, 50, 60, 60)
        pdf.text(60, 135, "Honeypot Report")
        pdf.set_font(family="Times", size=18)
        pdf.text(45, 155, "Incident Response: Honeypot Data To Analysis")
        pdf.set_font(family="Times", style="B", size= 18)
        pdf.text(66, 175, f"Creation Date: {pdf.today_date()}")
        pdf.text(85, 190, "Prepared for:")
        prepared_for_width = pdf.get_string_width("Prepared for:")
        page_width = pdf.w - 2 * pdf.l_margin 
        max_width_company_client_name = page_width 
        text_width = pdf.get_string_width(company_or_client_name)
        start_x_company_client_name = pdf.l_margin + (page_width - text_width) / 2
        start_y_company_client_name = 200 
        pdf.set_xy(start_x_company_client_name - 4, start_y_company_client_name)
        pdf.multi_cell(max_width_company_client_name, 7, company_or_client_name, align="L")
        pdf.text(85, 220, "Prepared by:")
        pdf.text(81, 235, "Honeypot Team")
        chapter_1 = pdf.add_link()
        chapter_2 = pdf.add_link()
        chapter_3 = pdf.add_link()
        chapter_4 = pdf.add_link()
        chapter_5 = pdf.add_link()
        chapter_6 = pdf.add_link()
        os_version_date_time = pdf.add_link()
        uptime = pdf.add_link()
        logged_on_users = pdf.add_link()
        mounted_drives = pdf.add_link()
        check_swap_file = pdf.add_link()
        active_connections = pdf.add_link()
        opened_ports = pdf.add_link()
        route_table = pdf.add_link()
        arp_table = pdf.add_link()
        current_running_processes = pdf.add_link()
        process_tree = pdf.add_link()
        current_running_services = pdf.add_link()
        current_users_scheduled_tasks = pdf.add_link()
        current_root_scheduled_tasks = pdf.add_link()
        clipboard_contents = pdf.add_link()
        collect_logs = pdf.add_link()
        pdf.add_page()
        pdf.cell(0, 10, "BRIEF CONTENTS", align="C")
        pdf.set_font("Times", size=16)
        pdf.ln(30)
        pdf.cell(0, 10, "Chapter 1: System Information: ..........................................................................", align="L", link=chapter_1)
        pdf.ln(15)
        pdf.cell(0, 10, "Chapter 2: Disk and Storage: ..............................................................................", align="L", link= chapter_2)
        pdf.ln(15)
        pdf.cell(0, 10, "Chapter 3: Network Information: .......................................................................", align="L", link=chapter_3)
        pdf.ln(15)
        pdf.cell(0, 10, "Chapter 4: Process Management: .......................................................................", align="L", link=chapter_4)
        pdf.ln(15)
        pdf.cell(0, 10, "Chapter 5: User Specific Information: ...............................................................", align="L", link=chapter_5)
        pdf.ln(15)
        pdf.cell(0, 10, "Chapter 6: Logging: ...........................................................................................", align="L", link=chapter_6)
        pdf.ln(15)

        pdf.add_page()
        pdf.set_font(family="Times", style="B", size= 18)
        pdf.cell(0, 10, "CONTENTS IN DETAIL", align="C")
        pdf.ln(30)



        pdf.bold_title_text("Chapter 1: System Information: ........................................................", chapter_1)
        pdf.index_content_with_linker("        OS version, date, time: ................................................................................", os_version_date_time)
        pdf.index_content_with_linker("        Uptime: .......................................................................................................", uptime)
        pdf.index_content_with_linker("        Logged on users: .........................................................................................", logged_on_users)

        pdf.bold_title_text("Chapter 2: Disk and Storage: .............................................................", chapter_2)
        pdf.index_content_with_linker("        Mounted drives: ..........................................................................................", mounted_drives)
        pdf.index_content_with_linker("        Check swap file: .........................................................................................", check_swap_file)

        pdf.bold_title_text("Chapter 3: Network Information: .....................................................", chapter_3)
        pdf.index_content_with_linker("        Active connections: .....................................................................................", active_connections)
        pdf.index_content_with_linker("        Opened ports: ..............................................................................................", opened_ports)
        pdf.index_content_with_linker("        Route table: .................................................................................................", route_table)
        pdf.index_content_with_linker("        ARP route: ..................................................................................................", arp_table)

        pdf.bold_title_text("Chapter 4: Process Management: .....................................................", chapter_4)
        pdf.index_content_with_linker("        Current running process: ............................................................................", current_running_processes)
        pdf.index_content_with_linker("        Process tree: ................................................................................................", process_tree)
        pdf.index_content_with_linker("        Current running services: ............................................................................", current_running_services)

        pdf.bold_title_text("Chapter 5: User Specific Information: ..............................................", chapter_5)
        pdf.index_content_with_linker("        Current user's scheduled tasks: ....................................................................", current_users_scheduled_tasks)
        pdf.index_content_with_linker("        Root user's scheduled tasks: ........................................................................", current_root_scheduled_tasks)
        pdf.index_content_with_linker("        Clipboard contents: .....................................................................................", clipboard_contents)

        pdf.bold_title_text("Chapter 6: Logging: ..............................................................................", chapter_6)
        pdf.index_content_with_linker("        Collect logs: ...................................................................................................", collect_logs)

        pdf.add_page()
        pdf.set_font(family="Times", style="B", size= 18)
        pdf.bold_title_text("Chapter 1: System Information:", chapter_1)


        pdf.italic_subtitle_with_linker("OS version, date, time:", os_version_date_time)
        pdf.set_font("DejaVuSans", size=12)
        process = os.popen("hostnamectl")
        output = process.read()
        process.close()
        process2 = os.popen("date")
        output2 = process2.read()
        process2.close()
        output += "Date and Time: " + output2
        del output2
        pdf.multi_cell(0, 7, text=output)
        pdf.ln(15)

        pdf.italic_subtitle_with_linker("Uptime:", uptime)
        pdf.set_font("DejaVuSans", size=12)
        process = os.popen("uptime")
        output = process.read()
        process.close()
        pdf.multi_cell(0, 7, text=output)
        pdf.ln(15)

        pdf.italic_subtitle_with_linker("Logged on users:", logged_on_users)
        pdf.set_font("DejaVuSans", size=12)
        process = os.popen("w")
        output = process.read()
        process.close()
        pdf.multi_cell(0, 7, text=output)
        pdf.ln(15)

        pdf.set_font(family="DejaVuSans_bold", size= 18)
        pdf.bold_title_text("Chapter 2: Disk and Storage:", chapter_2)


        pdf.italic_subtitle_with_linker("Mounted drives:", mounted_drives)
        pdf.set_font("DejaVuSans", size=12)
        process = os.popen("mount")
        output = process.read()
        process.close()
        pdf.multi_cell(0, 7, text=output)
        pdf.ln(15)

        pdf.italic_subtitle_with_linker("Check swap file:", check_swap_file)
        pdf.set_font("DejaVuSans", size=12)
        process = os.popen("free -h")
        output = process.read()
        process.close()
        pdf.multi_cell(0, 7, text=output)
        pdf.multi_cell(0, 7, "---------------------------------------------------------------------------------------------------------------------------")
        pdf.ln(15)
        process = os.popen("sudo swapon --show")
        output = process.read()
        process.close()
        pdf.multi_cell(0, 7, text=output)
        pdf.ln(15)

        pdf.set_font(family="DejaVuSans_bold", size= 18)
        pdf.bold_title_text("Chapter 3: Network Information:", chapter_3)


        pdf.italic_subtitle_with_linker("Active connections:", active_connections)
        pdf.set_font("DejaVuSans", size=12)
        process = os.popen("sudo netstat -tunap | grep -v LISTEN")
        output = process.read()
        process.close()
        pdf.multi_cell(0, 7, text=output)
        pdf.ln(15)

        pdf.italic_subtitle_with_linker("Opened ports:", opened_ports)
        pdf.set_font("DejaVuSans", size=12)
        process = os.popen("sudo netstat -tulnp | grep LISTEN")
        output = process.read()
        process.close()
        pdf.multi_cell(0, 7, text=output)
        pdf.ln(15)

        pdf.italic_subtitle_with_linker("Route table:", route_table)
        pdf.set_font("DejaVuSans", size=12)
        process = os.popen("sudo route -n")
        output = process.read()
        process.close()
        pdf.multi_cell(0, 7, text=output)
        pdf.ln(15)

        pdf.italic_subtitle_with_linker("ARP route:", arp_table)
        pdf.set_font("DejaVuSans", size=12)
        process = os.popen("arp -n")
        output = process.read()
        process.close()
        pdf.multi_cell(0, 7, text=output)
        pdf.ln(15)

        pdf.set_font(family="DejaVuSans_bold", size= 18)
        pdf.bold_title_text("Chapter 4: Process Management:", chapter_4)


        pdf.italic_subtitle_with_linker("Current running process:", current_running_processes)
        pdf.set_font("DejaVuSans", size=12)
        process = os.popen("ps aux")
        output = process.read()
        process.close()
        pdf.multi_cell(0, 7, text=output)
        pdf.ln(15)

        pdf.add_page(orientation="L")
        pdf.italic_subtitle_with_linker("Process tree:", process_tree)
        pdf.set_font("DejaVuSans", size=12)
        process = os.popen("pstree -p")
        output = process.read()
        process.close()
        pdf.multi_cell(0, 7, text=output)
        pdf.ln(15)

        pdf.add_page()
        pdf.italic_subtitle_with_linker("Current running services:", current_running_services)
        pdf.set_font("DejaVuSans", size=12)
        process = os.popen("systemctl list-units --type=service --no-pager")
        output = process.read()
        process.close()
        pdf.multi_cell(0, 7, text=output)
        pdf.ln(15)

        pdf.set_font(family="DejaVuSans_bold", size= 18)
        pdf.bold_title_text("Chapter 5: User Specific Information:", chapter_5)


        pdf.italic_subtitle_with_linker("Current user's scheduled tasks:", current_users_scheduled_tasks)
        pdf.set_font("DejaVuSans", size=12)
        process = os.popen("cat /etc/crontab")
        output = process.read()
        process.close()
        pdf.multi_cell(0, 7, text=output)
        pdf.ln(15)

        pdf.italic_subtitle_with_linker("Root user's scheduled tasks:", current_root_scheduled_tasks)
        pdf.set_font("DejaVuSans", size=12)
        process = os.popen("sudo crontab -l -u root")
        output = process.read()
        process.close()
        pdf.multi_cell(0, 7, text=output)
        pdf.ln(15)

        pdf.italic_subtitle_with_linker("Clipboard contents:", clipboard_contents)
        pdf.set_font("DejaVuSans", size=12)
        process = os.popen("xsel -b -o")
        output = process.read()
        process.close()
        pdf.multi_cell(0, 7, text=output)
        pdf.ln(15)

        pdf.set_font(family="DejaVuSans_bold", size= 18)
        pdf.bold_title_text("Chapter 6: Logging:", chapter_5)


        pdf.italic_subtitle_with_linker("Collect logs:", collect_logs)
        pdf.set_font("DejaVuSans", size=12)
        process = os.popen("journalctl -b --no-pager")
        output = process.read()
        process.close()
        pdf.multi_cell(0, 7, text=output)
        pdf.ln(15)

        pdf.output("path/Evidence.pdf")

    def today_date(self):
        import datetime
        self.now = datetime.datetime.now()
        self.formatted_datetime = self.now.strftime("%Y-%m-%d")
        return self.formatted_datetime

    def bold_title_text(self, text="None", link="None"):
        self.set_font(family="Times", style="B", size= 18)
        self.cell(0, 10, text, link=link, align="L")
        self.linker(link)
        self.ln(15)


    def index_content(self, text="None"):
        self.set_font("DejaVuSans", size=16)
        self.ln(15)
        self.cell(0, 10, text, align="L")


    def index_content_with_linker(self, text="None", link="None"):
        self.set_font("Times", size=16)
        self.cell(0, 10, text, link=link, align="L")
        self.ln(15)
        self.linker(link)

    def italic_subtitle_with_linker(self, text="None", link="None"):
        self.add_font("DejaVuSans", fname="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
        self.set_font(family="DejaVuSans", size=16)
        self.cell(0, 10, text, link=link, align="L")
        self.ln(15)
        self.linker(link)

    def linker(self, link):
        self.set_link(link)
    
    def footer(self):
        if self.page_no() > 4:
            self.set_y(-15)
            self.set_font('helvetica', "I", 8)
            self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align="C")

       
