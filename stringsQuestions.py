# strings made of the first two and last two substrings
str1 = input("Enter the input string1: ")
str2 = input("Enter the input string2: ") 
if len(str1) < 2:
    print("not a valid string")
else: 
    first =str1[: 2]
    last = str2[-2:]
    both_str = first + last
    print("Result: ",both_str)


#sepated by a space and swap first character 
str3 = input("Enter the input string1: ") 
str4 = input("Enter the input string2: ") 
first =str3[10:0:-1]
last = str4[10:0:-1]
both_str = first +" "+ last
print("Result: ",both_str)


# WAP to add "ing" at the end given strings if the given strings already ends with
# "ing" then add "ly" . less than 3 string unchanged
str5 = input("Enter the input string: ")
if len(str5)<3:
    result = str5
elif str5.endswith("ing"):
    result = str5 + "ly"
else:
    result = str5 + "ing"
print("Result",result)
 

# WAP to remove the nth index character from a nonempty string
str6 = input("Enter the input string: ")
nth = int(input("Enter the nth index: "))
new_str = str6[: nth] + str6[nth+1 :]
print("Result: ",new_str)

 


