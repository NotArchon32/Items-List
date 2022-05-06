the_almighty_list = []

def menu():
    print("Add An Item : 1\nRemove An Item : 2\nUpdate An Item : 3\nCurrent List : 4\nStop The Program : 5")
    choice = input("Please Enter your Choice:")

    if choice == "1":
        addItem()
        menu()

    elif choice == "2":
        removeItem()
        menu()

    elif choice == "3":
        updateItem()
        menu()

    elif choice == "4":
        showList()
        menu()

    elif choice == "5":
        print("Goodbye!")

    else:
        print("Invalid Choice...")
        menu()

def addItem():
    item_to_add = input("Enter The Name Of The Item You Want To Add:")
    if the_almighty_list.__contains__(item_to_add):
        print("Item Already Existing!")
        same_item_choice = input("Do You Still Want To Add The Same Item?")

        if same_item_choice == "yes":
            the_almighty_list.append(item_to_add)

        else:
            menu()

    else:
        the_almighty_list.append(item_to_add)

def removeItem():
    item_to_delete = input("Enter The Name Of The Item You Want To Remove:")

    if the_almighty_list.__contains__(item_to_delete):
        the_almighty_list.remove(item_to_delete)

    else:
        print("Item Is Not Available In Your List")

def updateItem():
    item_to_update = input("Enter The Name Of The Item You Want To Update:")

    if the_almighty_list.__contains__(item_to_update):
        new_item_name = input("Enter The New Name:")
        the_almighty_list[the_almighty_list.index(item_to_update)] = new_item_name

    else:
        print("There Is No Item Named", item_to_update, "In Your List")

def showList():
    print("|==========Current List==========|")
    for i in the_almighty_list:
        print(i)

menu()
