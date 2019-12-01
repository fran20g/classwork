from os import system

def add(a,b):
    c=a+b
    print("Addition is {}".format(c))

def sub(a,b):
    c=a-b
    print("subtraction is {}".format(c))

def mult(a,b):
    c=a*b
    print("Multiplication is {}".format(c))

def div(a,b):
    c=a/b
    print("Division is {}".format(c))

system('cls')
while True:
    print("====Main Menu====")
    print("1.Addition")
    print("2.subcription")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    print("Enter Your Selection:",end="")
    choice = input()

    if choice =="1":
      x= int (input("Enter First Value: "))
      y= int (input("Enter Second Value: "))
      add(x,y)
    elif choice =="2":
      x= int (input("Enter First Value: "))
      y= int (input("Enter Second Value: "))
      add(x,y)
    elif choice =="3":
       x= int (input("Enter First Value: "))
       y= int (input("Enter Second Value: "))
       add(x,y)
    elif choice =="4":
      x= int (input("Enter First Value: "))
      y= int (input("Enter Second Value: "))
      add(x,y)
    elif choice =="5":
        print("Exit from program")
        break
    else:
        print("Invalid Sellection")

    input("Press Enter to continue...")
    system('cls')
    
    