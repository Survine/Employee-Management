class Employee:
    def __init__(self, name: str, employee_id: str, hourly_wage: float, hours_worked: float):
        self.name = name
        self.employee_id = employee_id
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonuses = 0.0
        self.deductions = 0.0

    def calculate_monthly_salary(self):
        base_salary = self.hourly_wage * min(self.hours_worked, 160)
        overtime_pay = 0.0
        if self.hours_worked > 160:
            overtime_hours = self.hours_worked - 160
            overtime_pay = overtime_hours * self.hourly_wage * 1.5
        return base_salary + overtime_pay + self.bonuses - self.deductions

    def add_bonus(self, bonus: float):
        self.bonuses += bonus

    def add_deduction(self, deduction: float):
        self.deductions += deduction

    def generate_payslip(self):
        return (f"Employee ID: {self.employee_id}\nName: {self.name}\n"
                f"Monthly Salary: {self.calculate_monthly_salary():.2f}\n"
                f"Bonuses: {self.bonuses:.2f}\nDeductions: {self.deductions:.2f}")
