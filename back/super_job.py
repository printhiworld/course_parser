import requests
from dotenv import load_dotenv
import os
from back.models import JobAPI, Vacancy

api_key = os.environ.get("API_KEY")


class SuperJob(JobAPI):
    load_dotenv()
    api_key = os.environ.get("API_KEY")
    headers = {
        "Host": "api.superjob.ru",
        "X-Api-App-Id": api_key,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    url = "https://api.superjob.ru/2.0"

    def get_vacancies(self):
        """показывает вакансии на superjob"""
        vacancies = []
        response = requests.get(f'{self.url}/vacancies', headers=self.headers).json()['objects']
        for i in response:
            if i.get('payment_from') == 0:
                salary = i.get('payment_to', -1)
            else:
                salary = i.get('payment_from', -1)
            vacancy = Vacancy(i.get('id', '-'), i.get('profession', '-'), salary, i.get('candidat', '-'), i.get('link', '-'))
            vacancies.append(vacancy)
        return vacancies

