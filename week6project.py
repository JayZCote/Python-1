# Define the inventory list
inventory = []


# Function to add an item to the inventory
def add_item(name, price, quantity, category):
    item = {
        'name': name,
        'price': price,
        'quantity': quantity,
        'category': category
    }
    inventory.append(item)
    print(f"Item '{name}' added to inventory.")


# Function to update an item in the inventory
def update_item(name, price=None, quantity=None, category=None):
    for item in inventory:
        if item['name'] == name:
            if price is not None:
                item['price'] = price
            if quantity is not None:
                item['quantity'] = quantity
            if category is not None:
                item['category'] = category
            print(f"Item '{name}' updated.")
            return
    print(f"Item '{name}' not found in inventory.")


# Function to view all items in the inventory
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        for item in inventory:
            print(
                f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}, Category: {item['category']}")


# Function to remove an item from the inventory
def remove_item(name):
    for item in inventory:
        if item['name'] == name:
            inventory.remove(item)
            print(f"Item '{name}' removed from inventory.")
            return
    print(f"Item '{name}' not found in inventory.")


# Function to search for items by category
def search_by_category(category):
    found_items = [item for item in inventory if item['category'] == category]
    if not found_items:
        print(f"No items found in category '{category}'.")
    else:
        for item in found_items:
            print(
                f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}, Category: {item['category']}")


# Main loop to interact with the user
def main():
    while True:
        print("\nOptions: add, update, view, remove, search")
        choice = input("Choose an option: ").strip().lower()

        if choice == 'add':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            category = input("Enter item category: ")
            add_item(name, price, quantity, category)

        elif choice == 'update':
            name = input("Enter item name to update: ")
            price = input("Enter new price (leave blank to keep current): ")
            quantity = input("Enter new quantity (leave blank to keep current): ")
            category = input("Enter new category (leave blank to keep current): ")
            update_item(name, float(price) if price else None, int(quantity) if quantity else None,
                        category if category else None)

        elif choice == 'view':
            view_inventory()

        elif choice == 'remove':
            name = input("Enter item name to remove: ")
            remove_item(name)

        elif choice == 'search':
            category = input("Enter category to search: ")
            search_by_category(category)

        else:
            print("Invalid option. Please try again.")


# Run the main loop
if __name__ == "__main__":
    main()