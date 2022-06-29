import requests


class GreenHouse:
    def __init__(self):
        self.headers = None
        self.request = requests
        self.base_url = f"https://boards-api.greenhouse.io/v1/boards/kiperformance"
        self.response = None
        
    def create_headers(self):
        self.headers = {
            "Accept": "application/json",
        }
        
    def get_all_jobs(self):
        self.response = self.request.get(url=f"{self.base_url}/jobs", headers=self.headers)