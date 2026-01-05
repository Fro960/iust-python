def main():
    get_input()

def get_input():
    grocery_list = {}
    for i in range(5):
        item_name = input("Enter item: ")
        price = int(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        category = input("Enter category: ")
        grocery_list[item_name] = {"price": price, "quanity": quantity, "category": category}
    return grocery_list

def total_amount():
    grocery = get_input()
    bill = 0
    for items in grocery:
        bill += items["price"]
    return bill

def get_items():
    grocery = get_input()
    total_items = 0
    for items in grocery:
        total_items += 1
    return total_items

def quantity(grocery):
    for items in grocery:
        print(f"{items} : {items["quantity"]}")

def most_expensive(grocery):
    max = 0
    for items in grocery:
        if items["price"] > max:
            max = items["price"]
    print(max)

def most_items(grocery):
    maxm = {}
    for items in grocery:
        if items["grocery"] in max:
            items["grocery"] += 1
        else:
            max[items] = items["grocery"]
    print(max(maxm))

main()
