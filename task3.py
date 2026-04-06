# Nikolaos Bountouris-Voudouris
# Task 3: Load employees from a json file and provide a menu for searching and filtering.

import json
from employee import Employee


def load_employees_from_json(file_name):
    employees = []

    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        bonus_value = item["bonus"]

        if bonus_value == "" or bonus_value is None:
            bonus_value = 0

        employee = Employee(
            item["id"],
            item["first_name"],
            item["last_name"],
            item["email"],
            item["gender"],
            item["department"],
            int(item["salary"]),
            int(bonus_value),
            item["dateOfBirth"]
        )

        employees.append(employee)

    return employees


def display_all_employees(employees):
    for employee in employees:
        print(employee)
        print("-" * 50)


def search_by_attribute(employees, attribute_name, search_value):
    matching_employees = []

    for employee in employees:
        if hasattr(employee, attribute_name):
            value = getattr(employee, attribute_name)

            if str(value).lower() == search_value.lower():
                matching_employees.append(employee)

    return matching_employees


def display_numeric_filter(employees, attribute_name, limit_value):
    matching_employees = []

    for employee in employees:
        if hasattr(employee, attribute_name):
            value = getattr(employee, attribute_name)

            if isinstance(value, (int, float)) and value > limit_value:
                matching_employees.append(employee)

    return matching_employees


def show_menu():
    print("\nMenu")
    print("1. Display all the information")
    print("2. Search by attribute")
    print("3. Display all rows with a numeric attribute more than a value")
    print("4. Exit")


def main():
    file_name = "companyData.json"
    employees = load_employees_from_json(file_name)

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            display_all_employees(employees)

        elif choice == "2":
            print("\nAvailable attributes:")
            print("emp_id, first_name, last_name, email, gender, department, salary, bonus, date_of_birth")

            attribute_name = input("Enter attribute name: ").strip()
            search_value = input("Enter the value you want to search for: ").strip()

            results = search_by_attribute(employees, attribute_name, search_value)

            if results:
                for employee in results:
                    print(employee)
                    print("-" * 50)
            else:
                print("No matching employees found.")

        elif choice == "3":
            print("\nNumeric attributes: emp_id, salary, bonus")

            attribute_name = input("Enter numeric attribute name: ").strip()

            try:
                limit_value = float(input("Enter minimum value: ").strip())
                results = display_numeric_filter(employees, attribute_name, limit_value)

                if results:
                    for employee in results:
                        print(employee)
                        print("-" * 50)
                else:
                    print("No matching employees found.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Program closed.")
            break

        else:
            print("Invalid option. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()