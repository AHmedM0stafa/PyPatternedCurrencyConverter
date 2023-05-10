import tkinter as tk
from locale import currency
from factory import *
from MVC import *
from di import *
from observer import *
from strategy import *
from singleton import *


class MoneyController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.converter = CurrencyConverter()
        self.view.register_observer(self)

    def update(self):
        amount = self.view.get_amount()
        from_currency = self.view.get_from_currency()
        to_currency = self.view.get_to_currency()
        converted_amount = self.converter.convert(amount, from_currency, to_currency)
        self.view.set_converted_amount(converted_amount)


class MoneyView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.controller = None
        self.observers = []

        self.from_currency_var = tk.StringVar(self)
        self.to_currency_var = tk.StringVar(self)
        self.amount_var = tk.StringVar(self)
        self.converted_amount_var = tk.StringVar(self)

        self.from_currency_var.set("USD")
        self.to_currency_var.set("EUR")
        # GBP Great British Pound
        self.from_currency_choices = ["USD", "EUR", "GBP "]
        self.to_currency_choices = ["USD", "EUR", "GBP"]

        self.from_currency_menu = tk.OptionMenu(self, self.from_currency_var, *self.from_currency_choices)
        self.to_currency_menu = tk.OptionMenu(self, self.to_currency_var, *self.to_currency_choices)
        self.amount_entry = tk.Entry(self, textvariable=self.amount_var)
        self.converted_amount_label = tk.Label(self, textvariable=self.converted_amount_var)
        self.convert_button = tk.Button(self, text="Convert", command=self.convert)

        self.from_currency_menu.pack(side=tk.LEFT)
        self.amount_entry.pack(side=tk.LEFT)
        self.to_currency_menu.pack(side=tk.LEFT)
        self.convert_button.pack(side=tk.LEFT)
        self.converted_amount_label.pack(side=tk.LEFT)

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def get_from_currency(self):
        return self.from_currency_var.get()

    def get_to_currency(self):
        return self.to_currency_var.get()

    def get_amount(self):
        return float(self.amount_var.get())

    def set_converted_amount(self, converted_amount):
        self.converted_amount_var.set(f"{converted_amount:.2f}")

    def convert(self):
        self.notify_observers()

class Application(tk.Tk):
    def __init__(self,amount,currency):
        super().__init__()
        self.title("Currency Converter")
        self.model = Money(amount,currency)
        self.view = MoneyView(self)
        self.controller = MoneyController(self.model, self.view)
        self.view.pack()

if __name__ == "__main__":
    app = Application(amount,currency)
    app.mainloop()
