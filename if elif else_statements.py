#problem 1
a = 20
b = 30
if a>=15:
    print("a is greater than b")
elif a>=20:
    print("a is equal to b")
else:
    print("a is less than b")

#problem 2
#we can use elif statement as many times as we want
#using 'and' operator
marks = int(input("enter marks"))
if marks>=90:
    print("grade A")
elif marks<=89 and marks>=60:
    print("grade B")
elif marks<=59 and marks<=35:
    print("grade C")
else:
    print("grade D")

#problem 3 
marks = int(input("enter marks"))
if marks >= 90:
    print("grade A")
elif marks >= 75:
    print("grade B")
elif marks >= 60:
    print("grade C")
elif marks >= 40:
    print("grade D")
else:
    print("Fail")

#problem 4
#largest of two numbers
a = int(input("enter first number:"))
b = int(input("enter second number:"))
if a > b:
    print("a is largest")
elif b > a:
    print("b is largest")
else:
    print("both are equal")

#problem 5
#largest of three numbers
a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))
if a >= b and a >= c:
    print("largest:",a)
elif b >= a and b >= c:
    print("largest:",b)
else:
    print("largest:",c)

#problem 6
number = int(input("enter a number"))
if number>0:
    print("positive")
elif number<0:
    print("negative")
else:
    print("zero")

#problem 7
day = int(input("enter day number"))
if day == 1:
    print("monday")
elif day == 2:
    print("tuesday")
elif day == 3:
    print("wednesday")
elif day == 4:
    print("thursday")
elif day == 5:
    print("friday")
elif day == 6:
    print("saturday")
else:
    print("sunday")

#
    
          
