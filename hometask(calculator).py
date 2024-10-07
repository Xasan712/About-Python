menu = """
1. Add
2. Subtract
3. Multiply
4. Division 
5. Exit
"""
while True:
    x = input(menu)
    if int(x) == 1:
        a = int(input("A: "))
        b = int(input("B: "))
        print(a+b)
    elif int(x) == 2:
        a = int(input("A: "))
        b = int(input("B: "))
        print(a-b)
    elif int(x) == 3:
        a = int(input("A: "))
        b = int(input("B: "))
        print(a*b) 
    elif int(x) == 4:
        a = int(input("A: "))
        b = int(input("B: "))
        print(a//b) 
    elif int(x) == 5:
        print("Successfully stopped")  
        break
                  