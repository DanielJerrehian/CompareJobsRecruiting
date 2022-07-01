class CompareJobBoards:
    def __init__(self, green_house_jobs : list = [], join_jobs : list = []):
        self.green_house_jobs = green_house_jobs
        self.join_jobs = join_jobs
        self.green_house_job_names = []
        self.join_job_names = []
        self.jobs_missing_from_greenhouse = []

    def create_green_house_job_name_list(self):
        for job in self.green_house_jobs["jobs"]:
            self.green_house_job_names.append(job["title"])
            
    def create_join_job_name_list(self):
        for job in self.join_jobs:
            self.join_job_names.append(job["title"])
            
    def compare_jobs(self):
        for job_title in self.join_job_names:
            if job_title not in self.green_house_job_names:
                self.jobs_missing_from_greenhouse.append(job_title)
                