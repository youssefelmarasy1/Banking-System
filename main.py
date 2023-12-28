class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_details(self):
        print('Personal Details:')
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount

    def withdraw(self, amount):
        self.amount = amount
        if self.balance >= self.amount:
            self.balance = self.balance - self.amount
        else:
            print("Insufficient Funds")

    def show_balance(self):
        print(f"Balance: {self.balance}")

def main():
    user = User('Youssef', 21, 'Male')
    #user.show_details()
    #print(user.gender)
    bank = Bank(user.name, user.age, user.gender)
    bank.deposit(500)
    bank.withdraw(100)
    bank.show_balance()
    
if __name__ == "__main__":
    main()
        