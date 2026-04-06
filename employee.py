# Nikolaos Bountouris-Voudouris
# Employee class used for Task 3

class Employee:
    company_name = "Workforce Analytics Ltd"

    def __init__(self, emp_id, first_name, last_name, email, gender, department, salary, bonus, date_of_birth):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.department = department
        self.salary = salary
        self.bonus = bonus
        self.date_of_birth = date_of_birth

    def __str__(self):
        return (
            f"ID: {self.emp_id}\n"
            f"Name: {self.first_name} {self.last_name}\n"
            f"Email: {self.email}\n"
            f"Gender: {self.gender}\n"
            f"Department: {self.department}\n"
            f"Salary: {self.salary}\n"
            f"Bonus: {self.bonus}\n"
            f"Date of Birth: {self.date_of_birth}\n"
            f"Company: {Employee.company_name}"
        )

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_total_pay(self):
        return self.salary + self.bonus