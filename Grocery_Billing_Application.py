# Grocery Billing Application
#
# Grocery = {
#     product_id: 1  product_name: Maggie stock: 200 price: 23
#     product_id: 2  product_name: Biscuits stock: 1000 price: 50
# }
# menu -
# 1.Add new Product
# 2. show all product
# 3.Update specific product
# 4. Delete product
# 5.purchase product
#
# 5.which  product u want - - product_id - - 2
# how many qty u want - 20
# price - 200s
# pay - 200
# message - - Thanks for Visit our shop.Kindly collect your product
# do u want to continue -- Y then again display Menu otherwise exit from program

grocery = {'prod_1': {'name': 'maggie', 'qty': 200, 'price': 20},
           'prod_2': {'name': 'pencil', 'qty': 200, 'price': 10},
           'prod_3': {'name': 'perfume', 'qty': 100, 'price': 200},
           'prod_4': {'name': 'tpaste', 'qty': 150, 'price': 75},
           'prod_5': {'name': 'soap', 'qty': 120, 'price': 30},
           'prod_6': {'name': 'oilpkg', 'qty': 130, 'price': 120}}

print("prod_id\t\tname\t\tquantity\tprice")
print("-----------------------------------------------------")
for key, val in grocery.items():
    print(f"{key}\t\t{val['name']}\t\t{val['qty']}\t\t\t{val['price']}")

while True:
    print("Menu:")
    print("1. Add new product")
    print("2. Show all products")
    print("3. Update specific product")
    print("4. Delete product")
    print("5. Purchase product")
    choice = input("Enter your choice: ")

    if choice == '1':
        key = input("Enter product ID: ")
        if key in grocery:
            print("Product already exists.")
        else:
            name = input("Enter product name: ")
            qty = int(input("Enter stock quantity: "))
            price = int(input("Enter price: "))
            grocery[key] = {'name': name, 'qty': qty, 'price': price}
            print("Product added successfully.")

    elif choice == '2':
        for key, val in grocery.items():
            print(f"Product ID: {key}")
            for k, v in val.items():
                print(f"{k}: {v}")
            print()

    elif choice == '3':
        key = input("Enter product ID to update: ")
        if key not in grocery:
            print("Product does not exist.")
        else:
            for k, v in grocery[key].items():
                print(f"{k}: {v}")
            name = input("Enter new product name (** press enter to keep the same **): ")
            qty = int(input("Enter new stock quantity (** press 0 to keep the same **): "))
            price = int(input("Enter new price (** press 0 to keep the same **): "))
            if name:
                grocery[key]['name'] = name
            if qty != 0:
                if qty > grocery[key]['qty']:
                    print("")
                grocery[key]['qty'] = qty
            if price != 0:
                grocery[key]['price'] = price
            print("Product updated successfully.")

    elif choice == '4':
        key = input("Enter product ID to delete: ")
        if key not in grocery:
            print("Product does not exist.")
        else:
            del grocery[key]
            print("Product deleted successfully.")

    elif choice == '5':
        key = input("Enter the product ID you want to purchase: ")
        if key not in grocery:
            print("Product does not exist.")
        else:
            quantity = int(input("Enter the quantity you want to purchase: "))
            price = grocery[key]['price']
            total_price = price * quantity
            print(f"Total price: {total_price}")
            print(f"Please pay: {total_price}")
            payment = int(input("Enter the payment amount: "))
            if payment < total_price:
                print("Insufficient amount paid.")
            else:
                change = payment - total_price
                print("Thanks for visiting our shop. Kindly collect your product")
                print(f"Change: {change}")
                grocery[key]['qty'] -= quantity
                ques = input("Do you want to continue shopping? ")
                if ques == 'yes':
                    continue
                else:
                    break

    else:
        print("Invalid choice. Please try again.")
