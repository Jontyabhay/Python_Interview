def calc():
    a = input("Enter a number ")
    c = 0
    for i in range(0, int(a) ** 2):
        print("*", end=" ")
        c = c + 1
        if (c % int(a) == 0):
            print(end="\n")

def pattern():
    inp = input("Enter a number ")
    for i in range(int(inp)):
        for j in range(i+1):
            print("*", end=' ')
        print(end='\n')
calc()
pattern()            