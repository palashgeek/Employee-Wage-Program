import random 
def emp_attendence():
    attendence = random.randint(0,1)
    if attendence == 1:
        print("Employee is present")
    else:
        print("Employee is not present")
def daily_employee_wage():
    full_time_wage_per_hr = 20
    full_day_hr = 8

    if emp_attendence == 1:
        daily_wage = full_time_wage_per_hr * full_day_hr
        return "the daily wage for an full time employee is: {}".format(daily_wage)
    else:
        return "the employee is not present"

if __name__ == "__main__":
    print(daily_employee_wage())

