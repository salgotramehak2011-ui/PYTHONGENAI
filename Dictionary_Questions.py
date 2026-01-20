# QUESTION 1
# sen = input("Enter sentence: ")
# words = sen.lower().split()
# freq_word = {}
# for i in words:
#     if i in freq_word:
#         freq_word[i] +=1
#     else:
#         freq_word[i] = 1
# print(freq_word)

# QUESTION 2
# dic = {
#     "Shiv":12,
#     "Roopali":14,
#     "Danshu": 15
#     }
# print(dic)

# QUESTION 3
# dic = {
#     "Shiv":12,
#     "Roopali":14,
#     "Danshu": 15
#     }
# marks = sum(dic.values())
# total_std = len(dic)
# avg = marks/total_std
# print("Average marks: ",avg)
# print("Students scoring marks:")
# for name,marks in dic.items():
#     if marks > avg:
#         print(name)

# QUESTION 4
# dic1 ={
#     "a":50,
#     "b":30,
#     "c":70
# }
# dic2 ={
#     "b":60,
#     "c":65,
#     "d":40
# }
# merge_dic = dic1.copy()
# for key,value in dic2.items():
#     if key not in merge_dic:
#         merge_dic[key] = value
# print(merge_dic)

# QUESTION 5
# dic ={
#     "name":"Alice",
#     "city":"banglore",
#     "course":"data science"
# }
# max_key = max(dic, key = lambda k: len(dic[k]))
# print(max_key)

# QUESTION 6
# dic = {
#     "a":5,
#     "b":15,
#     "c":45,
#     "d":60
# }
# low = 10
# high = 50
# filter_dic = {}
# for key,value in dic.items():
#     if low <= value <= high:
#         filter_dic[key] = value
# print(filter_dic)

# QUESTION 7
# votes = {}
# n = int(input("Enter number of voters: "))
# for i in range(n):
#     cand = input("Enter candidate name: ")
#     if cand in votes:
#         votes[cand] += 1
#     else:
#         votes[cand] = 1
# print("Vote count: ",votes)
# win = max(votes, key=votes.get)
# print("Winner is: ",win)

# QUESTION 8
# dic1 ={
#     "a":10,
#     "b":20,
#     "c":30
# }
# dic2 ={
#     "b":200,
#     "c":300,
#     "d":400
# }
# for key in dic1:
#     if key in dic2:
#         dic1[key] = dic2[key]
# print("Updated Dictionary: ",dic1)

# QUESTION 9
# data = {"a":10,"b":20,"c":30}
# update = {"b":200,"c":300}
# for key in data:
#     if key in update:
#         data[key] = update[key]
# print(data)