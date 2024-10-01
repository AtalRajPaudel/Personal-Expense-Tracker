class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        return f"{self.date} - {self.category}: $self.amount"