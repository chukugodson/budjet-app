class Budget:

      
    def __init__(self, name):
        self.name = name 
        self.balance = 0

    #methods 
    def deposit(self, amount):
        self.balance = amount

        return f"Your new balance is #{self.balance} in {self.name} budget"
    
    def withdraw(self, amount):
        if self.balance < amount:
            return "insufficient funds"
        else:
            self.balance = self.balance - amount

            feedback = "=====================\n"
            feedback += "Transaction was successful\n"
            feedback += f"your new balance is #{self.balance} in {self.name} budget"
            
            return feedback

    def get_balance(self):
        feedback = f"THe balance for {self.name} is #{self.balance}"

        return feedback

    def transfer(self, amount, category):
        if self.balance < amount:
            return "insufficient funds"
        else:
            self.balance = self.balance - amount
            category.balance += amount

            feedback = "=====================\n"
            feedback += "Transaction was successful\n"
            feedback += f"The balance for {self.name} is {self.balance}\n"     
            feedback += f"The balance for {category.name} is #{category.balance}\n"

            return feedback 



category_cloth = Budget("clothing")
category_food = Budget("food")
category_entertainment = Budget("entertainment")


category_cloth.deposit(4000)
category_food.deposit(5000)
category_entertainment.deposit(10000)


print(category_cloth.withdraw(2398))
print(category_food.withdraw(3455))
print(category_entertainment.withdraw(4000))

print("=========================")

print(category_cloth.get_balance())
print(category_food.get_balance())
print(category_entertainment .get_balance())


print("=========================")


print(category_cloth.transfer(700, category_food))
print(category_entertainment.transfer(1000, category_cloth))
print(category_entertainment.transfer(1000, category_food))
