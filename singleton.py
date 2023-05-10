# Singleton design pattern implementation to create a single instance of a class

class Singleton:
    _instance = None

    def __new__(cls):
        # Check if an instance already exists
        if not cls._instance:
            # If not, create a new instance of the class
            cls._instance = super().__new__(cls)
        # Return the instance
        return cls._instance

# This class represents a unit of money with its amount and currency.
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

# This class represents a MoneyChanger that uses exchange rates to change a given money object to a new currency.
class MoneyChanger(Singleton):
    def __init__(self):
        self._exchange_rates = {
            "USD": {"EUR": 0.82, "GBP": 0.72},
            "EUR": {"USD": 1.22, "GBP": 0.87},
            "GBP": {"USD": 1.39, "EUR": 1.14}
        }
    
    # This method returns the exchange rate for the given currencies.
    def get_exchange_rate(self, from_currency, to_currency):
        # Get exchange rate between two currencies
        return self._exchange_rates[from_currency][to_currency]

    # This method changes the given money object to a new currency and returns a new money object.
    def change_money(self, money, to_currency):
        # Convert Money object to new currency
        from_currency = money.currency
        rate = self.get_exchange_rate(from_currency, to_currency)
        new_amount = money.amount * rate
        new_money = Money(new_amount, to_currency)
        # Return the new Money object in the new currency
        return new_money

# Create a new MoneyChanger object
money_changer1 = MoneyChanger()

# Create a new Money object with amount 100 and currency USD
money1 = Money(100, "USD")
# Convert the Money object to EUR currency
new_money1 = money_changer1.change_money(money1, "EUR")


# Print the converted amount and currency
print(money1.amount,money1.currency,"is equivalent to",new_money1.amount, new_money1.currency)  # 82.0 EUR


