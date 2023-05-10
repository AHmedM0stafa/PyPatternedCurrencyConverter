# Define a base class for Money
class Money:
    def __init__(self, amount):
        self.amount = amount

# Define classes for different types of Money, each with its own currency
class USDMoney(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self.currency = "USD"

class EURMoney(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self.currency = "EUR"

class GBPMoney(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self.currency = "GBP"

# Define a factory class for creating different types of Money objects
class MoneyFactory:
    # Define a static method for creating a Money object based on currency
    @staticmethod
    def create_money(currency, amount):
        # Create a Money object based on the specified currency
        if currency == "USD":
            return USDMoney(amount)
        elif currency == "EUR":
            return EURMoney(amount)
        elif currency == "GBP":
            return GBPMoney(amount)
        else:
            raise Exception("Invalid currency")

# Define a class for performing currency conversion using the Factory pattern
class CurrencyConverter:
    # Define a dictionary of exchange rates for different currency conversions
    def __init__(self):
        self.exchange_rates = {
            "USD": {"USD": 1, "EUR": 0.82, "GBP": 0.72},
            "EUR": {"USD": 1.22, "EUR": 1, "GBP": 0.87},
            "GBP": {"USD": 1.39, "EUR": 1.14, "GBP": 1}
        }
    # Define a method for converting an amount from one currency to another
    def convert(self, amount, from_currency, to_currency):
        # Use the MoneyFactory to create Money objects for the specified currencies
        from_money = MoneyFactory.create_money(from_currency, amount)
        to_money = MoneyFactory.create_money(to_currency, 0)
        
        # Look up the exchange rate for the specified currencies
        rate = self.exchange_rates[from_money.currency][to_money.currency]
        
        # Convert the amount using the exchange rate
        converted_amount = rate * from_money.amount
        
        # Update the amount of the destination Money object
        to_money.amount = converted_amount
        
        # Return the converted amount
        return to_money.amount


# Create an instance of CurrencyConverter class
converter = CurrencyConverter()

# Convert $100 to EUR
amount = 100
from_currency = "USD"
to_currency = "EUR"

# Convert the amount using the CurrencyConverter
converted_amount = converter.convert(amount, from_currency, to_currency)

# Output the converted amount
print(f"{amount} {from_currency} is equivalent to {converted_amount} {to_currency}")
