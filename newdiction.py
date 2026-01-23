# dic ={"order":[1,2,3,4],"product":["apples","banana","grapes","pears"]}
# print(dic)
# print(dic["order"])
# print(dic.keys())
# print(dic.get["order"][0])

# take empty dictionary and ask user to input to the number of time they want
# to enter and input from the user to make dic
# dic ={}
# x = input("Enter the input to the number: ")
# for i in range(x):
#     key = input("enter the key: ")
#     value = input("enter the value: ")
#     dic[key] = value
#     print("final dictionary")
# print(dic)

# GIVEN 
# employee_details ={
#     101: {"name":"Alice","department":"HR","salary":48000},
#     102:{"name":"Bob","department":"IT","salary":62000},
#     103:{"name":"Charlie","department":"Finance","salary":75000},
#     104:{"name":"Diana","department":"Marketing","salary":50000}
# }
# High_salary_employees = []
# for i in employee_details.values():
#     if i["salary"] > 50000:
#         High_salary_employees.append(i["name"])
# print(High_salary_employees)


#-------CREATING DICTIONARY--------
# std_dic = {
#     "name": "Mehak",
#     "class": "btech",
#     "roll_no. ":1234,
#     "course": "CSE"
# }
# print(std_dic)


#-------ACCESSSING VALUE--------
# print(std_dic["name"])
# print(std_dic["course"])


#------ADDING A NEW KEY-VALUE PAIR--------
# std_dic["marks"] = 21
# std_dic["age"] = 15
# print(std_dic)


#---------UPDATING A VALUE-----------
# std_dic["marks"] = 45
# print(std_dic)


#-------REMOVE A ITEM----------
# std_dic.pop("course")
# print(std_dic)


#--------LOOPING THROUGH A DICTIONARY--------
# for key,value in std_dic.items():
#     print(key,"--",value)


#------DICTIONARY FUNCTION----------
# std_dic.keys()    # all keys
# std_dic.values()  # all values
# std_dic.items()   # key-value pairs


# 
# std_dic = {
#     "name": "Mehak",
#     "class": "btech",
#     "roll_no. ":1234,
#     "course": "CSE"
# }
# print(std_dic["course"])

# std = {
#     "name": "Mehak",
#     "age": 14,
#     "marks": 60
# }
# print(std)

# data = {
#     "name": "Rahul",
#     "marks": 78
# }
# data["grade"] = "A"
# print(data)

# info = {
#     "name": "Mehak",
#     "city": "Delhi",
#     "course": "CSE"
# }
# print(info["city"])

# std = {
#     "name": "Mehak",
#     "marks": 75
# }
# std["marks"] = 90
# print(std)

# sub1 = {
#     "Science": 89,
#     "Math": 90,
#     "Hindi": 80
# }
# print(sub1.keys())

# sub2 = {
#     "Science": 89,
#     "Math": 90,
#     "Hindi": 80
# }
# print(sub2.values())

# dic = {
#     "name": "Komal"
# }
# dic.update({"course":"English","marks":70})
# print(dic)

data = {"a":10,"b":20,"c":30}
data.pop("b")
print(data)