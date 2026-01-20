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
employee_details ={
    101: {"name":"Alice","department":"HR","salary":48000},
    102:{"name":"Bob","department":"IT","salary":62000},
    103:{"name":"Charlie","department":"Finance","salary":75000},
    104:{"name":"Diana","department":"Marketing","salary":50000}
}
High_salary_employees = []
for i in employee_details.values():
    if i["salary"] > 50000:
        High_salary_employees.append(i["name"])
print(High_salary_employees)

