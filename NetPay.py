import EmployeeClass as ec
import PayrollDeductionClass as pay

def main():
    employee = create_employee()
    pays = enter_pay()
    display_emp(employee, pays)

def create_employee():
    emp_name = 'Jimmy Smith'
    emp_id = 58475
    emp_department = 'Information Systems'
    emp_title = 'Developer'
    emp_pay = 6800

    employee = ec.Employee(emp_name, emp_id, emp_department, emp_title, emp_pay)
    return employee

def enter_pay():
    pay1 = pay.Payroll_deduction('food court', '8/14/2022', 22.5, 39119)
    pay2 = pay.Payroll_deduction('gift contribution', '8/12/2022', 25, 58475)
    pay3 = pay.Payroll_deduction('food court', '8/17/2022', 15.25, 21547)
    pay4 = pay.Payroll_deduction('vending machine', '8/22/2022', 3, 58475)
    pay5 = pay.Payroll_deduction('vending machine', '8/5/2022', 2.75, 58475)
    pays = [pay1, pay2, pay3, pay4, pay5]

    return pays

def display_emp(employee, pays):


    if ec.Employee.get_iden == pay.Payroll_deduction.get_emp_iden:
        minus = sum(pay.charge_amount)

    print('\n*** Employee Pay ***')
    print('Name: ', ec.Employee.get_name(employee))
    print('ID: ', ec.Employee.get_iden(employee))
    print('Department: ', ec.Employee.get_department(employee))
    print('Gross Pay: ', ec.Employee.get_monthly_salary(employee))
    print('Net Pay: ', (ec.Employee.get_monthly_salary(employee) - minus))



main()

