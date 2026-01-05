def main():
    dic = {}
    max_price = 0
    expensive_item = None
    for i in range(5):
        item = input("Enter item name: ")
        price = int(input("Enter item price: "))
        dic[item] = price
        if price > max_price:
            max_price = price
            expensive_item = item
    print(dic)
    print(f"Most expensive is {expensive_item}")


main()