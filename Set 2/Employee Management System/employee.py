
# create an employee class

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Position:", self.position)
        print("Salary:", self.salary)


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        print("Enter employee information:")
        name = input("Name: ")
        age = input("Age: ")
        position = input("Position: ")
        salary = input("Salary: ")
        employee = Employee(name, age, position, salary)
        self.employees.append(employee)
        print("Employee added successfully.")

    def remove_employee(self):
        name = input("Enter name of employee to remove: ")
        for employee in self.employees:
            if employee.name.lower() == name.lower():
                self.employees.remove(employee)
                print("Employee removed successfully.")
                return
        print("Employee not found.")

    def display_all_employees(self):
        if len(self.employees) == 0:
            print("No employees to display.")
        else:
            for employee in self.employees:
                employee.display_info()

    def display_menu(self):
        print("\nWelcome to the Employee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Display All Employees")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.remove_employee()
            elif choice == "3":
                self.display_all_employees()
            elif choice == "4":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    ems = EmployeeManagementSystem()
    ems.run()
