for i in range(1,11):
    if i == 5:
        continue;
    print(i)

#print odd numbers from 1 to 10
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)

#print numbers until user enter 0
while True:
    number = int(input("enter number:"))
    if number == 0:
        break
    print("you entered:",number)

# print numbers from 1 to 100, but skip multiples of 3 and stop at 50
for i in range(1,101):
    if i == 50:
        break
    if i % 3 == 0:
        continue
    print(i)

#calculate the sum of positive numbers entered by the user
total = 0
while True:
    number = int(input("enter number"))
    if number < 0:
        continue
    if number == 0:
        break
    total = total+number
print("Total:",total)


#find the first number between 1 and 100 that is divisible 
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("first number:",i)
        break
    total = total+number
print("Total:",total)

#calculate the 
total = 0 
for i in range(10):
    number = int(input("enter number:"))
    if number <0:
        continue
total =total+number 
print("total")


#password check with limited attempts
correct_password = "python123"
for attempt in range(1,4):
    password = input("enter password")
    if password == correct_password:
        print("login successful")
        break
    print("wrong password")
else:
    print("Account holder")

#find the largest number among 5 numbers entered by the user
largest = None
for i in range(5):
    number = int(input("enter number"))
    if largest is None or number > largest:
        largest = number
print("Largest:",largest)

#find the smallest number among 5 numbers entered by the user
smallest = None
for i in range(5):
    number = int(input("enter number"))
    if smallest is None or number < smallest:
        smallest = number
print("Smallest:",smallest)










    

