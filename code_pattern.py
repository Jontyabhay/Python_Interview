# Square pattern
def pattern():
    a = int(input("Enter a number: "))
    c = 0
    for i in range(a ** 2):
        print("*", end=' ')
        c = c + 1
        if c % a == 0:
            print(end='\n')
          


# Triangle pattern
def pattern1():
    a = int(input('Enter a number: '))
    for i in range(a):
        for j in range(i+1):
            print("*", end=' ')
        print(end='\n')


# Reverse traingle pattern
def pattern2():
    a = int(input("Enter a number: "))
    for i in range(a):
        for j in range(a-i):
            print("*", end=' ')
        print(end='\n')
       

# Right M pattern
def pattern3():
    a = int(input('Enter a number: '))
    for i in range(a):
        for j in range(a-i):
            print("*", end=' ')
        print(end='\n')
    for i in range(a-1):
        for j in range(i+2):
            print("*", end=' ')
        print(end='\n')

# M mirror image
def pattern4():
    a = int(input("Enter a number: "))
    for i in range(a):
        for j in range(i+1):
            print("*", end=' ')
        print(end='\n') 
    for i in range(a):
        for j in range(a-i-1):
            print("*", end=' ')
        print(end='\n')