# ATM Machine System

# Insert ATM (y/n) --> y
# Please enter your pin --> ****


# WELCOME TO MAIN MENU
# ====================
# 1. Cash Withdrawal
# 2. Balance Enquiry
# 3. Change Pin Code
# 4. Exit


# GLOBAL VARIABLES
balance = 50000
pin_code = "1234"
insert_card = input("please insert card (y/n):").lower()
main_menu = [
    "WELCOME TO MAIN MENU",
    "=====================",
    "1. Cash Withdrawal",
    "2. Balance Enquiry",
    "3. Change Pin Code",
    "4. Exit"
]

cash_draw_menu = [
    "1. Rs.500",
    "2. Rs.1000",
    "3. Rs.2000",
    "4. Rs.3000",
    "5. Rs.4000",
    "6. Rs.5000",
    "7. Rs.10000"
]


# FUNCTION FOR PRINT LIST
def print_list(items):
    for x in items:
        print(x)


if insert_card == "n":
    print("Thanks you for using ATM Service.")


elif insert_card == "y":
    your_pin = input("Please type your pin code: ")

    if your_pin == pin_code:
        print_list(main_menu)
        menu_option = input("Please select menu option 1,2,3 or 4: ")
    else:
        print("Wrong pin")
        exit()

    if menu_option == "4":
        print("Thanks you for using ATM Service.")

    elif menu_option == "1":
        print_list(cash_draw_menu)
        cash_option = input("Please select 1,2,3,4,5,6 or 7: ")

        # CASH DRAW MENU
        if cash_option == "1":
            print("You draw Rs.500")
            print("Thanks you for using ATM Service.")
        elif cash_option == "2":
            print("You draw Rs.1000")
            print("Thanks you for using ATM Service.")
        elif cash_option == "3":
            print("You draw Rs.2000")
            print("Thanks you for using ATM Service.")
        elif cash_option == "4":
            print("You draw Rs.3000")
            print("Thanks you for using ATM Service.")
        elif cash_option == "5":
            print("You draw Rs.4000")
            print("Thanks you for using ATM Service.")
        elif cash_option == "6":
            print("You draw Rs.5000")
            print("Thanks you for using ATM Service.")
        elif cash_option == "7":
            print("You draw Rs.10000")
            print("Thanks you for using ATM Service.")
        else:
            print("Selected Wrong Option")

    elif menu_option == "2":
        print(balance)

    # CHANGE PIN CODE
    elif menu_option == "3":
        change_pin_code = input("Please enter your new pin: ")
        print("Your pin has been successfully changed!")

    else:
        print("Wrong Menu")

else:
    print("Wrong Menu, please select (y/n)")
