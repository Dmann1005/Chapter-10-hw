class Employee:
    def __init__(self, name, iden, department, job_title, monthly_salary):
        self.__name = name
        self.__iden = iden
        self.__department = department
        self.__job_title = job_title
        self.__monthly_salary = monthly_salary

    def get_name(self):
        return self.__name
    def get_iden(self):
        return self.__iden
    def get_department(self):
        return self.__department
    def get_job_title(self):
        return self.__job_title
    def get_monthly_salary(self):
        return self.__monthly_salary



