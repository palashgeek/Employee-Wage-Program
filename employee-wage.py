import random 

FULL_TIME_WAGE_PER_HR = 20
FULL_DAY_HR = 8
PART_TIME_WAGE_HR = 4

def emp_attendence():
    attendence = random.randint(0,2)
    if attendence == 1:
        return 1
    elif attendence ==2:
        return 2
    else:
        return 0
    
def daily_employee_wage():

    if emp_attendence() == 1:
        daily_wage = FULL_TIME_WAGE_PER_HR * FULL_DAY_HR
        return "Employee is present for full time and the daily wage of the employee is {}".format(daily_wage)
    elif emp_attendence() == 2:
        daily_wage = FULL_TIME_WAGE_PER_HR * PART_TIME_WAGE_HR 
        return "Employee is present only for part time and the daily wage of employee is {}".format(daily_wage)
    else:
        return "The Employee is Absent and the daily wage is 0."
    


if __name__ == "__main__":
    print(daily_employee_wage())

