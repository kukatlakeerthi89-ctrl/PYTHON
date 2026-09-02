a = 10
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

#simple calculator
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("addition:",a+b)
print("subraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)


#student marks calculator
a = int(input("enter english marks"))
b = int(input("enter maths marks"))
c = int(input("enter social marks"))
total = a+b+c
avg = total/3
print(total)
print(avg)

#shopping bill calculator
price1 = float(input("Enter product 1 price:"))
price2  = float(input("Enter product 2 price:"))
price3 = float(input("Enter product 3 price:"))
total = price1+price2+price3
discount = total*0.10
final_amount = total-discount
print(final_amount)

#salary calculator
basic  = float(input("Enter basic salary:"))
hra = basic*0.20
da = basic*0.10
gross_salary = basic+hra+da

print("Basic salary:",basic)
print("HRA:",hra)
print("DA:",da)
print("Gross salary:",gross_salary)




