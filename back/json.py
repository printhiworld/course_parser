import json

from back.models import JobData


class JobDataJSON(JobData):
    path: str = 'file.json'

    def read_data(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def write_data(self, dict):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(dict, file, ensure_ascii=False, indent=4)

    def delete_job(self, job_id):
        data = self.read_data()
        data = [job for job in data if job.get('id') != job_id]
        self.write_data(data)

    def add_job(self, job_dict):
        dict = self.read_data()
        dict.append(job_dict)
        self.write_data(dict)

    def get_job(self, filters):
        data = self.read_data()
        if not filters:
            return data
        result = []
        for i in data:
            if filters in i.values():
                result.append(i)
        return result

