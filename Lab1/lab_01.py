 
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
    name = input("Please enter name to be delated: ")
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
    name = input("Please enter name to be updated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
    
        del list[deletePosition]
    phone = input("Please enter student phone: ")
    group = input("please enter studentr group: ")
    avaragemark = input("Please enter studen avarage mark: ")
    newItem = {"name": name, "phone": phone, "group": group, "avarage mark": avaragemark}
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
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
            case "D" | "d":
                print("Element will be deleted")
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