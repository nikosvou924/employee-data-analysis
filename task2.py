# Nikolaos Bountouris-Voudouris
# Task 2: Read csv using csv module, use dictionaries,
# count employees per department and calculate statistics

import csv
from task1 import ask_for_file, ask_for_number_of_rows


def read_csv_as_dicts(file_name):
    data = []

    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data


def count_departments(data):
    department_counts = {}

    for employee in data:
        dept = employee["department"]

        if dept not in department_counts:
            department_counts[dept] = 1
        else:
            department_counts[dept] += 1

    return department_counts


def calculate_statistics(data):
    total_employees = len(data)
    total_salary = 0

    for employee in data:
        salary = int(employee["salary"])
        total_salary += salary

    average_salary = total_salary / total_employees

    return total_employees, total_salary, average_salary


def display_department_counts(department_counts, limit):
    print("\nDepartment      #Employees")
    print("----------------------------")

    sorted_depts = sorted(department_counts.items(), key=lambda x: x[0])

    for dept, count in sorted_depts[:limit]:
        print(f"{dept:<15} {count}")


def main():
    default_file = "companyData.csv"

    file_name = ask_for_file(default_file)

    data = read_csv_as_dicts(file_name)

    department_counts = count_departments(data)

    limit = ask_for_number_of_rows()

    display_department_counts(department_counts, limit)

    total_employees, total_salary, average_salary = calculate_statistics(data)

    print("\nStatistics")
    print("----------------------------")
    print(f"Total employees: {total_employees}")
    print(f"Total salary: {total_salary}")
    print(f"Average salary: {average_salary:.2f}")


if __name__ == "__main__":
    main()