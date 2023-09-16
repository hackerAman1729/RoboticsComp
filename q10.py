def manage_inventory(N, initial_items, M, operations):
  inventory = {item_name: quantity for item_name, quantity in initial_items}

  for operation in operations:
    op, item_name, quantity = operation

    if op == "ADD":
      if item_name in inventory:
        inventory[item_name] += quantity
        print(f"UPDATED Item {item_name}")
      else:
        inventory[item_name] = quantity
        print(f"ADDED Item {item_name}")

    elif op == "DELETE":
      if item_name not in inventory:
        print(f"Item {item_name} does not exist")
      else:
        if inventory[item_name] < quantity:
          print(f"Item {item_name} could not be DELETED")
        else:
          inventory[item_name] -= quantity
          print(f"DELETED Item {item_name}")

  print(f"Total Items in Inventory: {sum(inventory.values())}")


def main():
  T = int(input())
  for _ in range(T):
    N = int(input())
    initial_items = [tuple(input().split()) for _ in range(N)]
    initial_items = [(item[0], int(item[1])) for item in initial_items]

    M = int(input())
    operations = [tuple(input().split()) for _ in range(M)]
    operations = [(item[0], item[1], int(item[2])) for item in operations]

    manage_inventory(N, initial_items, M, operations)


main()
