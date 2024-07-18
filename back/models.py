import dataclasses
from abc import abstractmethod, ABC


class JobAPI(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


@dataclasses.dataclass
class Vacancy:
    id: int
    name: str
    salary: str
    description: str
    url: str

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary


class JobData(ABC):

    @abstractmethod
    def add_job(self, job_data):
        pass

    def get_jobs(self):
        pass

    @abstractmethod
    def delete_job(self, job_id):
        pass

