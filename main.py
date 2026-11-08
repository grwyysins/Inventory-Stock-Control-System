class Product:

    def __init__(self, product_id, name, category, unit_price, quantity):

        self.product_id = product_id
        self.name = name
        self.category = category
        self.unit_price = unit_price
        self.quantity = quantity

    def display_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Unit Price: KSH {self.unit_price}")
        print(f"Quantity in stock: {self.quantity}")

    def calculate_stock_value(self):

        return self.unit_price * self.quantity


inventory = {}

product1 = Product("P001", "Sugar", "Food", 250, 10)
product2 = Product("P002", "Rice", "Food", 100, 3)
product3 = Product("P003", "Cooking Oil", "Household", 450, 9)

inventory[product1.product_id] = product1
inventory[product2.product_id] = product2
inventory[product3.product_id] = product3


def add_product():

    product_id = input("Enter Product ID: ")

    if product_id in inventory:
        print("Error! Product ID already exists.")
        return

    name = input("Enter Product Name: ")
    category = input("Enter Category: ")

    try:
        unit_price = float(input("Enter Unit Price: "))

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    if unit_price <= 0:
        print("Invalid price! Price must be greater than zero.")
        return

    try:
        quantity = int(input("Enter quantity needed: "))

    except ValueError:
        print("Invalid input! Please enter a whole number.")
        return

    if quantity < 0:
        print("Invalid quantity! Quantity cannot be negative.")
        return

    product = Product(product_id, name, category, unit_price, quantity)

    inventory[product_id] = product

    print("Product Added Successfully!")

def search_product():

    product_id = input("Enter Product ID to search: ")

    if product_id in inventory:

        product = inventory[product_id]

        print("\n===== PRODUCT FOUND =====")
        product.display_details()

    else:
        print("Product not found!")


def update_stock():

    product_id = input("Enter Product ID: ")

    if product_id not in inventory:
        print("Product not found!")
        return

    product = inventory[product_id]

    print("1. Add stock")
    print("2. Remove stock")

    choice = input("Choose an option: ")

    if choice == "1":

        try:
            quantity = int(input("Enter quantity to add: "))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            return

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

        product.quantity += quantity
        print("Stock added successfully!")

    elif choice == "2":

        try:
            quantity = int(input("Enter quantity to remove: "))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            return

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

        if quantity > product.quantity:
            print("Insufficient stock!")
            return

        product.quantity -= quantity
        print("Stock removed successfully!")

    else:
        print("Invalid choice!")

    print(f"Updated quantity: {product.quantity}")


def record_sale():

    product_id = input("Enter Product ID: ")

    if product_id not in inventory:
        print("Product not found!")
        return

    product = inventory[product_id]

    try:
        quantity = int(input("Enter quantity sold: "))
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero!")
        return

    if quantity > product.quantity:
        print("Insufficient stock!")
        return

    total = quantity * product.unit_price

    product.quantity -= quantity

    print("\n<=-=-= SALES RECEIPT =-=-=>")
    print(f"Product: {product.name}")
    print(f"Quantity Sold: {quantity}")
    print(f"Unit Price: KSh {product.unit_price}")
    print(f"Total Amount: KSh {total}")
    print(f"Remaining Stock: {product.quantity}")
    print("--==--==--==--==--==--==--==--==")


def check_low_stock():

    print("\n<=-=-= LOW STOCK ALERTS =-=-=>")

    for product_id, product in inventory.items():

        if product.quantity < 5:
            print(f"WARNING: {product.name} is running low!")
            print(f"Remaining Quantity: {product.quantity}")
            print("-------------------------")


def calculate_total_inventory_value():
    total_value = 0

    for product_id, product in inventory.items():

        stock_value = product.calculate_stock_value()

        total_value += stock_value

    print(f"\nTotal Inventory Value: KSh {total_value:,.2f}")


def display_all_products():

    print("\n<=-=-= ALL INVENTORY PRODUCTS =-=-=>")

    for product_id, product in inventory.items():

        product.display_details()
        print("-------------------------")


def main_menu():

    while True:

        print("\n<=-=-= INVENTORY MANAGEMENT SYSTEM =-=-=>")
        print("1. Add Product")
        print("2. Search Product")
        print("3. Update Stock")
        print("4. Record Sale")
        print("5. Check Low Stock")
        print("6. Calculate Total Inventory Value")
        print("7. Display All Products")
        print("8. Exit")

        choice = input("Select an option (1-8): ")

        if choice == "1":
            add_product()

        elif choice == "2":
            search_product()

        elif choice == "3":
            update_stock()

        elif choice == "4":
            record_sale()

        elif choice == "5":
            check_low_stock()

        elif choice == "6":
            calculate_total_inventory_value()

        elif choice == "7":
            display_all_products()

        elif choice == "8":
            print("Thank you for using my Inventory Management System!")
            break

        else:
            print("Invalid choice! Please select an option between 1 and 8.")

main_menu()
