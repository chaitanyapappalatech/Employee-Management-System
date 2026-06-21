import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chaitanya@800",
    database="employee_db"
)

cursor = conn.cursor()

print("Database Connected Successfully")

def add_employee():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    email = input("Enter Email: ")

    query = """
    INSERT INTO employees
    VALUES(%s,%s,%s,%s,%s)
    """

    values = (id, name, dept, salary, email)

    cursor.execute(query, values)
    conn.commit()
    print("Employee Added Successfully")


def view_employee():

    cursor.execute("SELECT * FROM employees")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

def search_employee():

    emp_id = int(input("Enter Employee ID: "))

    cursor.execute(
        "SELECT * FROM employees WHERE id=%s",
        (emp_id,)
    )

    result = cursor.fetchone()

    if result:
        print(result)
    else:
        print("Employee Not Found")

def update_employee():

    emp_id = int(input("Enter Employee ID: "))

    salary = float(input("Enter New Salary: "))

    cursor.execute(
        "UPDATE employees SET salary=%s WHERE id=%s",
        (salary, emp_id)
    )

    conn.commit()

    print("Employee Updated")

def delete_employee():

    emp_id = int(input("Enter Employee ID: "))

    cursor.execute(
        "DELETE FROM employees WHERE id=%s",
        (emp_id,)
    )

    conn.commit()

    print("Employee Deleted")

add_employee()
view_employee()
search_employee()
update_employee()
delete_employee()

while True:

    print("\n===== Employee Management System =====")

    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        view_employee()

    elif choice == 3:
        search_employee()

    elif choice == 4:
        update_employee()

    elif choice == 5:
        delete_employee()

    elif choice == 6:
        break

    else:
        print("Invalid Choice")