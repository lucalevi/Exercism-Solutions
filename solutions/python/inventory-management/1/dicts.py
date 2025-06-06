"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    return add_items({}, items)

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    # loop over the items list
    for item in items:
    # if an item is already present in inventory, add 1
        if item in inventory:
            inventory[item] += 1
    # otherwise, create a new item in inventory and set its value to 1
        else:
            inventory[item] = 1
            
    # return the inventory
    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

     # loop over the items list
    for item in items:
        if item in inventory:
            # Only decrement if the count is greater than 0
            if inventory[item] > 0:
                inventory[item] -= 1

    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    # check if the item is in inventory
    if item in inventory:
    # if so, remove it
        inventory.pop(item)
    # if not, return the inventory
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    # create an empty list
    tuple_list = []
    # loop over the inventory
    for key in inventory:
        # if the quantity is higher than 0
        if inventory[key] > 0:
        # create a key-value tuple 
            tuple = (key, inventory[key])
        # push the tuple to the list
            tuple_list.append(tuple)
            
    # return the list
    return tuple_list

