#Panos30fyllou - February 2020
import sys
def ask_for_input():
    valid_test(list(input("Enter a string consisted by x and y\n")))
def dpda(a):
    status = "k1"
    stack = ["$"]
    print("\nStack \t\tState \t\tSymbols from input remaining")
    for str in stack:
        print(str, end = "")
    print("\t\t", end = "")
    for str in status:
        print(str, end = "")
    print("\t\t", end = "")
    for char in a:
        print(char, end = "")
    print("")
    for x in range(len(a)):
        if status == "k1":
            if a[0] == "y":
                break
            else:
                stack.append(a[0])
                status = "k2"                   
        elif status == "k2":
            if a[0] == "y":
                stack.pop()
                if stack[len(stack)-1] == "$":  status = "k1"
            else:
                stack.append(a[0])
        a.pop(0)
        for str in stack:
             print(str, end = "")
        print("\t\t", end = "")
        for str in status:
            print(str, end = "")
        print("\t\t", end = "")
        for char in a:
             print(char, end = "")
        print("")
    print ("\nYes" if status == "k1" and stack[0] == "$" and len(a) == 0 else "\nNo")
    try_again()
def valid_test(a):
    valid = True
    for char in a:
        if not(char == "x" or char == "y"):
            valid = False
            break            
    if not valid:
        print("Invalid string. The string must be consisted only by x and y.")
        ask_for_input()
    else:
        dpda(a)
def try_again():
    r = input("Do you want to try an other string? (y/n)")
    if r == "y":
        print("")
        ask_for_input()
    elif r == "n":  sys.exit(0)
    else:           try_again()
ask_for_input()