class GroceryList:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity):
        for item in self.items:
            if item.name == name:
                item.quantity += quantity
                return
        self.items.append(Item(name, quantity))

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]

    def show_list(self):
        if not self.items:
            print("Your grocery list is empty.")
        else:
            print("Your Grocery List:")
            for item in self.items:
                print(f"- {item}")

# Create GroceryList instance
my_list = GroceryList()

# Add to list
my_list.add_item("Apples", 5)
my_list.add_item("Bread", 2)
my_list.add_item("Milk", 1)

# Show list
my_list.show_list()

# Remove item
my_list.remove_item("Bread")

# Display updated list
my_list.show_list()
