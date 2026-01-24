# QUESTION 1
# friday = {"Alice","Bob","Charlie"}
# saturday = {"Charlie","David","Eve"}
# all_guest = friday.union(saturday)
# print("Everyone attending atleast one night: ",all_guest)
# one_guest = friday.intersection(saturday)
# print("The Guest who is attending both night: ",one_guest)

# QUESTION 2
# data = {1,2,2,3,4,4,4,5}
# data.add(6)
# print("list cleaner: ",data)

# data = {1,2,2,3,4,4,4,5}
# remove_dupli = set(data)
# remove_dupli.add(6)
# print("list cleaner: ",remove_dupli)

# QUESTION 3
# library_books = {"Hobbit","1984","Gastsby","Odyssey","Hamlet"}
# checked_out = {"1984","Hamlet"}
# available = library_books.difference(checked_out)
# print("The Books currently available: ",available)
# donate_book = "Don Quixote"
# library_books.add(donate_book)
# print("The Updated new book",library_books)

# QUESTION 4
# user_permission = {"read","write"}
# admin_reqs =  {"read","write","execute"}
# is_subset = user_permission.issubset(admin_reqs)
# print("Check all permission required for admin access: ",is_subset)
# missing = admin_reqs.difference(user_permission)
# print("specific permission the user is missing: ",missing)

# QUESTION 5
# logs = {
#     "404":[10,12,15,20],
#     "500":[12,20,22,25],
#     "403":[10,20,30]
# }
# eve_typ = set(logs["404"]).intersection(logs["500"],logs["403"])
# print("Experienced every type of error:",eve_typ)

# neve = set(logs["500"]).difference(logs["404"])
# print("Never experienced a 404 error: ",neve)
