def add_employee(employee):
    employees.append(employee)
    print("Employee Created Successfully!")


def search(emp_id):
    for employee in employees:
        if employee["ID"] == emp_id:
            return employee
    return None


def assign_role(employee):
    employee["Role"] = input("Enter Role: ")
    employee["Salary"] = int(input("Enter Salary: "))
    print("Employee details updated successfully!")


def transfer_salary(employee):
    # Ensure a salary has been set before attempting to add to balance
    if employee["Salary"] is None:
        print("Cannot transfer salary: No salary or role has been assigned yet!")
    else:
        employee["Balance"] += employee["Salary"]
        print(f"Salary Transfer Success! New Balance: {employee['Balance']}")


def display(employee):
    print("\n--- Employee Details ---")
    for key, value in employee.items():
        print(f"{key}: {value}")


options = """
Options:
1. Create an employee account
2. Assign a role to employee
3. Transfer salary to employee
4. Display employee details
5. Close application
"""

employees = []

while True:
    print("\nEmployee Management System")
    print(options)

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    match choice:
        case 1:
            print("\nCreating Employee:")
            name = input("Name: ")
            age = int(input("Age: "))
            dob = input("DOB (DD/MM/YYYY): ")
            gender = input("Gender: ")

            # Generates IDs like E1, E2, E3 based on list size
            employee = {
                "ID": "E" + str(len(employees) + 1),
                "Name": name,
                "Age": age,
                "DOB": dob,
                "Gender": gender,
                "Role": "not yet assigned",
                "Salary": None,
                "Balance": 0
            }

            add_employee(employee)

        case 2:
            print("\nAssigning Role:")
            emp_id = input("Enter Employee ID (e.g., E1): ")
            employee = search(emp_id)

            if employee is None:
                print("Employee Not Found")
            else:
                assign_role(employee)

        case 3:
            print("\nTransferring Salary:")
            emp_id = input("Enter Employee ID (e.g., E1): ")
            employee = search(emp_id)

            if employee is None:
                print("Employee Not Found")
            else:
                transfer_salary(employee)

        case 4:
            print("\nDisplaying Employee Details:")
            emp_id = input("Enter Employee ID (e.g., E1): ")
            employee = search(emp_id)

            if employee is None:
                print("Employee Not Found")
            else:
                display(employee)

        case 5:
            print("Application Closed. Goodbye!")
            break

        case _:
            print("Invalid option. Try again.")

    print("=" * 30)
