# -*- coding:utf-8
from application.db.people import get_employees
from application.salary import calculate_salary


if __name__ == '__main__':
    get_employees()
    calculate_salary()
