# Observable class represents the object that is observed by the observers.

# It maintains a list of observers and provides methods for adding, removing,
# and notifying observers.
class Observable:
    def __init__(self):
        self.observers = []

    # Method for adding an observer to the list
    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
    
    # Method for removing an observer from the list
    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    # Method for notifying all observers when the observed object changes
    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            # Call the update method of each observer, passing the observed object,
            # and any additional arguments and keyword arguments
            observer.update(self, *args, **kwargs)

# Money class represents a currency amount with its currency type .
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

# MoneyChanger class is a concrete observer. It observes changes in the observed object
# and performs some actions when notified of these changes.
class MoneyChanger(Observable):
    def __init__(self):
        super().__init__()
        self._exchange_rates = {
            "USD": {"EUR": 0.82, "GBP": 0.72},
            "EUR": {"USD": 1.22, "GBP": 0.87},
            "GBP": {"USD": 1.39, "EUR": 1.14}
        }

    # Method for getting the exchange rate from one currency to another
    def get_exchange_rate(self, from_currency, to_currency):
        return self._exchange_rates[from_currency][to_currency]

    # Method for changing a money object from one currency to another
    def change_money(self, money, to_currency):
        from_currency = money.currency
        # Get the exchange rate from the from_currency to the to_currency
        rate = self.get_exchange_rate(from_currency, to_currency)
        # Calculate the new amount in the to_currency
        new_amount = money.amount * rate
        # Create a new Money object with the new amount and the to_currency
        new_money = Money(new_amount, to_currency)
        # Notify observers of the change with the original and new money objects
        self.notify_observers(money, new_money)
        return new_money

# Logger class is a concrete observer that prints a log message when notified of changes
class Logger:
    def update(self, observable, *args, **kwargs):
        money, new_money = args
        print(f"{money.amount} {money.currency} was changed to {new_money.amount} {new_money.currency}")



# Example usage:
# Create a MoneyChanger object and a Logger object
money_changer = MoneyChanger()
logger = Logger()

# Add the Logger object as an observer of the MoneyChanger object
money_changer.add_observer(logger)

# Create a Money object with 200 EUR
money = Money(200, "EUR")
# Convert the money object to USD using the MoneyChanger object
new_money = money_changer.change_money(money, "USD")










