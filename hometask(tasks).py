menu = """
1. Add task
2. Remove task
3. Tasks list 
4. Exit
"""

# Shuni ham while da list methods bilan Todo list basic
# Homework ‼️
tasks = []
while True:
    print(menu)
    x = int(input("Choose number: "))
    if int(x) == 1:
        theme = str(input("Theme of task: "))
        tasks.append(theme)
        task = str(input("Task: "))
        tasks.append(task)
        print("Successfully added")
    elif int(x) == 2:
        nametask = str(input("Task name: "))
        tasks.remove(nametask)
        print("Succesfully removed")
    elif int(x) == 3:
        print(f"""
              All tasks:
              {tasks}
              """)     
    elif int(x) == 4:
        print("Task is done, see you soon") 
        break      
