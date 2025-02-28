#!/usr/bin/env python3
import requests

def check_google_drive():
    url = "https://drive.google.com"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"Google Drive is accessible! (Status Code: {response.status_code})")
        else:
            print(f" Google Drive returned a different status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Google Drive is BLOCKED or unreachable: {e}")

check_google_drive()
