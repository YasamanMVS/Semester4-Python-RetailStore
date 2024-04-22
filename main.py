"""
Student Name:   Yasaman Mirvahabi Sabet
Student ID:     101217770
Lab Professor:  Maziar Sojoudian

"""

from employee_management import create_employee, display_employees
from item_management import create_item, display_items
from purchase_management import make_purchase
from database import create_table


def print_main_menu():
    print("——————————————————————————————")
    print("|          MAIN MENU          |")
    print("|                             |")
    print("| 1. Create Employee          |")
    print("| 2. Create Item              |")
    print("| 3. Make Purchase            |")
    print("| 4. All Employee Summary     |")
    print("| 5. Exit                     |")
    print("|                             |")
    print("——————————————————————————————")
    option = input("Enter your option  (1-5):  ")
    return option

def post_action_prompt():
    response = input("Do you want to go back to the Main Menu? (YES/NO): ").strip().lower()
    return response == "yes"

def main():
    create_table()
    while True:
        option = print_main_menu()
        if option == '1':
            create_employee()
        elif option == '2':
            create_item()
        elif option == '3':
            make_purchase()
        elif option == '4':
            display_employees()
        elif option == '5':
            print("Exiting the program..")
            break
        else:
            print("Invalid option. Please choose option between 1 to 5.")

        if option != '5':
            if not post_action_prompt():
                print("Exiting the program..")
                break

if __name__ == "__main__":
    main()