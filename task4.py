# Nikolaos Bountouris-Voudouris
# Task 4: Load data from API, clean, analyse and visualize it

import requests
import pandas as pd
import matplotlib.pyplot as plt


def load_data(api_url):
    response = requests.get("https://my.api.mockaroo.com/company_data.json?key=2d8e46d0")
    data = response.json()
    df = pd.DataFrame(data)
    return df


def clean_data(df):
    # numeric columns
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce").fillna(0)
    df["bonus"] = pd.to_numeric(df["bonus"], errors="coerce").fillna(0)

    # text columns
    text_cols = ["first_name", "last_name", "email", "gender", "department"]
    for col in text_cols:
        df[col] = df[col].fillna("NA")

    return df


def add_total_salary(df):
    df["total_salary"] = df["salary"] + df["bonus"]
    return df


def show_basic_info(df):
    print("\nFirst rows")
    print("-" * 30)
    print(df.head())

    print("\nStatistics")
    print("-" * 30)
    print(df[["salary", "bonus", "total_salary"]].describe())


def show_department_counts(df):
    print("\nEmployees per department")
    print("-" * 30)
    print(df["department"].value_counts())


def show_subset(df):
    high_salary = df[df["salary"] > 5000]

    print("\nEmployees with salary > 5000")
    print("-" * 30)
    print(high_salary[["first_name", "last_name", "department", "salary"]].head(10))


def plot_data(df):
    # Plot 1: employees per department
    df["department"].value_counts().plot(kind="bar")
    plt.title("Employees per Department")
    plt.xlabel("Department")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plot 2: salary distribution
    plt.hist(df["salary"], bins=15)
    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()


def main():
    api_url = "https://my.api.mockaroo.com/company_data.json?key=2d8e46d0"

    df = load_data(api_url)
    df = clean_data(df)
    df = add_total_salary(df)

    show_basic_info(df)
    show_department_counts(df)
    show_subset(df)
    plot_data(df)


if __name__ == "__main__":
    main()