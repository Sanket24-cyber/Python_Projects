class VendingMachine:
    def __init__(self):
        self.products = {'1. Coke': 150, '2. Pepsi': 130, '3. Snacks': 200, '4. Water': 100}
        self.coins1 = [5, 10, 20, 50, 100]

    def display(self):
        print("\n*** WELCOME TO THE VENDING MACHINE ***")

        print("\nMenu of Available products: ")
        for product, price in self.products.items():
            print("--------------------------------------")
            print(f"{product}: {price} cents")

    def purchase(self):
        while True:
            choice = input("\nEnter the name of the product you want: ")
            if choice in self.products:
                return choice
            else:
                print(" Invalid Input. Try again.")

    def insert_coins(self, product_price):
        total_price = 0
        while True:
            coin = int(input("\nInsert a coin (5, 10, 20, 50, 100 cents): "))
            if coin in self.coins1:
                total_price += coin
                if total_price >= product_price:
                    return total_price
                else:
                    remaining_amount = product_price - total_price
                    print(f"Remaining amount: {remaining_amount} cents")
            else:
                print("Invalid coin. Please try again.")

    def calculate_change(self, product_price, total_price):
        change = total_price - product_price
        return change

    def cal_no_coins(self, change):
        coins = [100, 50, 20, 10, 5]
        min_coins = {}
        for coin in coins:
            if change >= coin:
                count = change // coin
                change -= count * coin
                min_coins[coin] = count
        return min_coins

    def display_change(self, change, coins):
        print(f"Change amount: {change} cents")
        print("Coins to return:")
        for coin, count in coins.items():
            print(f"Collect your coins {count} of {coin} cents")


obj1 = VendingMachine()
obj1.display()
obj2 = obj1.purchase()
obj3 = obj1.products[obj2]
obj4 = obj1.insert_coins(obj3)
obj5 = obj1.calculate_change(obj3, obj4)
obj6 = obj1.cal_no_coins(obj5)
obj1.display_change(obj5, obj6)
