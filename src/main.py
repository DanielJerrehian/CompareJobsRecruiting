from dotenv import load_dotenv
from pprint import pprint

from src.green_house import GreenHouse
from src.join import Join
from src.compare_job_boards import CompareJobBoards


def main():
    load_dotenv(dotenv_path=".env")
    
    green_house = GreenHouse()
    green_house.create_headers()
    green_house.get_all_jobs()
    green_house_jobs_dict = green_house.response.json()
    
    join = Join()
    join.create_headers()
    join.get_all_jobs()
    join_jobs_dict = join.response.json()
    
    comparison = CompareJobBoards(green_house_jobs=green_house_jobs_dict, join_jobs=join_jobs_dict)
    comparison.create_green_house_job_name_list()
    comparison.create_join_job_name_list()
    comparison.compare_jobs()

    pprint(comparison.jobs_missing_from_greenhouse)
