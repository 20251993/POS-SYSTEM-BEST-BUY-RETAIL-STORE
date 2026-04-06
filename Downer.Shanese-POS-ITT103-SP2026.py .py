#POS SYSTEM - BEST BUY RETAIL STORE
#Product Catalog storing item name, price and available stock
products = {
    "Rice": {"price": 300, "stock": 12},
    "Flour": {"price": 200, "stock": 12},
    "Bread": {"price": 600, "stock": 3},
    "Sugar": {"price": 100, "stock": 12},
    "Salt": {"price": 100, "stock": 5},
    "Cooking Oil": {"price": 400, "stock": 5},
    "Tang": {"price": 50, "stock": 12},
    "Jack Mackerel": {"price": 500, "stock": 6},
    "Tissue": {"price": 150, "stock": 12},
    "Soap": {"price": 50, "stock": 12}
}
#Dictionary to store shopping cart: name -> quantity
cart = {}

#Function for user to add items to shopping cart
def add_item():
    try:
        name = input("Enter product name: ")
        if name not in products:
            print("Product not found. ")
            return
        #Get quantity and verify valid input
        quantity: int= int(input("Enter quantity: "))

        #Check Stock Availability
        if quantity >products[name]["stock"]:
            print("Low stock available. ")
            return

        #Add item to cart or update existing quantity of item
        if name in cart:
            cart[name]+= quantity
        else:
            cart[name]= quantity
        #Reduce Stock after adding item to cart
        products[name]["stock"]-=quantity
        print("Item added to cart.")
    #Check for invalid numeric input
    except ValueError:
        print("Invalid input. Enter numbers only.")

#Function to remove items from cart
def remove_item():
    name = input("Enter product name to remove: ")
    if name in cart:
        del cart[name]
        print("Item removed from cart.")
    else:
        print("Item not found in cart. ")

#Function to display items in cart with subtotal
def view_cart():
    if cart == {}:
        print("cart is empty. ")
        return
    subtotal=0
    #Loop through cart and calculate total cost
    for name, quantity in cart.items():
        price=products[name]["price"]
        item_total=price*quantity
        subtotal += price*quantity
        print(f"{name} x {quantity} = ${item_total}")

    print(f"Subtotal: ${subtotal}")

#Function to process checkout -> total bill, apply tax, apply discount
#and process payment
def checkout():
    if cart == {}:
        print("cart is empty.")
        return
    #Calculate Subtotal
    subtotal = 0

    for name, quantity in cart.items():
        subtotal +=products[name]["price"] * quantity
    #Apply 10% tax
    tax = subtotal*0.10

    #Apply discount if subtotal exceeds 5000
    discount = 0
    if subtotal >5000:
         discount = subtotal*0.05
    #Calculate total including tax and discount
    total = subtotal + tax -discount

    #Display bill summary to user
    print(f"Subtotal:${subtotal}")
    print(f"Tax:${tax}")
    print(f"Discount:${discount}")
    print(f"Total:${total}")

    #Process customer payment and change calculation
    #Loop will ensure user enters a valid input and sufficient payment
    while True:
        try:
            payment = float(input("Enter amount paid: "))
            #Check if payment is sufficient to cover cost
            if payment<total:
                print("insufficient funds.")
            else:
                change = payment - total
                print(f"Change: ${change}")
                print("payment successful.")
                #Generate receipt and clear cart after transaction is complete
                generate_receipt(subtotal, tax, discount, total, payment, change)
                cart.clear()
                break
        #Check for invalid numeric input
        except ValueError:
            print("Invalid input. Enter numbers only.")

#Function to generate receipt
def generate_receipt(subtotal, tax, discount, total, payment, change):
    print("\n===BEST BUY RETAIL STORE===")
    print("\n---RECEIPT---")
    #Display each item purchased with quantity and cost
    for name, quantity in cart.items():
        price=products[name]["price"]
        print(f"{name} x{quantity} @${price} =${price*quantity}")

    print("-------------------")
    #Display transaction summary
    print(f"Subtotal: ${subtotal}")
    print(f"Tax: ${tax}")
    print(f"Discount: ${discount}")
    print(f"Total: ${total}")
    print(f"Paid: {payment}")
    print(f"Change: ${change}")
    print("Thank you for Shopping with us!")

#Function to alert user when a product has a low stock count below 5 units
#5 units being minimum low stock threshold
def check_low_stock():
    print("/n---LOW STOCK ALERT---")
    #Loop through all products in the catalog
    for name in products:
        #Check if stock is below minimum threshold
        if products[name]["stock"]<5:
            print(f"{name} stock is low ({products[name]['stock']} left)")

#Program loop that continuously displays the menu and allows for multiple
#transactions until user exits
while True:
    #Display menu options to the user
        print("/n---POS MENU---")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")
        #Get user to input choice
        choice = input("Enter choice:")
        #Run the appropriate function based on user choice
        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            checkout()
        elif choice == "5":
            print("Exiting this page")
            break
        else:
            print("Invalid choice")
