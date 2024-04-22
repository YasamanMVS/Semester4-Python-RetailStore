from database import connect_db
from item_management import display_items
from employee_management import display_employees

def calculate_discount(employee, item_price):
    years_worked = int(employee[3])
    is_manager = employee[2].lower() == 'manager'
    discount_percentage = min(10, 2 * years_worked) + (10 if is_manager else 0)
    discount_amount = (discount_percentage / 100) * item_price
    return min(discount_amount, 200)


def make_purchase():
    while True:
        display_items()
        discount_number = input("Enter your employee discount number:  ")
        conn = connect_db()
        cur = conn.cursor()

        cur.execute("SELECT * FROM Employees WHERE discount_number = ?", (discount_number,))
        employee = cur.fetchone()
        if not employee:
            print("Invalid employee discount number.")
            cur.close()
            continue

        item_number = input("Enter the item number you wish to purchase:  ")
        cur.execute("SELECT * FROM Items WHERE item_number = ?", (item_number,))
        item = cur.fetchone()
        if not item:
            print("Invalid item number.")
            cur.close()
            continue

        item_price = item[2]
        discount = calculate_discount(employee, item_price)
        final_price = item_price - discount

        # Updating the employee purchase records
        new_total_purchased = employee[4] + final_price
        new_total_discounts = employee[5] + discount
        cur.execute("UPDATE Employees SET total_purchased = ?, total_discounts = ? WHERE discount_number = ?",
                    (new_total_purchased, new_total_discounts, discount_number))
        conn.commit()
        print(f"Purchase successful. Final price after discount: ${final_price:.2f}")

        cur.close()

        # Another purchase
        new_purchase = input("Would you like to make another purchase? (YES/NO): ").lower()
        if new_purchase != "yes":
            display_employees()
            break