playerInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'bananas':99, 'pants': 1,}

def inventoryFunction(any_inventory):
    print("Your Inventory:")
    item_total = 0
    for x,y in any_inventory.items():
        print(x,y)
        item_total += y
    print("The total number of items is " + str(item_total) + '.')

inventoryFunction(playerInventory)
