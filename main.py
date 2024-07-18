from back.hh import HHJob
from back.json import JobDataJSON
from back.super_job import SuperJob


def interaction():
    hh = HHJob()
    super = SuperJob()
    json_d = JobDataJSON()
    while True:
        print('1) Посмотреть вакансии на hh')
        print('2) Посмотреть вакансии на super job')
        print('3) Создать вакансию')
        print('4) Удалить вакансию')
        print('5) Посмотреть вакансии в файле')
        print('Ведите любой символ чтобы выйти')
        action = input()
        if action == '1':
            vacancies = hh.get_vacancies()
            for vacancy in vacancies:
                print(vacancy)
        elif action == '2':
            vacancies = super.get_vacancies()
            for vacancy in vacancies:
                print(vacancy)
        elif action == '5':
            print('Введите ключевые значения для поиска')
            filter = input()
            vacancies = json_d.get_job(filter)
            for vacancy in vacancies:
                print(vacancy)
        elif action == '4':
            idi = input('id удаляемой вакансии')
            json_d.delete_job(idi)
        elif action == '3':
            id = input('id вакансии')
            name = input('название')
            salary = input('зп')
            desc = input('описание ')
            url = input('ссылка')
            dict = {'id': id, 'name' : name, 'salary': salary, 'desc': desc, 'url': url}
            json_d.add_job(dict)
        else:
            break

if __name__ == "__main__":
    interaction()
