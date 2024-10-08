import pprint
s= """
School management system
1.Login
2.Register
->
"""

users = {
    "students": {
        "1": {
            "fullname": "jack",
            "username": "jacks",
            "password": 1111,
            "grade": 4,
            "lesson": "Python,Math,English",
            "class": "10b23",
            "homeTask": "Decorators"
        },
        "2": {
            "fullname": "Xasan",
            "username": "xxa571",
            "password": 2222,
            "grade": 5,
            "lesson": "Python,Math,English",
            "class": "10b23",
            "homeTask": "Decorators"
        },

    }
}

d = """
1. my profile
2. my lesson
3. my class
4. homeTask
"""

# data types for while

while 1:
    print(s)
    e = str(input("Num: "))
    if e == "1":
        ids = input("id: ")

        if ids in users["students"].keys():
            username = input("username: ")
            password = input("password: ")
            if username == users["students"][ids]['username'] and password == str(users["students"][ids]["password"]):
                print(d)
                option = input("Menudan tanlang(1-4): ")
                if option == "1":

                    print(users["students"][ids])
                elif option == "2":

                    x = users["students"][ids]['lesson']
                    print(f"Your lessons: {x}")
                elif option == "3":
                    x3 = users["students"][ids]['class']
                    print(f"Your class: {x3}")
                elif option == "4":
                    x4 = users["students"][ids]['homeTask']
                    print(f"Your home task: {x4}")
                else:
                    print("Invalid option selected.")
    if e == "2":
        newId = str(len(users["students"]) + 1)
        fullname = input("Enter fullname: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        grade = input("Enter grade: ")
        lesson = input("Enter lessons (comma-separated): ")
        student_class = input("Enter class: ")
        home_task = input("Enter home task: ")
        newstudent = {
            "fullname": fullname,
            "username": username,
            "password": password,
            "grade": int(grade),
            "lesson": lesson,
            "class": student_class,
            "homeTask": home_task
        }
        users["students"][newId] = newstudent
        print(f"Student successfully add: {newId}")




