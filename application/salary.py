from accounting.db.people import get_employees


def calculate_salary():
    salary = f"Зарплата расчитана для {get_employees()}"
    return salary