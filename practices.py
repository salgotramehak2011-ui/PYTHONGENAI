# fruits = ['apple','banana','orange']
# print(fruits)

# fruits.append('grapes') # append means jo last mei add hota hai
# print(fruits)

# fruits.insert(1,'grapes')
# print(fruits)

# for fruit in fruits:
#     print(fruit)

# data = ["Rahul", 20, 5.9, True]
# print(data)

# num = int(input("Enter a number: "))
# fact =1
# for i in range(1,num+1):
#     fact = fact * i
#     print(fact)

# a = int(input("Enter a number 1: "))
# b = int(input("Enter a number 2: "))
# print(a+b) # addition
# print(a-b) # subtraction
# print(a*b) # Multiple
# print(a/b) # divide
# print(a%b) # Modulus (remainder)
# print(a//b) # Floor division (quotient)
# print(a**b) # power

# n = int(input("Enter a table number: "))
# for i in range(1,11):
#     print(n,"x",i,"=",n*i)

# n = int(input("Enter a number: "))
# if n%2 == 0:
#     print('Even')
# else:
#     print('Odd')

# num = int(input("Enter a number: "))
# for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
# else:
#     print("Prime Number")

# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
#     print(fact)

#check whether a number is a palindrome;output:1221
# palin = input("Enter the palindrome: ")
# if palin == palin[::-1]:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")

# n = int(input("Enter number of terms: "))
# a = 0
# b = 1
# for i in range(n):
#     print(a)
#     c = a + b
#     a = b
#     b = c


# data = [12, 20, 5, 9, 10]
# data.sort()
# print(data)


# data = [12, 20, 5, 9, 10]
# data.sort(reverse=True)
# print(data)



#Create a list and add 59 on 3 location after that append 5 and print list and lenght of list
# list1 = [12,13,14,32,21,15,18]
# list1.insert(3,59)
# list1.append(5)
# len = len(list1)
# print("List",list1)
# print("Length of list",len)

# Find the common numbers in two lists
# list_a = [1,2,3,4]
# list_b = [2,3,4,5]

# com = [i for i in list_a for j in list_b  if i == j]
# print('Common number', com)

# Second largest number
# num = [12,25,23,34,50]
# num.sort()
# sec_larg = num[-2]
# print('Largest',sec_larg)

# a = int(input('Enter a number 1: '))
# b = int(input('Enter a number 2: '))
# c = int(input('Enter a number 3: '))

# largest = a

# if b > largest:
#     largest = b

# if c > largest:
#     largest = c

# print("Largest number is:", largest)

# WAP to remove duplicates from a list
# num = [10, 20, 30, 20, 40, 10, 50]
# num = list(set(num))  #set() automatically removes duplicate values. #Then we convert it back to a list using list().
# num.sort()
# print("List after removing duplicates:", num)