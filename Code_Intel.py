def calc():
    a = input("Enter a number ")
    c = 0
    for i in range(0, int(a) ** 2):
        print("*", end=" ")
        c = c + 1
        if (c % int(a) == 0):
            print(end="\n")
calc()