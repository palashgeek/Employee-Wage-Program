import random 

FULL_TIME_WAGE_PER_HR = 20
FULL_DAY_HR = 8
PART_TIME_WAGE_HR = 4
MONTHLY_WORKING_DAYS = 20
MONTHLY_WORKING_HRS = 100

def emp_attendence():
    return random.randint(0,2)
    
    
def daily_employee_wage(attendance):

    if attendance == 0:
            return 0
        
    elif attendance ==1:
            return FULL_TIME_WAGE_PER_HR * FULL_DAY_HR 
        
    elif attendance == 2:
             return FULL_TIME_WAGE_PER_HR * PART_TIME_WAGE_HR 

def month_wage():
    montly_wage = 0
    total_hrs = 0
    total_days = 0

    while total_hrs < MONTHLY_WORKING_HRS and total_days < MONTHLY_WORKING_DAYS:
        attendance = emp_attendence()
        daily_wage = daily_employee_wage(attendance)
        montly_wage += daily_wage

        if attendance != 0:
             total_days +=1
             if attendance == 1:
                  total_hrs += FULL_DAY_HR
             elif attendance == 2:
                  total_hrs += PART_TIME_WAGE_HR
    
    return montly_wage
        


if __name__ == "__main__":
    print(month_wage())

