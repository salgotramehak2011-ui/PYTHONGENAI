def avg_marks(*a):
    print(a)
    sum = 0
    for i in a:
        sum = sum + i
        return sum
    print(avg_marks(45,56,48))
    print(avg_marks(99,100,89,90))
    print(avg_marks(45,56))