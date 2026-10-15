employees = {}


def add_employee():
    print("\n--- Add Employee ---")
    emp_id = input("Enter employee ID: ").strip()

    if not emp_id:
        print("Employee ID cannot be empty.")
        return

    if emp_id in employees:
        print("Employee ID already exists.")
        return

    name = input("Enter employee name: ").strip()
    department = input("Enter department: ").strip()

    try:
        salary = float(input("Enter salary: "))
        if salary < 0:
            print("Salary cannot be negative.")
            return
    except ValueError:
        print("Enter a valid salary.")
        return

    if not name or not department:
        print("Name and department cannot be empty.")
        return

    employees[emp_id] = {
        "name": name,
        "department": department,
        "salary": salary
    }
    print("Employee added successfully!")


def update_employee():
    emp_id = input("Enter employee ID to update: ").strip()

    if emp_id not in employees:
        print("Employee not found.")
        return

    employee = employees[emp_id]

    name = input("New name (Enter to keep current): ").strip()
    department = input("New department (Enter to keep current): ").strip()
    salary_text = input("New salary (Enter to keep current): ").strip()

    if name:
        employee["name"] = name
    if department:
        employee["department"] = department

    if salary_text:
        try:
            salary = float(salary_text)
            if salary < 0:
                print("Salary cannot be negative.")
                return
            employee["salary"] = salary
        except ValueError:
            print("Invalid salary.")
            return

    print("Employee updated successfully!")


def delete_employee():
    emp_id = input("Enter employee ID to delete: ").strip()

    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")


def show_employee(emp_id, employee):
    print(f"\nID: {emp_id}")
    print(f"Name: {employee['name']}")
    print(f"Department: {employee['department']}")
    print(f"Salary: {employee['salary']:.2f}")


def search_employee():
    emp_id = input("Enter employee ID to search: ").strip()

    if emp_id in employees:
        show_employee(emp_id, employees[emp_id])
    else:
        print("Employee not found.")


def list_employees():
    if not employees:
        print("No employees available.")
        return

    for emp_id, employee in employees.items():
        show_employee(emp_id, employee)


def highest_salary():
    if not employees:
        print("No employees available.")
        return

    emp_id = max(employees, key=lambda key: employees[key]["salary"])
    show_employee(emp_id, employees[emp_id])


def average_salary():
    if not employees:
        print("No employees available.")
        return

    total = sum(emp["salary"] for emp in employees.values())
    print(f"Average salary: {total / len(employees):.2f}")


def department_filter():
    department = input("Enter department name: ").strip().casefold()
    found = False

    for emp_id, employee in employees.items():
        if employee["department"].casefold() == department:
            show_employee(emp_id, employee)
            found = True

    if not found:
        print("No employees found in this department.")


def main():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Search Employee")
        print("5. List All Employees")
        print("6. Highest Salary")
        print("7. Average Salary")
        print("8. Department Filter")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            update_employee()
        elif choice == "3":
            delete_employee()
        elif choice == "4":
            search_employee()
        elif choice == "5":
            list_employees()
        elif choice == "6":
            highest_salary()
        elif choice == "7":
            average_salary()
        elif choice == "8":
            department_filter()
        elif choice == "9":
            print("Application closed.")
            break
        else:
            print("Invalid choice. Enter 1-9.")


if __name__ == "__main__":
    main()