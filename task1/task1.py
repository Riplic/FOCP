def calculate_order_cost(num_pizzas, include_delivery, is_tuesday, order_via_app):
    """
    Calculate the total cost of an order based on the number of pizzas, delivery option, day of the week,
    and whether the order is placed via the BPP App.

    Parameters:
    - num_pizzas (int): The number of pizzas in the order.
    - include_delivery (bool): True if the order includes delivery, False for collection.
    - is_tuesday (bool): True if it's Tuesday, False otherwise.
    - order_via_app (bool): True if the order is placed via the BPP App, False otherwise.

    Returns:
    - float: The total cost of the order.
    """
    base_price_per_pizza = 12.0
    delivery_cost = 2.50
    free_delivery_threshold = 5
    tuesday_discount = 0.5  # 50% discount on Tuesdays
    app_discount = 0.75  # 25% discount for orders via the BPP App

    # Apply a 50% discount on all pizza prices if it's Tuesday
    if is_tuesday:
        base_price_per_pizza *= tuesday_discount

    total_cost = num_pizzas * base_price_per_pizza

    # Add delivery cost if applicable
    if include_delivery and num_pizzas < free_delivery_threshold:
        total_cost += delivery_cost

    # Apply additional 25% discount for orders via the BPP App
    if order_via_app:
        total_cost *= app_discount

    return total_cost



def main():
    while True:
        try:
            num_pizzas = int(input("Enter the number of pizzas: "))
            if num_pizzas < 1:
                raise ValueError("Please enter a positive integer greater than 0!")
            break  # Exit the loop if the input is valid
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter a valid positive integer greater than 0.")

    while True:
        include_delivery_input = input("Is delivery required? (yes/no): ").lower()
        if include_delivery_input in ['yes', 'no']:
            include_delivery = include_delivery_input == 'yes'
            break
        else:
            print("Error: Please enter 'yes' or 'no'.")

    while True:
        is_tuesday_input = input("Is it Tuesday? (yes/no): ").lower()
        if is_tuesday_input in ['yes', 'no']:
            is_tuesday = is_tuesday_input == 'yes'
            break
        else:
            print('Error: Please answer "yes" or "no".')

    while True:
        order_via_app_input = input("Did the customer use the app? (yes/no): ").lower()
        if order_via_app_input in ['yes', 'no']:
            order_via_app = order_via_app_input == 'yes'
            break
        else:
            print('Error: Please answer "yes" or "no".')

    order_cost = calculate_order_cost(num_pizzas, include_delivery, is_tuesday, order_via_app)

    print("\nOrder summary:")
    print(f"Number of pizzas: {num_pizzas}")
    print(f"Include delivery: {'Yes' if include_delivery else 'No'}")
    print(f"Is it Tuesday: {'Yes' if is_tuesday else 'No'}")
    print(f"Did the customer use the app: {'Yes' if order_via_app else 'No'}")
    print(f"Total cost: ${order_cost:.2f}")

if __name__ == "__main__":
    main()
