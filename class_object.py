std_details = []
#print("hello class")
def __init__(self):
    #print("hello this is constructor")
    #print(self)
    # self.name = n
    # self.rollno = r
    #print(f"name is {self.name} and rollno is {self.rollno})
    pass
def getMehak(self):
    self.name = input("enter name: ")
    self.rollno = input("enter roll no: ")
def printValues(self):
    #print(f"name is {self.name} and rollno is {self.rollno})
    std_details.append({self.name:self.rollno})

stu1 = Student()
stu2 = Student()
stu1.getMehak()
stu2.getMehak()

stu2.printValues()
#stu1.printVlue()

print(std_details)
# stu1 = Student("Mehak",12)
# stu1 = Student("Aru",13)
# print(std1)
