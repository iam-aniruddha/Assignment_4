# Employee Data Generator using Faker

## Problem Statement

Creating a Python script that generates fake employee data and stores it in a JSON file. create a dataset of employee details, including attributes such as employee ID, name, email, business unit, and salary, also need to develop a solution that can handle setting and getting employee attributes, converting employee objects to JSON format, and writing employee data to a JSON file.

```
Use the python Faker module to generate fake data for the following.
	a. Create an JSON File "Employee Personal Details" with following data. Generate around 50-100 records
		"EMP ID", "EMP NAME", "EMP EMAIL", "Businees Unit" "Salary"
Note: This is already done as a part of the last assignment.

User the above as input data and do the following.

1. Define a class for the Employee and load all the data as Objects of this class.

2. Define setter methods for every attribute of the class.
   a. Set the value passed to it as a parameter
   b. Use Faker module to set the value as default

3. Define getter methods for very attribute of the class.

4. Define a method in the class to convert the Employee object to a JSON and write it to a file.
The function should be able to do it for 
* one employee
* List of Employees 
* All(by default)
```

## Solution Approach

1. **Creating Employee Objects**:

   - We define an `Employee` class that represents an employee.
   - The class has attributes for employee ID, name, email, business unit, and salary.
   - We use the **Faker** library to generate default values for these attributes.
2. **Setter Methods**:

   - We provide setter methods (`set_emp_id`, `set_emp_name`, etc.) to allow explicit assignment of attribute values.
   - These methods enable customization of employee data beyond the default values.
3. **Getter Methods**:

   - Getter methods (`get_emp_id`, `get_emp_name`, etc.) retrieve the attribute values.
   - These methods allow accessing employee data.
4. **JSON Conversion and File Writing**:

   - The `to_json_and_write` method converts an `Employee` object (or a list of objects) to JSON format.
   - It writes the data to a specified JSON file.
   - The method can handle writing data for a single employee, a list of employees, or all employees (by default).
5. **Example Usage**:

   - The script demonstrates how to create employee objects, generate default values, and write their data to JSON files.
   - It includes writing a single employee, a list of employees, and all employees to separate JSON files.

## Dependencies

- Python 3.x
- [Faker](https://pypi.org/project/Faker/) library (for generating realistic data)

## Usage

1. Install the required dependencies:

   ```bash
   pip install faker
   ```
2. Run the script:

   ```bash
   python faker_data.py
   ```
3. Check the generated JSON files:

   - `single_employee.json`: Contains data for a single employee.
   - `multiple_employees.json`: Contains data for multiple employees.
   - `employee_personal_details.json` (default): Contains data for all employees.

## Note

- Ensure that the generated JSON files have employee data.
- Verify that the script can handle different scenarios (single employee, multiple employees, default filename).
- Assess the readability and maintainability of the code.

---
