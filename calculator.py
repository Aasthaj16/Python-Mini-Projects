welcome_msg = """

---Welcome to the calculator---"""

print(welcome_msg)


def addition(x, y):
    return x+y


def substraction(x, y):
    return x-y


def multiplication(x, y):
    return x*y


def division(x, y):
    return x//y


List_of_operations = '''
    1. Addition
    2. Substraction
    3. Multiplication
    4. Division'''
choice = ""
while(choice != "e"):
    print(List_of_operations)
    choice = input(
        "Choose any number from the list given above or 'e' to exit ")
    if(choice == "e"):
        break
    elif(int(choice) > 4):
        print("Enter valid value")
        continue
    var_1, var_2 = [int(var1) for var1 in input("Enter two values: ").split()]
    # print(var_1, var_2)
    if(choice == "1"):
        print("Addition:", addition(var_1, var_2))
    elif(choice == "2"):
        print("Substraction:", substraction(var_1, var_2))
    elif(choice == "3"):
        print("Multiplication:",  multiplication(var_1, var_2))
    elif(choice == "4"):
        print("Division:", division(var_1, var_2))

Ending_msg = """

----Thankyouu for using the calculator!!!----
"""
print(Ending_msg)
