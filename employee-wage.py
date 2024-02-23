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
            return 0
        
        case 1:
            daily_wage = FULL_TIME_WAGE_PER_HR * FULL_DAY_HR
            return daily_wage
        
        case 2:
             daily_wage = FULL_TIME_WAGE_PER_HR * PART_TIME_WAGE_HR 
             return daily_wage

def month_wage():
    montly_wage = 0
    for i in range(20):
       montly_wage += daily_employee_wage()
    return montly_wage
        
        

if __name__ == "__main__":
    print(month_wage())

