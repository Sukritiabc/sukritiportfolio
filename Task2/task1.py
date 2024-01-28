import sys
def get_total_price(pizzas, tuesday, app_order, delivery):
    pizza_price = 12.0

    if tuesday == "y":
        pizza_price *= 0.5
    elif tuesday != "n":
        print("Please answer y or n fo is it tuesday")
    total_pizza_price = pizzas * pizza_price

    if app_order == "y":
        total_pizza_price *= 0.75
    elif app_order != "n":
        print("Please answer y or n for is order from the app")
        return None

    total = total_pizza_price + delivery
    return round(total, 2)

def get_delivery_cost(pizzas):
    delivery = 2.5
    if pizzas >= 5:
        delivery = 0
    return delivery

def main():
    try:
        pizzas = int(input("Enter the number of pizzas: "))
        if pizzas<0:
            print("please enter valid number")
            sys.exit()
    except ValueError:
        print("Please enter a valid number for the number of pizzas.")
        return  # Exit the program if input is not valid

    tuesday = input("Is it Tuesday? (y/n): ").lower()
    app_order = input("Is the order from the app? (y/n): ").lower()
    delivery = input("is delivery required?(y/n): ").lower()=="y"
    total= get_total_price(pizzas, tuesday, app_order, delivery)
    
    if total is not None:
        print(f"The total price for the order is £{total}.")
    else:
        sys.exit()

if __name__ == "__main__":
    main()
