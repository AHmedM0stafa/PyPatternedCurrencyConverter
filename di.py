#In the Dependency Injection pattern,
# the exchange rate strategy is passed to the MoneyChanger class as a constructor argument,
# which makes the MoneyChanger class more flexible and allows us to easily
# swap different exchange rate strategies at runtime.


# ExchangeRate class represents a general exchange rate, it has a method that should be implemented by its subclasses.

class ExchangeRate:
    def get_rate(self, from_currency, to_currency):
        pass
# SimpleExchangeRate represents a simple exchange rate, where rates are defined as a dictionary.
class SimpleExchangeRate(ExchangeRate):
    def __init__(self, rates):
        self._rates = rates
    # This method calculates the exchange rate between two currencies based on a predefined dictionary of rates.
    def get_rate(self, from_currency, to_currency):
        return self._rates[from_currency][to_currency]
# ComplexExchangeRate represents a more complex exchange rate, where rates are defined with respect to a base currency.
class ComplexExchangeRate(ExchangeRate):
    def __init__(self, base_currency, rates):
        self._base_currency = base_currency
        self._rates = rates
    # This method calculates the exchange rate between two currencies based on the predefined rates with respect to a base currency.
    def get_rate(self, from_currency, to_currency):
        if from_currency == to_currency:
            return 1.0
        elif from_currency == self._base_currency:
            return self._rates[to_currency]
        elif to_currency == self._base_currency:
            return 1 / self._rates[from_currency]
        else:
            return self._rates[to_currency] / self._rates[from_currency]

# Money class represents a monetary amount with a currency.
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
# MoneyChanger class is responsible for changing money from one currency to another, it uses a strategy to calculate the exchange rate.
class MoneyChanger:
    def __init__(self, exchange_rate_strategy):
        self._exchange_rate_strategy = exchange_rate_strategy
    # This method changes the currency of the given money to the specified currency using the exchange rate strategy.

    def change_money(self, money, to_currency):
        from_currency = money.currency
        rate = self._exchange_rate_strategy.get_rate(from_currency, to_currency)
        new_amount = money.amount * rate
        new_money = Money(new_amount, to_currency)
        return new_money

# MoneyConverter class is responsible for converting money from one currency to another using a MoneyChanger object.
class MoneyConverter:
    def __init__(self, money_changer):
        self._money_changer = money_changer
    # This method changes the currency of the given money to the specified currency using the MoneyChanger object.
    def change_money(self,
                     money, to_currency):
        return self._money_changer.change_money(money, to_currency)


# Create a SimpleExchangeRate object with predefined rates.
simple_exchange_rate = SimpleExchangeRate({
    'USD': {'EUR': 0.85, 'GBP': 0.75},
    'EUR': {'USD': 1.18, 'GBP': 0.88},
    'GBP': {'USD': 1.34, 'EUR': 1.14}
})

# Create a ComplexExchangeRate object with predefined rates with respect to a base currency.
complex_exchange_rate = ComplexExchangeRate('USD', {
    'EUR': 0.85,
    'GBP': 1.25
})

# Create a MoneyChanger object using the ComplexExchangeRate object as a strategy.
money_changer = MoneyChanger(complex_exchange_rate)
# Create a MoneyConverter object using the MoneyChanger object.
money_converter = MoneyConverter(money_changer)


# Using the MoneyConverter to convert money
# Create a Money object with a given amount and currency.
money = Money(15, 'EUR')
new_money = money_converter.change_money(money, 'USD')
print(f'{money.amount} {money.currency} is equivalent to {new_money.amount} {new_money.currency}')
