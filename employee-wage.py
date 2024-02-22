import random 
def emp_attendence():
    attendence = random.randint(0,1)
    if attendence == 1:
        print("Employee is present")
    else:
        print("Employee is not present")

if __name__ == "__main__":
    emp_attendence()

