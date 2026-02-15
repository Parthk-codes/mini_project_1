print("Welcome to our Restaurant!")
print("Here's our menu:")

Menu = {
    "Pizza": 100,
    "Burger": 50,
    "Fries": 50,
    "Chowmein": 40,
    "Momos": 20
}
for key, value in Menu.items():
    print(f"{key}: Rs{value}")

Order_Total = 0

valid_items = []
invalid_items = []

items_input = input("\nEnter the items you want to order (separated by commas): ")

ordered_items = [item.strip().capitalize() for item in items_input.split(',')]

for item in ordered_items:
    if item in Menu:
        Order_Total += Menu[item]
        valid_items.append(item)
    elif item: # This ensures we don't process empty strings
        invalid_items.append(item)

if valid_items:
    print(f"\nAdded to your order: {', '.join(valid_items)}")

if invalid_items:
    print(f"Sorry, we don't have: {', '.join(invalid_items)}")

if Order_Total > 0:
    print(f"\nThank you for your order! Your total is: Rs{Order_Total}")
else:
    print("\nNo valid items were ordered.")
