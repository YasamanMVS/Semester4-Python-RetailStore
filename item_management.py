from database import connect_db


# Function to add a new item to database
def add_item(name, cost):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''INSERT INTO Items (name, cost) VALUES (?, ?)''', (name, cost))
    conn.commit()
    conn.close()
    print(f"Item {name} with price ${cost} added successfully.")



# Check the validation of user inputs
def input_validation(prompt, validation_func, error_message):
    while True:
        input_value = input(prompt)
        if validation_func(input_value):
            return input_value
        else:
            print(error_message)


# Create an item with user input
def create_item():
    while True:
        item_name = input_validation(
            "Enter Item Name:  ",
            lambda x: x.strip() !="",
            "Item Name cannot be empty!! Please enter again."
        )

        item_cost = input_validation(
            "Enter Item Price:  ",
            lambda x: x.isdigit(),
            "Item Price must be an integer!! Please enter again."
        )

        # Adding the new item to the item list
        add_item(item_name, int(item_cost))

        # If user wants to add another item
        another = input("Would you like to add another item? (YES/NO):  ").strip().lower()
        if another != "yes":
            break


# Function to retrieve a list of items from database
def list_items():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''SELECT item_number, name, cost FROM Items''')
    print("Available Items: ")
    print("Item Number   | Item Name   | Item Cost")
    for item in cur.fetchall():
        print(f"{item[0]}             | {item[1]}       | ${item[2]:.2f}")
    conn.close()


# Display items from database
def display_items():
    list_items()
