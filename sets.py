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



n = int(input("Enter a number: "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)

