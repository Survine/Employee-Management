from Employee import Employee

class Developer(Employee):
    def __init__(self, name: str, employee_id: str, hourly_wage: float, hours_worked: float, programming_language: str):
        super().__init__(name, employee_id, hourly_wage, hours_worked)
        self.programming_language = programming_language
