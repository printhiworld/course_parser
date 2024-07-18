import requests
import os
from back.models import JobAPI, Vacancy

api_key = os.environ.get("API_KEY")


class HHJob(JobAPI):
    url = "https://api.hh.ru"

    def get_vacancies(self):
        vacancies = []
        response = requests.get(f'{self.url}/vacancies').json()['items']
        for i in response:
            salary = i.get("salary")
            try:
                salary1 = salary.get('to', 0)
            except:
                continue
            vacancy = Vacancy(i.get('id', '-'), i.get('name', '-'), salary1, i.get('snippet', '-'), i.get('url', '-'))
            vacancies.append(vacancy)
        return vacancies
