import csv

class Employee:
    def __init__(self, name, employee_id, hourly_rate, job_title):
        self.name = name
        self.employee_id = employee_id
        self.hourly_rate = hourly_rate
        self.job_title = job_title
        self.hours_worked = {
            'Monday': 0,
            'Tuesday': 0,
            'Wednesday': 0,
            'Thursday': 0,
            'Friday': 0,
            'Saturday': 0,
            'Sunday': 0
        }
    #Adds new employee to employees list  
    def add_employee():
      name = input("Enter employee name: ")
      employee_id = input("Enter employee ID: ")
      hourly_rate = float(input("Enter hourly rate: "))
      job_title = input("Enter job title: ")
      return Employee(name, employee_id, hourly_rate, job_title)
    #Checks for matching employee id, then removes them from employees
    def remove_employee(employees, employee_id):
        employees[:] = [employee for employee in employees if employee.employee_id != employee_id]
    #Updates hours worked on specific days
    def update_hours(self):
        for day in self.hours_worked:
            hours = float(input(f"Enter hours worked on {day}: "))
            self.hours_worked[day] = hours
    #Displays employees information, inlcuding hours worked
    def display_info(self):
        print("Name:",self.name,"\nEmployee ID:",self.employee_id,"\nHourly Rate:",self.hourly_rate,"\nJob Title:",self.job_title)
        print("Hours Worked:")
        for day, hours in self.hours_worked.items():
            print(f"{day}: {hours} hours")
        print(f"Total Hours: {sum(self.hours_worked.values())} hours")

#Function which updates payroll.csv with new employees, removed employees, and updated hours.
def save_to_csv(employees):

    emply = ['Name', 'EmployeeId', 'Pay', 'Title', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Total']

    with open("payroll.csv", mode='a', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=emply)
        csvwriter.writeheader()

        for employee in employees:
            csvwriter.writerow({
                'Name': employee.name,
                'EmployeeId': employee.employee_id,
                'Pay': employee.hourly_rate,
                'Title': employee.job_title,
                'Monday': employee.hours_worked['Monday'],
                'Tuesday': employee.hours_worked['Tuesday'],
                'Wednesday': employee.hours_worked['Wednesday'],
                'Thursday': employee.hours_worked['Thursday'],
                'Friday': employee.hours_worked['Friday'],
                'Saturday': employee.hours_worked['Saturday'],
                'Sunday': employee.hours_worked['Sunday'],
                'Total': sum(employee.hours_worked.values())
            })

if __name__ == '__main__':
    #Listed dictionaries for employees
    employees = []
    #Looped menu system
    while True:
        print("1 - Administrator")
        print("2 - Employee")
        print("0 - Save and Quit")
        ask = input("What would you like to do? ")
        #Looped administrator menu
        if ask == '1':
            print("0 - Add Employee")
            print("1 - Remove Employee")
            admin_choice = input('What would you like to do? ')

            if admin_choice == '0':
                new_employee = Employee.add_employee()
                employees.append(new_employee)
                print(f"Employee {new_employee.name} added successfully.")
            elif admin_choice == '1':
                remove_id = input('Enter the ID of the employee you would like to remove: ')
                Employee.remove_employee(employees, remove_id)
        #Employee menu to add hours worked
        elif ask == '2':
            employee_id = input('Enter your Employee ID: ')
            found = False
            for emp in employees:
                if employee_id == emp.employee_id:
                    emp.update_hours()
                    emp.display_info()
                    found = True
                    break
            if not found:
                print('ID not found in the system')
        #Updates payroll.csv, then exits
        elif ask == '0':
            save_to_csv(employees)
            print('Data saved to payroll.csv. Exiting...')
            break

        else:
            print("Invalid choice. Please try again.")
