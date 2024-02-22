import random 

FULL_TIME_WAGE_PER_HR = 20
FULL_DAY_HR = 8

def emp_attendence():
    attendence = random.randint(0,1)
    if attendence == 1:
        return 1
    else:
        return 0
    
def daily_employee_wage():

    if emp_attendence() == 1:
        daily_wage = FULL_TIME_WAGE_PER_HR * FULL_DAY_HR
        return "Employee is present for full time and the daily wage of the employee is {}".format(daily_wage)
    else:
        return "The Employee is Absent and the daily wage is 0."
    


if __name__ == "__main__":
    print(daily_employee_wage())

