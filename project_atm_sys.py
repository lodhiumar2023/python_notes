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


# FUNCTION FOR PRINT LIST
def print_list(list):
    for x in list:
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
        print("CASH WITHDRAWAL")  # --> Menu will be added
    elif menu_option == "2":
        print("Rs.50,000")
    elif menu_option == "3":
        print("PLEASE ENTER YOUR NEW PIN")  # --> Menu will be added
    else:
        print("Wrong Menu")


else:
    print("Wrong Menu, please select (y/n)")
