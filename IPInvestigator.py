import requests
import json
from PySide6.QtWidgets import QMessageBox

ABUSEDB_API_KEY = "your API key"
BASE_URL = "https://api.abuseipdb.com/api/v2/"

class IPInvestigator:
    def check_ip(ip_address, max_age_in_days=90):
        url = f"{BASE_URL}check"
        headers = {
            "Accept": "application/json",
            "Key": ABUSEDB_API_KEY,
        }
        params = {
            "ipAddress": ip_address,
            "maxAgeInDays": max_age_in_days,
        }
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(None, "Error", f"Error checking IP: {e}")
            if 'response' in locals() and response is not None:
                try:
                    error_json = response.json()
                    QMessageBox.critical(None, "Error", json.dumps(error_json, indent=4))
                except json.JSONDecodeError:
                    QMessageBox.critical(None, "Error", f"Response status code: {response.status_code}")
            return None

    def report_ip(ip_address, categories, comment):
        url = f"{BASE_URL}report"
        headers = {
            "Accept": "application/json",
            "Key": ABUSEDB_API_KEY,
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "ip": ip_address,
            "categories": ",".join(map(str, categories)),
            "comment": comment,
        }

        try:
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error reporting IP: {e}")
            if response is not None:
                try:
                    error_json = response.json()
                    print(json.dumps(error_json, indent=4))
                except:
                    print(f"Response status code: {response.status_code}")
            return None
