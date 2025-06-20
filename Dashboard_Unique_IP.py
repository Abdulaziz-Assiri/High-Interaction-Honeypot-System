import subprocess
import threading
import time
from PySide6.QtCore import Signal, QObject

class Dashboard_Unique_IP(QObject):
    output_received = Signal(str)
    started = Signal()
    finished = Signal()

    def __init__(self, output_signal=None):
        super().__init__()
        self.process = None
        self.output_thread = None
        self.running = False
        self.output_buffer = []
        if output_signal:
            self.output_received.connect(output_signal)

    def _read_output(self, stdout):
        for line in iter(stdout.readline, ''):
            cleaned_line = line.strip()
            self.output_received.emit(cleaned_line)
            self.output_buffer.append(cleaned_line)
        stdout.close()
        self.running = False
        if self.process:
            self.process.wait()
        self.finished.emit()

    def start_sniffing(self):
        if self.running:
            print("Sniffing is already running.")
            return

        try:
            command = ["sudo", "python3", "path/Unique_IP.py"]
            self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
            self.running = True
            self.started.emit()

            self.output_thread = threading.Thread(target=self._read_output, args=(self.process.stdout,))
            self.output_thread.daemon = True
            self.output_thread.start()

            error_thread = threading.Thread(target=self._read_output, args=(self.process.stderr,))
            error_thread.daemon = True
            error_thread.start()

        except FileNotFoundError:
            print("Error: Sniffer.py not found.")
            self.finished.emit()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            self.finished.emit()

    def get_current_output(self):
        return list(self.output_buffer)

    def stop_sniffing(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.running = False
            if self.output_thread and self.output_thread.is_alive():
                self.output_thread.join(timeout=5)
        else:
            print("Sniffing process is not running.")
        self.finished.emit()
