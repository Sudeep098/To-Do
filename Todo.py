import time
Tasks=[]
ok=1



def Add():
    SNO=len(Tasks)
    Title=input("Enter Title: ")
    Description=input("Description: ")
    Deadline=input("Deadline/Time: ")
    Status="Uncompleted"
    Task=[SNO, Title, Description, Deadline, Status]
    Tasks.append(Task)
    line("*")
    print("Task Added")
    line("*")

def View():
    line("=")
    print("S.No.    Title    Description    Deadline    Status")
    for i in Tasks:
        line("-")
        for j in i:
            print(j, end="      ")
        line("-")
        # print("\n")
def Remove():
    a=int(input("Enter Task number to delete: "))
    Tasks.remove(Tasks[a])
    line("~")
    print("Task Removed")
    line("~")
def Mark():
    b=int(input("Enter Task number to mark completed: "))
    Tasks[b][4]="Completed"
    line("*")
    print("Marked Successfully")
    line("*")

def line(sign, k=60):
    print("\n")
    for i in range(k):
        print(sign, end="")
    print("\n")
def center():
    for k in range(50):
        print(" ", end="")

def load():
    word="LOADING...!!"
    for i in word:
        print(i, end=" ")
        time.sleep(0.3)










load()
line("\"", 100)
center()
print("To-Do Maker")
line("\"", 100)
while ok!=0:
    print("(1)Add Task")
    print("(2)View Tasks")
    print("(3)Remove Task")
    print("(4)Mark As Completed")
    print("(5)Quit")
    choice=int(input("**Enter Action: "))
    print("\n")
    if choice==1:
        Add()
    elif choice==2:
        View()
    elif choice==3:
        Remove()
    elif choice==4:
        Mark()
    elif choice==5:
        break

print("\n-----Exit Successful-----\n")

