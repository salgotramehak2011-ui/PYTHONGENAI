# set1 = {23,45,True,"hi","surbhi",45,89,100}
# print("Set1 values: ",set1)

# set1.add(33)
# print("Add values: ",set1)

# set1.update({33,99,88})
# set1.update([33,99,88])
# print("Updated values: ",set1)

# set1.pop()
# print("Pop values: ",set1)

# set1.remove(100)
# print("Removed values: ",set1)

# set1.discard(122)
# print("Discarded values: ",set1)

# s = frozenset(["a","b","c","d"])
# print("Frozenset: ",s)
# s.add("e")
# print(s)

# marketing_user= {"Photoshop","Slack","Zoom","Canva","Trello"}
# sales_user= {"Salesforce","Slack","Zoom","Linkdin","HubSpot"}
# both_dep = marketing_user.union(sales_user)
# print("Both Department: ",both_dep)
# unq_dep = marketing_user.intersection(sales_user)
# print("All Unique Department: ",unq_dep)
# exe_dep = marketing_user.difference(sales_user)
# print("Exclusive Department: ",exe_dep)
# eir_dep = marketing_user.symmetric_difference(sales_user)
# print("Either  Department: ",exe_dep)



# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)
# setA = {1,2,3,4,5}
# setG = {1,2}
# is_subset = setG.issubset(setA)
# print(is_subset)# true or false
# is_superset = setA.issuperset(setG)
# print(is_superset)
# setH = {9,3}
# is_disjoint = setA.isdisjoint(setH)
# print(is_disjoint)





#=============================================================
#=============================================================
# def sumRet(*a):
#     print(a)
#     sum = 0
#     for i in a:
#         sum = sum + i
#     return sum
# print(sumRet(45,56,48))
# print((sumRet99,100,89,90))
# print(sumRet(45,56))


# def sumRet (**a):
#     print(a)
#     sum = 0
#     for i in a.values():
#         sum = sum + i
#     return sum
# print(sumRet(a = 45,b = 56,c= 48))
# print(sumRet(a = 99,b = 100,c = 89,d = 90))
# print(sumRet(a = 45,b = 56))