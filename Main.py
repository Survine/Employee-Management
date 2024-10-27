from Manager import Manager
from Development import Developer

# Create a Manager
manager = Manager(name="Nami", employee_id="M001", hourly_wage=50, hours_worked=170, team_size=3)

# Create Developers
dev1 = Developer(name="Aizen", employee_id="D001", hourly_wage=40, hours_worked=160, programming_language="Python")
dev2 = Developer(name="Subaru", employee_id="D002", hourly_wage=40, hours_worked=175, programming_language="JavaScript")

# Add team members to the Manager's team
manager.add_team_member(dev1)
manager.add_team_member(dev2)

# Add bonuses and deductions
manager.add_bonus(500)
manager.add_deduction(100)
dev1.add_bonus(300)
dev2.add_deduction(50)

# Print payslips
print("-----------------------------------")
print(manager.generate_payslip())
print("-----------------------------------")
print(dev1.generate_payslip())
print("-----------------------------------")
print(dev2.generate_payslip())
print("-----------------------------------")

# Calculate and print total team salary for the Manager
print(f"Total team salary for Manager {manager.name}: {manager.calculate_team_salaries():.2f}")
