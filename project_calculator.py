print("My Calculator")
print("<==================>")

print("1. Add")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

opt_menu = input("Please select option 1,2,3,4 or 5 to exit: ")

if opt_menu == "5":
    print("Program Exit")
    exit()


def my_cal(a, b):

    if opt_menu == "1":
        return a + b

    elif opt_menu == "2":
        return a - b

    elif opt_menu == "3":
        return a * b

    elif opt_menu == "4":
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    else:
        return "Invalid option"


value_a = int(input("Enter number a: "))
value_b = int(input("Enter number b: "))

result = my_cal(value_a, value_b)

print("Answer is:", result)
