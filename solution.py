# faker_data.py
"""importing necessary libraries"""
# pylint: disable=line-too-long, too-many-arguments,redefined-outer-name

import json
import random
from faker import Faker
import decorator

# Initialize Faker object
fake = Faker()

class Employee:
    """
    Represents an employee with attributes such as ID, name, email, business unit, and salary.
    """

    def __init__(self, emp_id=None, emp_name=None, emp_email=None, business_unit=None, salary=None):
        """
        Initializes an Employee object.

        Args:
            emp_id (int): Employee ID.
            emp_name (str): Employee name.
            emp_email (str): Employee email.
            business_unit (str): Business unit (e.g., Sales, Marketing).
            salary (float): Employee salary.
        """
        self._emp_id = emp_id
        self._emp_name = emp_name
        self._emp_email = emp_email
        self._business_unit = business_unit
        self._salary = salary

    def set_emp_id(self, emp_id):
        """
        Sets the employee ID.

        Args:
            emp_id (int): Employee ID.
        """
        self._emp_id = emp_id

    def set_emp_name(self, emp_name):
        """
        Sets the employee name.

        Args:
            emp_name (str): Employee name.
        """
        self._emp_name = emp_name

    def set_emp_email(self, emp_email):
        """
        Sets the employee email.

        Args:
            emp_email (str): Employee email.
        """
        self._emp_email = emp_email

    def set_business_unit(self, business_unit):
        """
        Sets the business unit.

        Args:
            business_unit (str): Business unit (e.g., Sales, Marketing).
        """
        self._business_unit = business_unit

    def set_salary(self, salary):
        """
        Sets the employee salary.

        Args:
            salary (float): Employee salary.
        """
        self._salary = salary

    def get_emp_id(self):
        """
        Retrieves the employee ID.

        Returns:
            int: Employee ID.
        """
        return self._emp_id

    def get_emp_name(self):
        """
        Retrieves the employee name.

        Returns:
            str: Employee name.
        """
        return self._emp_name

    def get_emp_email(self):
        """
        Retrieves the employee email.

        Returns:
            str: Employee email.
        """
        return self._emp_email

    def get_business_unit(self):
        """
        Retrieves the business unit.

        Returns:
            str: Business unit.
        """
        return self._business_unit

    def get_salary(self):
        """
        Retrieves the employee salary.

        Returns:
            float: Employee salary.
        """
        return self._salary

    def generate_default_values(self):
        """
        Generates default values for attributes using the Faker library.
        """
        if not self._emp_id:
            self._emp_id = fake.random_int(min=1000, max=9999)
        if not self._emp_name:
            self._emp_name = fake.name()
        if not self._emp_email:
            self._emp_email = fake.email()
        if not self._business_unit:
            business_units = ["Sales", "Marketing", "Finance", "Human Resources", "IT", "Operations"]
            self._business_unit = random.choice(business_units)
        if not self._salary:
            self._salary = round(random.uniform(30000, 100000), 2)

    @staticmethod
    @decorator.log_decorator
    def to_json_and_write(employees, file_name="employee_personal_details.json"):
        """
        Converts Employee object(s) to JSON and writes to a file.

        Args:
            employees (Union[Employee, List[Employee]]): Employee object(s) or list of Employee objects.
            file_name (str): Name of the output JSON file.
        """
        if not isinstance(employees, list):
            employees = [employees]

        json_data = []
        for emp in employees:
            emp_dict = {
                "EMP ID": emp.get_emp_id(),
                "EMP NAME": emp.get_emp_name(),
                "EMP EMAIL": emp.get_emp_email(),
                "Business Unit": emp.get_business_unit(),
                "Salary": emp.get_salary()
            }
            json_data.append(emp_dict)

        with open(file_name, "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, indent=4)
        print(f"Employee data written to '{file_name}'")

# Example usage:
if __name__ == "__main__":
    fake = Faker()
    emp1 = Employee()
    emp1.generate_default_values()

    employees_list = [Employee() for _ in range(50)]  # Generate 50 records
    for emp in employees_list:
        emp.generate_default_values()

    emp1.to_json_and_write([emp1], "single_employee.json")
    Employee.to_json_and_write(employees_list[:5], "multiple_employees.json")
    Employee.to_json_and_write(employees_list) #default file name is "employee_personal_details.json"
