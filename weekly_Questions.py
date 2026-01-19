# # QUESTION 1
# for i in range(1,51):
#     if i%3 == 0 and i%5 ==0:
#         print("FizzBuzz")
#     elif i%3 == 0:
#         print("Fizz")
#     elif i%5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# # QUESTION 2
# for num in range(1,101):
#     prime = True
#     for i in range (2,num):
#         if num%i ==0:
#             prime = False
#             break
#     if prime:
#         print(num)

# # QUESTION 3
# score = int(input("Enter the input score(0-100): "))
# if 90 <= score <=100:
#     print("Grade A")
# elif 80 <= score <=89:
#     print("Grade B")
# elif 70 <= score <=79:
#     print("Grade C")
# elif 60 <= score <=69:
#     print("Grade D")
# elif 0 <= score < 60:
#     print("Grade F")
# else:
#     print("Invalid")

# # QUESTION 4
# num = int(input("Enter a number"))
# for i in range(1,11):
#     print(num, "X", i,"=",num*i)

# # QUESTION 5
# square = [i*i for i in range(1,21) if i%2 == 0]
# print(square)

# # QUESTION 6
# year = int(input("Enter a year: "))
# if (year%4 == 0 and year % 100 != 0) or (year%400 == 0):
#     print("Leap year",year)
# else:
#     print("Not Leap year",year)

# # QUESTION 7
# a = float(input("Enter side 1: "))
# b = float(input("Enter side 2: "))
# c = float(input("Enter side 3: "))
# if a+b>c and a+c>b and b+c>a:
#     if a == b == c:
#         print("Equilateral Triangle")
#     elif a == b or b == c or a == c:
#         print("Isoceles Triangle")
#     elif (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
#         print("Right angled triangle")
#     else:
#         print("Scalene triangle")
# else:
#     print("Invalid Triangle")

# # QUESTION 8
# num = int(input("Enter an integer:"))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# QUESTION 10
# BMI = float(input("Enter body mass in index: "))
# if BMI < 18.5:
#     print("Underweight")
# elif 18.5 <= BMI < 24.9:
#     print("Normal Weight")
# elif 25 <= BMI < 29.9:
#     print("Overweight")
# elif BMI >= 30:
#     print("Obesity")
# else:
#     print("Invalid")

# # QUESTION 11
# day = int(input("Enter a number(1-7):"))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thrusday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Invalid")

# QUESTION 12
# price = float(input("Enter the price: "))
# if price > 1000:
#     discount = 0.10 * price
# elif 500 <= price < 1000:
#     discount = 0.05 * price
# else:
#     discount = 0
# final_price = price - discount
# print("Price:",price)
# print("Discount:",discount)
# print("Final price:",final_price)

# # QUESTION 13
# n = int(input("Enter a number"))
# sum = 0
# for i in range (1,n+1):
#     sum = sum + 1
# print("First n natural number:",sum)

# # QUESTION 15
# number = input("Enter the vowel: ")
# vowels ="AEIOUaeiou"
# count =0
# for i in number:
#     if i in vowels:
#         count = count + 1
# print("Vowels: ",count)

# # QUESTION 16
# n = int(input("Enter a number"))
# for i in range(1, n+1):
#     print("*" * i) 


# # QUESTION 17
# num = int(input("Enter a number"))
# digit_sum = 0
# while num > 0:
#     digit_sum += num%10
#     num = num // 10
# print("Sum of the digits: ",digit_sum)

# QUESTION 19
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     if i % 2 == 0:
#         print(i)

#QUESTION 20
# lis = [10,15,20,25,35,25,45,52,32,70]
# if 25 in lis:
#     print("It's Exists")
# else:
#     ("It's Not Exists")
# print("Total lenght of list: ", len(lis))
# print("Total occurance of 25 in the list: ",lis.count(25))
# print("Traverse of each element: ")
# for i in lis:
#     print(i)
# print("Show all even element: ")
# for i in lis:
#     if i % 2 == 0:
#         print(i)

# QUESTION21 
# user = input("Enter input a string of min 10 words and max 19 words: ")
# if len(user) > 10 and len(user) <= 19:
#     print("Here is your input string")
# else:
#     print("Add more string character")
# print("Full String: ",user)
# print("Lenght of String: ",len(user))
# print("Second last word in the string: ",user[2])


# QUESTION 22
# print("Welcome to calci")
# print("1. Power")
# print("2. Sum")
# print("3. Sub")
# print("4. Multiple")
# choice = int(input("Enter your choice: "))
# num1 = int(input("Enter 1st Number: "))
# num2 = int(input("Enter 2nd Number: "))
# if choice == 1:
#     print("Power is:",num1 ** num2)
# elif choice == 2:
#     print("Sum is:",num1 + num2)
# elif choice == 3:
#     print("Sub is:",num1 - num2)
# elif choice == 4:
#     print("Multiple is:",num1 * num2)
# else:
#     print("Invalid Choice")

# QUESTION 23
# x = ["abc","xyz","aba","1221"]
# count = 0
# for i in x:
#     if len(i) >=2 and i[0] == i[3]:
#         count = count + 1
# print("Number of string: ",count)



