task =[]
task1 = input("Enter your task1:")
task.append(task1)

task2 = input("Enter your task2:")
task.append(task2)

task3 = input("Enter your task3:")
task.append(task3)

task4 = input("Enter your task4:")
task.append(task4)

task5 = input("Enter your task5:")
task.append(task5)
print("YOUR TO-DO LIST:")
for i in range(len(task)):
    print(f"{i+1}. {task[i]}")

    