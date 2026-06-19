budget = {}

class Category:
    def __init__(self, name):
        
        self.name = name
        self.ledger = []
    
    def check_funds(self, amount):
        total = 0
        for amt in self.ledger: 
            total += amt["amount"]
        return amount <= total

    def deposit(self, amount, description = ""):
        new_item = {'amount': amount, 'description': description}
        self.ledger.append(new_item)
    
    def withdraw (self, amount, description = ""):
        if self.check_funds(amount):
            amount = -1 * amount
            new_item = {'amount': amount, 'description': description}
            self.ledger.append(new_item)
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        for amt in self.ledger:
            #if amt["description"] == self.name:
            total += amt["amount"]
        return total
   
    def transfer(self, amount, dest): 
        #self.name = dest
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {dest.name}")
            dest.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def __str__(self):
        title = self.name.center(30, "*") + "\n"

        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:7.2f}\n"

        total = f"Total: {self.get_balance()}"

        return title + items + total

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"

    withdrawals = []

    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += -item["amount"]

        withdrawals.append(spent)

    total_spent = sum(withdrawals)

    percentages = [
        int((spent / total_spent) * 100 // 10) * 10
        for spent in withdrawals
    ]

    # bars
    for level in range(100, -1, -10):
        chart += f"{level:>3}| "

        for p in percentages:
            if p >= level:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    # horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1)
    chart += "\n"

    # labels
    max_len = max(len(cat.name) for cat in categories)

    for i in range(max_len):
        chart += "     "

        for cat in categories:
            if i < len(cat.name):
                chart += cat.name[i] + "  "
            else:
                chart += "   "

        chart += "\n"

    return chart.rstrip("\n")

    


name="Food"

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

print(create_spend_chart([food, clothing]))
