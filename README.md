# Banking-System

This simple Python project simulates a basic banking system. It consists of two classes: `User` and `Bank`. The `User` class stores personal details such as name, age, and gender, while the `Bank` class, inheriting from `User`, manages a user's bank account operations.

## Features

### User Class

#### Initialization
- `__init__(self, name, age, gender)`: Initializes a user with the provided name, age, and gender.

#### Personal Details
- `show_details(self)`: Displays the user's personal details, including name, age, and gender.

### Bank Class

#### Initialization
- `__init__(self, name, age, gender)`: Initializes a bank account associated with a user, setting the initial balance to 0.

#### Transactions
- `deposit(self, amount)`: Deposits a specified amount into the account, updating the balance and providing a success message.
- `withdraw(self, amount)`: Withdraws a specified amount from the account if sufficient funds are available, updating the balance and providing a success or insufficient funds message.
- `view_balance(self)`: Displays the current balance of the account.

## Object-Oriented Programming (OOP) Principles

### Encapsulation

The classes `User` and `Bank` encapsulate related attributes and methods. Internal details are hidden from the outside world, and access to data is controlled through methods. For example, the `User` class encapsulates personal details and provides a method `show_details` to reveal this information.

### Inheritance

The `Bank` class inherits from the `User` class, promoting code reuse and a logical organization of functionality. This reduces redundancy in the code, as the `Bank` class inherits the `__init__` method from the `User` class.

### Polymorphism

Polymorphism is evident in the use of the `deposit` and `withdraw` methods. These methods can behave differently based on the context (balance sufficiency) during runtime. For instance, the `withdraw` method in the `Bank` class behaves differently depending on whether there are sufficient funds, demonstrating polymorphic behavior.

### Abstraction

Abstraction is achieved by defining the classes `User` and `Bank` with relevant attributes and methods, hiding the complexity of their implementations. Users interacting with these classes don't need to know the internal workings; they interact through well-defined interfaces.

### Composition

The `Bank` class uses composition to include a `User` object as an attribute. This allows the `Bank` class to leverage the functionality of the `User` class without being tightly coupled to it. The `Bank` class includes a `User` object as a part of its state, demonstrating composition for building complex objects.

By applying these OOP principles, the code becomes more modular, maintainable, and flexible. It promotes code organization, reusability, and abstraction of complex systems into manageable components.

## Usage

1. Create a `User` instance with the desired personal details.
2. Create a `Bank` instance associated with the user, initializing the bank account.
3. Perform transactions using the `deposit` and `withdraw` methods.
4. Check the account balance using the `view_balance` method.

## Example

```python
def main():
    # Create a user
    user = User('Youssef', 21, 'Male')

    # Create a bank account associated with the user
    bank = Bank(user.name, user.age, user.gender)

    # Deposit and withdraw from the account
    bank.deposit(500)
    bank.withdraw(100)

    # View the current account balance
    bank.view_balance()

if __name__ == "__main__":
    main()
