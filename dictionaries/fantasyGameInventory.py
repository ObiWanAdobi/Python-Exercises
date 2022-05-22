import pprint

inventoryExample = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot =  ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


#Task 1: Fantasy Game Inventory
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for a in inventory:
        print(str(inventory[a]) + ' ' + a)
        item_total += inventory[a]
    print("Total number of items: " + str(item_total))

displayInventory(inventoryExample)


#Task 2: 
def addToInventory(inventory, addedItems):
    oldinventory = inventory.copy()

    for newItem in addedItems:
        if newItem in inventory:
            #print("\t added " + newItem + " to the inventory")
            inventory[newItem] += 1
        else:
            #print("\t added a total new item !! =>> !! " + newItem + " !! to the inventory")
            inventory[newItem] = 1

    checkChange(oldinventory, inventory)

def checkChange(oldint, newint):
    print("Loot is:")
    for a in oldint:
        print("\t " + a + " + " + str(newint[a]-oldint[a]))
    for a in newint:
        if a not in oldint:
            print("\t " + a + " + " + str(newint[a]) + " (new Item)")



#displayInventory(inventoryExample)
print("looted a dragon \n")
addToInventory(inventoryExample, dragonLoot)
#displayInventory(inventoryExample)

