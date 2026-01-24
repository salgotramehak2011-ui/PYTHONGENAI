# QUESTION 1
# sen = "python is easy and python is very easy"
# words = sen.split()
# freq_word = {}
# for i in words:
#     freq_word[i] = words.count(i)
# print(freq_word)

# QUESTION 2
# marks = {
#     "Shiv":12,
#     "Roopali":14,
#     "Danshu": 15
#     }
# total = sum(marks.values())
# avg = total/len(marks)
# print("Average marks: ",avg)
# print("Students scoring marks:")
# for i in marks:
#     if marks[i] > avg:
#         print(i)

# QUESTION 3
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
# for i in dic2:
#     if i in merge_dic:
#         if dic2[i] > merge_dic[i]:
#             merge_dic[i] = dic2[i]
#     else:
#         merge_dic[i] = dic2[i]
# print(merge_dic)

# QUESTION 4
# dic ={
#     "name":"Alice",
#     "city":"banglore",
#     "course":"data science"
# }
# max_key = ""
# for i in dic:
#     if len(dic[i]) > len(max_key):
#         max_key = i
# print(max_key)

# QUESTION 5
# dic = {
#     "a":5,
#     "b":15,
#     "c":45,
#     "d":60
# }
# filter_dic = {}
# for i in dic:
#     if 10 <= dic[i] <= 50:
#         filter_dic[i] = dic[i]
# print(filter_dic)

# QUESTION 6
# vote_list =["Tony","Sony","Tony"]
# votes = {}
# for i in vote_list:
#     votes[i] = vote_list.count(i)  
# print("Vote count: ",votes)
# win = max(votes, key=votes.get)
# print("Winner is: ",win)


# QUESTION 7
# data = {"a":10,"b":20,"c":30}
# update = {"b":200,"c":300}
# for i in data:
#     if i in update:
#         data[i] = update[i]
# print(data)