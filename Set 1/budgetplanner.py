class BudgetTracker:
    def __init__(self):
        self.transactions = []
        
    def add_transaction(self, date, category, amount, description):
        self.transactions.append({
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        })
        
    def get_balance(self):
        balance = 0
        for transaction in self.transactions:
            balance += transaction["amount"]
        return balance
    
    def get_category_sum(self, category):
        category_sum = 0
        for transaction in self.transactions:
            if transaction["category"] == category:
                category_sum += transaction["amount"]
        return category_sum
    
    def get_categories(self):
        categories = set()
        for transaction in self.transactions:
            categories.add(transaction["category"])
        return categories
    
    def generate_report(self):
        report = {}
        categories = self.get_categories()
        for category in categories:
            report[category] = self.get_category_sum(category)
        return report

# Example usage
bt = BudgetTracker()
bt.add_transaction("2022-01-01", "Income", 1000, "Salary")
bt.add_transaction("2022-01-05", "Expense", 100, "Groceries")
bt.add_transaction("2022-01-15", "Expense", 200, "Rent")
print("Balance: ", bt.get_balance())
print("Expense: ", bt.get_category_sum("Expense"))
print("Report: ", bt.generate_report())
