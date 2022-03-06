from application.salary import calculate_salary
from db.people import get_employees
from datetime import datetime
from datetime import date

if __name__ == '__main__':
    print(f'{calculate_salary()} на период {datetime.now()}')

