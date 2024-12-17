# Function to display the menu
def display_menu(menu):
    print("Pizza Menu:")
    for pizza, price in menu.items():
        print(f"- {pizza}: RM {price}")

# Function to calculate total cost
def calculate_total(order_list, menu):
    return sum(menu[pizza] for pizza in order_list)

# Function to apply discounts
def apply_discount(total_cost, is_regular_customer):
    if total_cost > 100:
        discount = 0.15  # 15% discount for totals exceeding RM 100
        print("A 15% discount has been applied.")
    elif is_regular_customer:
        discount = 0.10  # 10% discount for regular customers
        print("A 10% discount has been applied.")
    else:
        discount = 0.0
        print("No discount applied.")

    discount_amount = total_cost * discount
    final_cost = total_cost - discount_amount
    return discount_amount, final_cost

# Main program
def main():
    # Pizza menu
    menu = {"Margherita": 25, "Pepperoni": 30, "BBQ Chicken": 35, "Veggie": 28}
    
    # Step 1: Display the menu
    display_menu(menu)
    
    # Step 2: Take orders
    order_list = []
    while True:
        order = input("\nEnter a pizza name to order (or type 'done' to finish): ").title()
        if order == 'Done':
            break
        elif order in menu:
            order_list.append(order)
            print(f"{order} has been added to your order.")
        else:
            print("We don't have that pizza. Please choose from the menu.")

    # Step 3: Check if the customer is regular
    is_regular_customer = input("\nAre you a regular customer? (yes/no): ").lower() == 'yes'

    # Step 4: Calculate total cost
    total_cost = calculate_total(order_list, menu)
    
    # Step 5: Apply discounts
    discount_amount, final_cost = apply_discount(total_cost, is_regular_customer)
    
    # Step 6: Display order summary
    print("\nOrder Summary:")
    print("Pizzas ordered:")
    for pizza in order_list:
        print(f"- {pizza}: RM {menu[pizza]}")
    print(f"Total Cost: RM {total_cost}")
    print(f"Discount: RM {discount_amount:.2f}")
    print(f"Final Cost: RM {final_cost:.2f}")

# Run the program
if __name__ == "__main__":
    main()
