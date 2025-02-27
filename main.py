class BankAccount:
    def __init__(self, name, balance, id_):
        self.name = name
        self.balance = balance
        self.id_ = id_
        
    def deposit(self, amount):
        if amount < 0:
            print("amount must be more than 0")
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance < amount:
            print("YOu don't have enough money on balance")
        self.balance -= amount
        
    def check_balance(self):
        print(self.balance)
        

account = BankAccount("Nodo", 100, 00000)
account.deposit(300)
account.withdraw(200)
account.check_balance()