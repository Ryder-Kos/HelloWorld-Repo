groceryList = []
costOfItem = []

def compare_grocery_purchases(groceryDict, secondGroceryDict):
    return groceryDict == secondGroceryDict

while True:
    item = input("Enter the name of the grocery item (or type 'DONE' to finish): ")
    if item == 'DONE':
        break
    cost = float(input(f"Enter the cost of {item}: "))
    
    groceryList.append(item)
    costOfItem.append(cost)

costOfItem = list(map(int, costOfItem))
groceryDict = dict(zip(groceryList, costOfItem))
total_amount = sum(costOfItem)

print(f"My grocery list is {groceryList}")
print(f"Cost for each item {costOfItem}")
print(groceryDict)
print(f"Total amount spent on grocery shopping is {total_amount}")

secondGroceryDict = {'bread': 3, 'milk': 2, 'eggs': 1, 'cheese': 4}
print(f"\nSecond Grocery Purchase:\n{secondGroceryDict}")

result = compare_grocery_purchases(groceryDict, secondGroceryDict)
if result:
    print("The grocery purchases are the same.")
else:
    print("The grocery purchases are different.")
    items1 = set(groceryDict.keys())
    items2 = set(secondGroceryDict.keys())
    mixed_items1 = items1.difference(items2)
    mixed_items2 = items2.difference(items1)

    different_prices = {item: secondGroceryDict.get(item, 0) - groceryDict.get(item, 0) for item in items1}

    for item, price_difference in different_prices.items():
        if price_difference > 0:
            print(f"{item} is cheaper on purchase1.")
        elif price_difference < 0:
            print(f"{item} is cheaper on purchase2.")
        else:
            print(f"{item} has the same price in both purchases.")
            
    for item in mixed_items1:
        print(f"{item} is only on purchase1.")   
    for item in mixed_items2:
        print(f"{item} is only on purchase2.")

groceryPurchase = {
    'banana': (5, 10),
    'apple': (1, 3),
    'orange': (3, 2)
}

for item, (quantity, price) in groceryPurchase.items():
    item_name = item if quantity == 1 else f"{item}s"
    print(f"Purchase {quantity} {item_name} at cost {price} dollars each.")

