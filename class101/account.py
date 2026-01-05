class Bank:
    def __init__(self, name):
        self.net_amount = 0
        self.name = name
        
    def deposit(self, amount):
        self.net_amount += amount

    def withdraw(self, amount):
        if amount > self.net_amount:
            print("Not enough balance")
            return
        else:
            self.net_amount -= amount

    def balance(self):
        print(f"{self.name} has a balance of ${self.net_amount}")


b1 = Bank("Marcus")
b1.deposit(100)
b1.withdraw(21)
b1.balance()


