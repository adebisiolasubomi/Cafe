#product catalogue items
products = [
    ["Iced Toffee Nut Latte", 4.50],
    ["Caramel Waffle Latte", 3.50],
    ["Iced Caramel Waffle Latte", 2.75],
    ["Iced White Chocolate Mocha", 8.90],
    ["Gingerbread Latte", 7.55],
    ["Classic Hot Chocolate", 4.50],
    ["White Hot Chocolate", 8.30],
    ["All Day Breakfast Wrap", 7.50]
]

# this function just prints out the menu. simple stuff.
def show_menu():
    print("--- café menu ---")
    print("item".ljust(30) + "price")
    print("-" * 40)
    # loop through all the items in the products list and print them.
    for product in products:
        print(f"{product[0].ljust(30)} £ {product[1]:.2f}")
    print()  # blank line for spacing

# this function is for adding items to the cart.
# the cart is just a list where we put the items the user wants to buy.
def add_to_cart(cart):
    # ask the user what they want to add
    item_name = input("enter the name of the item to add to your cart: ").strip()
    found = False  # this is to check if we actually found the item in the menu
    for product in products:  # loop through the menu items
        # check if the user's input matches an item (ignoring case)
        if product[0].strip().lower() == item_name.lower():
            cart.append(product)  # add the item to the cart
            print(f"{product[0]} has been added to your cart.")  # tell them it worked
            found = True  # mark it as found so we don't print the error message
            break
    # if we didn't find the item, print an error message
    if not found:
        print("item not found. please check the menu and try again.")

# this function shows the user what's in their cart
def view_cart(cart):
    print("--- your cart ---")
    if len(cart) == 0:  # check if the cart is empty
        print("your cart is empty. add something first!")
    else:
        total = 0  # this will store the total cost of the items in the cart
        for item in cart:  # loop through the cart
            print(f"{item[0]} - £{item[1]:.2f}")  # print each item and its price
            total += item[1]  # add the item's price to the total
        print("-" * 40)  # separator line
        print(f"total: £{total:.2f}")  # print the total cost
    print()  # blank line for spacing

# this function is for when the user is done shopping and wants to checkout
def checkout(cart):
    if len(cart) == 0:  # check if the cart is empty
        print("your cart is empty. there's nothing to checkout.")
    else:
        print("thank you for your purchase! here's what you bought:")
        total = 0  # total cost of items
        for item in cart:  # loop through the cart
            print(f"{item[0]} - £{item[1]:.2f}")  # print each item and its price
            total += item[1]  # add the item's price to the total
        print("-" * 40)  # separator line
        print(f"grand total: £{total:.2f}")  # print the total cost
        print("have a nice day!")  # friendly goodbye message
    cart.clear()  # empty the cart after checkout

# main function to run the program
def main():
    cart = []  # this will store the user's selected items
    while True:  # loop until the user chooses to exit
        print("options:")
        print("1. add an item to your cart")
        print("2. view your cart")
        print("3. done (checkout)")
        # ask the user what they want to do
        choice = input("enter your choice (1-3): ").strip()

        # check the user's input and call the appropriate function
        if choice == "1":
            add_to_cart(cart)
        elif choice == "2":
            view_cart(cart)
        elif choice == "3":
            checkout(cart)
            break  # exit the loop after checkout
        else:
            print("invalid option, try again.")  # if the input is invalid

# run the program
# first, we show the menu
show_menu()
# then, we run the main function
main()

# --- TESTING SECTION ---
# manually testing the program
# i’ll simulate a few inputs and outputs to make sure it’s working as expected.

print("\n--- TESTING ---")

# test case 1: add an item to the cart
print("\nTest Case 1: Adding 'Caramel Waffle Latte' to the cart")
cart = []  # clear the cart for testing
item_to_add = "Caramel Waffle Latte"
found = False
for product in products:
    if product[0] == item_to_add:
        cart.append(product)
        found = True
        print(f"Added: {item_to_add} - £{product[1]:.2f}")
        break
if not found:
    print(f"Item '{item_to_add}' not found in menu.")

# test case 2: viewing the cart
print("\nTest Case 2: Viewing the cart")
if cart:
    print("Cart contains:")
    for item in cart:
        print(f"- {item[0]}: £{item[1]:.2f}")
else:
    print("Cart is empty.")

# test case 3: checkout process
print("\nTest Case 3: Checkout process")
if cart:
    total = 0
    print("Items in your cart:")
    for item in cart:
        print(f"- {item[0]}: £{item[1]:.2f}")
        total += item[1]
    print(f"Total price: £{total:.2f}")
else:
    print("Cart is empty. Nothing to checkout.")

print("\n--- TESTING COMPLETE ---")
# --- END OF TESTING SECTION ---