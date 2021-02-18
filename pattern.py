def pattern():
    a = input("Enter a number ")
    for i in range(int(a)):
        for j in range(i+1):
            print("*", end =" ")
        print(end='\n')   

def another_pattern():
    a = 0
    inp = input("Enter a number ")
    for i in range(int(inp) ** 2):
        print("*", end=" ")
        a = a + 1
        if (a % int(inp) == 0):
            print(end='\n')

another_pattern()
pattern()            