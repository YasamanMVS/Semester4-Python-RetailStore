from database import connect_db

def add_employee(name, type, years_worked, discount_number):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('''INSERT INTO Employees (name, type, years_worked, discount_number)
                      VALUES (?, ?, ?, ?)''', (name, type, years_worked, discount_number))
    conn.commit()
    conn.close()
    print(f"Employee {name} added successfully.")

def is_unique_discount_number(discount_number):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''SELECT discount_number FROM Employees WHERE discount_number = ?''', (discount_number,))
    return cur.fetchone() is None
def create_employee():
    while True:
        employee_name = input("Enter Employee Name: ")
        while employee_name == "":
            print("Employee Name cannot be empty. Please Enter again.")
            employee_name = input("Enter Employee Name: ")

        employee_type = input("Enter Employee Type (Manager/Hourly): ")
        while employee_type not in ["Manager", "Hourly"]:
            print("Employee Type must be either Manager or Hourly. Please Enter again.")
            employee_type = input("Enter Employee Type (Manager/Hourly): ")

        years_worked = input("Enter Years Worked: ")
        while not years_worked.isdigit():
            print("Years Worked must be a number. Please Enter again.")
            years_worked = input("Enter Years Worked: ")

        discount_number = input("Enter Employee Discount Number: ")
        while not discount_number.isdigit() or not is_unique_discount_number(discount_number):
            print("Discount Number must be unique and a number. Please Enter again.")
            discount_number = input("Enter Employee Discount Number: ")

        # Adding the new employee to the employee list
        add_employee(employee_name, employee_type, int(years_worked), int(discount_number))

        # If user wants to add another employee
        another = input("Would you like to add another employee? (YES/NO):  ").lower()
        if another != "yes":
            break


def display_employees():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Employees''')
    employees = cur.fetchall()
    print("Employee ID  | Employee Name       | Employee Type | Years Worked | Total Purchased | Total Discount | Employee Discount Number")
    for employee in employees:
        print(f"{employee[0]}  | {employee[1]}   | {employee[2]}   | {employee[3]}   | ${employee[4]:.2f}   | ${employee[5]:.2f}   | {employee[6]}")
    conn.close()