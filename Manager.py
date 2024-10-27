from Employee import Employee

class Manager(Employee):
    def __init__(self, name: str, employee_id: str, hourly_wage: float, hours_worked: float, team_size: int):
        super().__init__(name, employee_id, hourly_wage, hours_worked)
        self.team_size = team_size
        self.team_members = []

    def add_team_member(self, employee):
        """Add an employee to the manager's team"""
        self.team_members.append(employee)

    def calculate_team_salaries(self):
        """Calculate the total salary of all team members."""
        total_salary = sum(member.calculate_monthly_salary() for member in self.team_members)
        return total_salary
