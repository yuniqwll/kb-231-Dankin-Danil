
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", "group":"KB-231","avarage mark":"81"},
    {"name":"Emma", "phone":"0631234567","group":"KB-231","avarage mark":"84"},
    {"name":"Jon",  "phone":"0631234567", "group":"KB-231","avarage mark":"83"},
    {"name":"Zak",  "phone":"0631234567", "group":"KB-231","avarage mark":"82"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Group" + elem["group"] + "avarage mark is" + elem["avarage mark"]
        print(strForPrint)
    return 

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    group = input("please enter studentr group: ")
    avaragemark = input("Please enter studen avarage mark: ")
    newItem = {"name": name, "phone": phone, "group": group, "avarage mark": avaragemark}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return

def updateElement():
    name_to_update = input("Please enter the name to be updated: ")
    found = False
    for student in list:
        if student["name"] == name_to_update:
            found = True
            # нові дані
            new_name = input("Please enter new name: ")
            new_phone = input("Please enter new phone: ")
            new_group = input("Please enter new group: ")
            new_avarage_mark = input("Please enter new average mark: ")
            
            # оновлення даних
            student["name"] = new_name
            student["phone"] = new_phone
            student["group"] = new_group
            student["avarage mark"] = new_avarage_mark
            
            print(f"Student '{name_to_update}' has been updated to '{new_name}'.")
            break
    
    if not found:
        print(f"Student with name '{name_to_update}' not found.")
    else:
        # Сортуємо список після оновлення
        list.sort(key=lambda x: x["name"])
        print("List has been re-sorted.")
    return

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deletped")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()