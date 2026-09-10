#comparision_operators.py
a = 20
b = 30

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#age eligibility checker
age = int(input("Enter your age:"))
print("Eligible:",age >=18)

#pass or fail checker
marks = int(input("Enter marks:"))
print("passed:",marks >= 40)

#login validation
correct_username = "admin"
correct_password = "1234"

username = input("Enter username:")
password = input("Enter password:")

print(username == correct_username)
print(password == correct_password)

#logical operators
age = 25
citizen = True
print(age >= 18 and citizen == True)
print(age >= 16 and citizen == True)
age = 16
citizen = False


has_card = False
has_cash = True
print(has_card or has_cash)
is_logged_in = True

print(not is_logged_in)

#atm eligibility checker
balance = 10000
withdraw = 5000

print(withdraw > 0 and withdraw <= balance)

#student scholarship eligibity checker
marks = float(input("Enter marks:"))
attendance = float(input("Enter attendance:"))

eligible = marks >= 85 and attendance >= 75
print("Scholarship eligible:",eligible)

#electric city bill calculator
units = int(input("Enter electicity units:"))
rate = 6
bill = units * rate
print("Electricity Bill:", bill)

#travel expense calculator
travel = float(input("Travel expense:"))
food = float(input("Food expense:"))
hotel = float(input("Hotel expenses:"))

total = travel+food+hotel
print("Total Expense:", total)