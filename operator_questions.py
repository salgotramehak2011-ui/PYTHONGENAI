std_name= input("Enter name: ")
std_class= input("Enter class: ")
std_section= input("Enter section: ")

marks1=int(input("Enter marks of sub1: "))
marks2=int(input("Enter marks of sub2: "))
marks3=int(input("Enter marks of sub3: "))
marks4=int(input("Enter marks of sub4: "))
marks5=int(input("Enter marks of sub5: "))
total_marks= marks1 + marks2 + marks3 + marks4 + marks5
percentage= (total_marks / 500) * 100

print("Name",std_name)
print("Class",std_class)
print("Section",std_section)
print("Total Marks",total_marks)
print("Percentage",percentage)

#input 3 numbers and return sum of these
num1= int(input("Enter first numbers: "))
num2= int(input("Enter second numbers: "))
num3= int(input("Enter third numbers: "))
return_sum= num1 + num2 + num3
print("Total sum of these num: ",return_sum)

#input a number and find square of it
num= int(input("Enter numbers: "))
print(num**2)

#write a program
#take the temperature #convert into a float
temp_celsius = input("Enter temperature in celsius: ")
print(temp_celsius)
print(float(temp_celsius))

#celsius and fahrenheit
temp = input("Enter temperature in celsius: ")
celsius = float(temp)
fahrenheit = (celsius * 9/5)+32
print(celsius)
print(fahrenheit)

#WAP to calculat the reminder------
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
return1_result = num1 % num2
print("Remainder is: ",return1_result)
return2_result = num1 // num2
print("Quotient is: ",return2_result)

#WAP to calculate using the formula
P = float(input("Enter the principal: "))
R = float(input("Enter the rate: "))
T = float(input("Enter the time: "))
SI = (P*R*T)/100
print(SI)

 




