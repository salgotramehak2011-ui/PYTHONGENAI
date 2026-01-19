#WAP month name
month = int(input("Enter the momth (1-12):"))
if month==1:
    print("January")
elif month==2:
    print("Feburary")
elif month==3:
    print("March")
elif month==4:
    print("April")
elif month==5:
    print("May")
elif month==6:
    print("June")
elif month==7:
    print("July")
elif month==8:
    print("August")
elif month==9:
    print("September")
elif month==10:
    print("October")
elif month==11:
    print("November")
elif month==12:
    print("December")
else:
    print("Invalid Month")

#question2
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
#BOTH NO. ARE EQUAL OR NOT
if num1 == num2:
    print("Both number are equal")
else:
    print("Both number are not equal")

# FIRST NUMBER IS SMALLER OR EQUAL TO SECOND NUMBER
if num1 <= num2:
    print("First number is smaller or equal to second number")
else:
    print("First number is not smaller or equal to second number")

#WHICH IS BIGGER IN BOTH
if num1 > num2:
    print("First number is bigger")
else:
    print("Second number is bigger")

#PRINT YOUR FIRST NAME FIVE TIMES-------
if num1 > num2:
    for i in range(5):
        print("First name")
elif num1 < num2:
    for i in range(3):
        print("Surname")

# Question3 
str1 = input("Enter first string")
str2 = input("Enter second string")
if str1 == str2:
    print("Both string are equal")
else
    print("Both string are not equal")

# Question4
str_1 = input("Enter first string")
str_2 = input("Enter second string")
num1 = int(str_1)
num2 = int(str_2)
if str_1 == str_2:
    print("Both are equal")
else:
    print("Both are not equal")

#QUESTION 5
num = int(input("Enter the number"))
sum = 0
for i in range(1,num):
    sum+=i
print("Sum of all number from 1 to given no.:",sum)

#Question 6
num = int(input("Enter the input number:"))
for i in range(0,29,2):
    print(i,end=",")
#QUESTIONS 7
op = input("Enter operator + or -")
num = int(input("Enter number"))
if op == "+":
    for i in range(0,num):
        print(i,end=",")
elif op == "-":
    for i in range(num,0,-1):
        print(i,end=",")
else:
    print("Invalid")


