def pattern():
    a = input("Enter a number ")
    for i in range(int(a)):
        for j in range(i+1):
            print("*", end =" ")
        print(end='\n')

pattern()            