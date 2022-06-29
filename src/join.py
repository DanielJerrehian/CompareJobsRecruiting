import os
import requests


class Join:
    def __init__(self):
        self.headers = None
        self.request = requests
        self.base_url = f"https://api.join.com/v1"
        self.response = None
        
    def create_headers(self):
        self.headers = {
            "Accept": "application/json",
            "Authorization": os.environ.get("JOIN_API_KEY")
        }
        
    def get_all_jobs(self):
        self.response = self.request.get(url=f"{self.base_url}/jobs", headers=self.headers)