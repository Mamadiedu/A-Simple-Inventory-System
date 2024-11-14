inventory = {}

def add_item():
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    inventory[item_name] = inventory.get(item_name, 0) + quantity
    print(f"{quantity} {item_name}(s) added to inventory.")

def update_quantity():
    item_name = input("Enter item name to update: ")
    if item_name in inventory:
        new_quantity = int(input("Enter new quantity: "))
        inventory[item_name] = new_quantity
        print(f"Quantity of {item_name} updated to {new_quantity}.")
    else:
        print(f"{item_name} not found in inventory.")

def retrieve_item():
    item_name = input("Enter item name to retrieve: ")
    if item_name in inventory:
        print(f"{item_name}: {inventory[item_name]}")
    else:
        print(f"{item_name} not found in inventory.")

def calculate_total_quantity():
    total_quantity = sum(inventory.values())
    print(f"Total quantity of all items: {total_quantity}")

while True:
    print("\nInventory System Menu")
    print("1. Add Item")
    print("2. Update Quantity")
    print("3. Retrieve Item")
    print("4. Calculate Total Quantity")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        update_quantity()
    elif choice == '3':
        retrieve_item()
    elif choice == '4':
        calculate_total_quantity()
    elif choice == '5':
        print("Exiting inventory system.")
        break
    else:
        print("Invalid choice. Please try again.")