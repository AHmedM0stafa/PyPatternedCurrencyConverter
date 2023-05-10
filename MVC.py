# This code implements the Model-View-Controller (MVC) design pattern to convert money from one currency to another.

class Money:
    # The Money class represents the amount and currency of money.
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

class MoneyChanger:
    # The MoneyChanger class holds the exchange rates for different currencies.
    def __init__(self):
        self._exchange_rates = {
            "USD": {"EUR": 0.82, "GBP": 0.72},
            "EUR": {"USD": 1.22, "GBP": 0.87},
            "GBP": {"USD": 1.39, "EUR": 1.14}
        }

    # Returns the exchange rate for converting from_currency to to_currency.
    def get_exchange_rate(self, from_currency, to_currency):
        return self._exchange_rates[from_currency][to_currency]

    # Converts the given money object to the given to_currency and returns the new money object.
    def change_money(self, money, to_currency):
        from_currency = money.currency
        rate = self.get_exchange_rate(from_currency, to_currency)
        new_amount = money.amount * rate
        new_money = Money(new_amount, to_currency)
        return new_money

class MoneyModel:
    # The MoneyModel class represents the data of the application, which is the money object.
    def __init__(self):
        self._money = Money(0, "USD")
        self._money_changer = MoneyChanger()

    # Returns the money object.
    def get_money(self):
        return self._money

    # Sets the money object to the given amount and currency.
    def set_money(self, amount, currency):
        self._money.amount = amount
        self._money.currency = currency

    # Converts the money object to the given to_currency using the MoneyChanger object.
    def change_money(self, to_currency):
        self._money = self._money_changer.change_money(self._money, to_currency)

class MoneyView:
    # The MoneyView class represents the presentation of the application, which is the console output.
    def __init__(self, model):
        self._model = model

    # Displays the amount and currency of the money object in the console.
    def display(self):
        money = self._model.get_money()
        print(f"{money.amount:.2f} {money.currency}")

class MoneyController:
    # The MoneyController class controls the flow of the application.
    def __init__(self, model, view):
        self._model = model
        self._view = view

    # Sets the money object to the given amount and currency.
    def set_money(self, amount, currency):
        self._model.set_money(amount, currency)
    
    # Converts the money object to the given to_currency and displays the new amount and currency in the console.
    def change_money(self, to_currency):
        self._model.change_money(to_currency)
        self._view.display()

# Create the model, view, and controller objects.
model = MoneyModel()
view = MoneyView(model)
controller = MoneyController(model, view)

# Set the initial amount and currency of the money object.
controller.set_money(100, "USD")

# Convert the money object to EUR and display the new amount and currency.
controller.change_money("EUR")  # Outputs: 82.00 EUR
