# Nikolaos Bountouris-Voudouris
# Task 1: Read employee data from a csv file, sort it, and display selected rows.

import os


def ask_for_file(default_file):
    while True:
        file_name = input(f"Enter csv file name [{default_file}]: ").strip()

        if file_name == "":
            file_name = default_file

        if os.path.exists(file_name):
            return file_name

        print("File not found. Please try again.")


def ask_for_number_of_rows():
    while True:
        user_input = input("How many rows do you want to display (0-100)? ").strip()

        try:
            number = int(user_input)
            if 0 <= number <= 100:
                return number
            else:
                print("Please enter a number from 0 to 100.")
        except ValueError:
            print("Please enter a valid integer.")


def read_csv_file(file_name):
    rows = []

    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines[1:]:
        line = line.strip()
        if line != "":
            row = line.split(",")
            rows.append(row)

    return rows


def sort_rows(rows):    
    return sorted(rows, key=lambda row: (row[5], row[2]))
# Sort by department first and then by last name. This helps the user see employees grouped by department and ordered alphabetically inside each group.

def show_rows(rows, how_many):
    print("-" * 120)
    print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Email':<30} {'Gender':<10} {'Department':<20} {'Salary':<10} {'Bonus':<8}")
    print("-" * 120)

    for row in rows[:how_many]:
        employee_id = row[0]
        first_name = row[1]
        last_name = row[2]
        email = row[3]
        gender = row[4]
        department = row[5]
        salary = row[6]
        bonus = row[7] if row[7] != "" else "NA"

        print(f"{employee_id:<5} {first_name:<15} {last_name:<15} {email:<30} {gender:<10} {department:<20} {salary:<10} {bonus:<8}")


def main():
    default_file = "companyData.csv"

    file_name = ask_for_file(default_file)
    rows = read_csv_file(file_name)
    sorted_rows = sort_rows(rows)

    how_many = ask_for_number_of_rows()
    show_rows(sorted_rows, how_many)


if __name__ == "__main__":
    main()