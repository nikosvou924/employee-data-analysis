# Nikolaos Bountouris-Voudouris
# Task 3 test file for the Employee class

from employee import Employee


def main():
    employee1 = Employee(
        1,
        "Nikos",
        "Voudouris",
        "nikos@example.com",
        "Male",
        "Engineering",
        2500,
        300,
        "2002-05-10"
    )

    employee2 = Employee(
        2,
        "Maria",
        "Papadaki",
        "maria@example.com",
        "Female",
        "Marketing",
        2200,
        250,
        "2001-11-20"
    )

    print(employee1)
    print("-" * 40)
    print(employee2)
    print("-" * 40)

    print("Employee 1 full name:", employee1.get_full_name())
    print("Employee 1 total pay:", employee1.get_total_pay())

    print("Employee 2 full name:", employee2.get_full_name())
    print("Employee 2 total pay:", employee2.get_total_pay())


if __name__ == "__main__":
    main()