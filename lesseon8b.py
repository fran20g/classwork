while True :
    print("=====Main Menu====")
    print("1.Add")
    print("2.List")
    print("3.Edit")
    print("Enter your Selection : ",end="")

    choice = input()


    if choice =="1":
        print("Add New record")
    elif choice =="2":
        print("List Record")
    elif choice =="3":
        print("Edit Record")
    elif choice =="4":
        print("Exit from program")
        break
    else:
        print("Invalid Selection")
