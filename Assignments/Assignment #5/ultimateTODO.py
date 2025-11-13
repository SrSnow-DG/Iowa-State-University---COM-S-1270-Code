# Guillermo Montiel             11-13-2025
# Assignment #5 - The Ultimate TODO List!
# This application tracks tasks using a Dictionary of Lists with the categories:
# backlog, todo, in_progress, in_review, done. You can add, move, delete items,
# save to a .lst file and load it later from the main menu.

import sys
import pickle

def printTitleMaterial():
    print("The Ultimate TODO List!")
    print()
    print("By: Guillermo Montiel")
    print("[COM S 127 1]")
    print()

def initList():
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []
    return todoList

def checkIfListEmpty(todoList):
    if (len(todoList["backlog"]) > 0 or 
        len(todoList["todo"]) > 0 or
        len(todoList["in_progress"]) > 0 or
        len(todoList["in_review"]) > 0 or
        len(todoList["done"]) > 0):
        return False
    return True

def saveList(todoList):
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()

def loadList():
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    return todoList

def checkItem(item, todoList):
    for k in todoList.keys():
        lst = todoList[k]
        for i, v in enumerate(lst):
            if v == item:
                return True, k, i
    return False, "", -1

def addItem(item, toList, todoList):
    found, keyName, index = checkItem(item, todoList)
    if not found:
        todoList[toList].append(item)
    else:
        print("ERROR: '{0}' already exists in '{1}' at index {2}.".format(item, keyName, index))
    return todoList

def deleteItem(item, todoList):
    itemFound, keyName, index = checkItem(item, todoList)
    if itemFound:
        todoList[keyName].pop(index)
    else:
        print("ERROR: '{0}' does not exist.".format(item))
    return itemFound, todoList

def moveItem(item, toList, todoList):
    itemFound, todoList = deleteItem(item, todoList)
    if itemFound:
        addItem(item, toList, todoList)
    return todoList

def printTODOList(todoList):
    for key in todoList.keys():
        print("{0}: {1}".format(key, todoList[key]))
    return None

def runApplication(todoList):
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()
        if choice == "a":
            item = input("Enter An Item: ")
            addItem(item, "backlog", todoList)
            printTODOList(todoList)
        elif choice == "m":
            if not checkIfListEmpty(todoList):
                item = input("Enter An Item To Move: ")
                found, keyName, index = checkItem(item, todoList)
                while not found:
                    print("ERROR: '{0}' does not exist!".format(item))
                    item = input("Enter A Different Item To Move: ")
                    found, keyName, index = checkItem(item, todoList)
                dest = input("Enter The List To Move {0} To: ".format(item))
                while dest not in todoList.keys():
                    print("ERROR: '{0}' is not a valid list key!".format(dest))
                    dest = input("Enter The List To Move {0} To: ".format(item))
                moveItem(item, dest, todoList)
            else:
                print("No items to move!")
            printTODOList(todoList)
        elif choice == "d":
            if not checkIfListEmpty(todoList):
                item = input("Enter An Item To Delete: ")
                deleteItem(item, todoList)
            else:
                print("No items to delete!")
            printTODOList(todoList)
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()
    return todoList

def main():
    taskOver = False
    printTitleMaterial()
    while not taskOver:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n":
            todoList = initList()
            printTODOList(todoList)
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()
            printTODOList(todoList)
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()
