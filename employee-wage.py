import random 

FULL_TIME_WAGE_PER_HR = 20
FULL_DAY_HR = 8
PART_TIME_WAGE_HR = 4

def emp_attendence():
    attendence = random.randint(0,2)
    match attendence:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
    
def daily_employee_wage():

    match emp_attendence():
        case 0:
            return "The Employee is Absent and the daily wage is 0."
        
        case 1:
            daily_wage = FULL_TIME_WAGE_PER_HR * FULL_DAY_HR
            return "Employee is present for full time and the daily wage of the employee is {}".format(daily_wage)
        
        case 2:
             daily_wage = FULL_TIME_WAGE_PER_HR * PART_TIME_WAGE_HR 
             return "Employee is present only for part time and the daily wage of employee is {}".format(daily_wage)

def month_wage():
    if emp_attendence() == 1:
        n = int(input("how many days Employee is present:"))
        monthly = FULL_TIME_WAGE_PER_HR * FULL_DAY_HR * n
        return monthly

    elif emp_attendence() == 2:
        m = int(input("how many days part time Employee is present:")) 
        monthly_part_time = FULL_TIME_WAGE_PER_HR * PART_TIME_WAGE_HR  * m
        return monthly_part_time

    else:
        return 0
    

if __name__ == "__main__":
    print(month_wage())

