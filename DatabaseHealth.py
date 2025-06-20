import hashlib
import shelve
import os.path
from PySide6.QtWidgets import QMessageBox

class DatabaseHealth:
    def check_for_path(self, parent, path):
        if os.path.exists(path):
            if os.path.isfile(path):
                self.generate_hash_value(parent, path)
            elif os.path.isdir(path):
                QMessageBox.critical(parent, "Error", f"The path provided ('{path}') is a directory. Please specify a file path.")
        else:
            QMessageBox.critical(parent, "Error", "The specified path does not exist.")


    def generate_hash_value(self, parent, path):
        with open(path,'rb') as f:
            lines = f.read()
            hash_value = hashlib.sha256(lines).hexdigest()
        self.save_hash(parent, hash_value, path)

    def save_hash(self, parent, hash_value, path):
        hashes_database = shelve.open('hashes.db')
        hashes_database[path] = hash_value
        hashes_database.close()
        QMessageBox.information(parent, "Notification", "Hash Added successfully!")


    def check_hash(self, parent, path):
        content = shelve.open('hashes.db')
        saved_hash_value = content[path]
        with open(path,'rb') as f:
            lines = f.read()
            hash_value = hashlib.sha256(lines).hexdigest()
        if saved_hash_value == hash_value:
            QMessageBox.information(parent, "Notification", "No changes detected.")
        else:
            QMessageBox.information(parent, "Notification", "File modified.")
        content.close()    
