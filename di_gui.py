import tkinter as tk

from di import *

class MoneyConverterGUI:
    def __init__(self, root, money_converter):
        self.root = root
        self.money_converter = money_converter

        # Create UI elements
        self.from_currency_label = tk.Label(root, text="From Currency:")
        self.from_currency_entry = tk.Entry(root)
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_entry = tk.Entry(root)
        self.to_currency_label = tk.Label(root, text="To Currency:")
        self.to_currency_entry = tk.Entry(root)
        self.convert_button = tk.Button(root, text="Convert", command=self.convert_money)
        self.result_label = tk.Label(root, text="Result:")
        self.result_entry = tk.Entry(root, state="readonly")

        # Layout UI elements using grid
        self.from_currency_label.grid(row=0, column=0)
        self.from_currency_entry.grid(row=0, column=1)
        self.amount_label.grid(row=1, column=0)
        self.amount_entry.grid(row=1, column=1)
        self.to_currency_label.grid(row=2, column=0)
        self.to_currency_entry.grid(row=2, column=1)
        self.convert_button.grid(row=3, column=1)
        self.result_label.grid(row=4, column=0)
        self.result_entry.grid(row=4, column=1)

    def convert_money(self):
        # Get input values from UI elements
        from_currency = self.from_currency_entry.get()
        amount = float(self.amount_entry.get())
        to_currency = self.to_currency_entry.get()

        # Convert money using MoneyConverter class
        money = Money(amount, from_currency)
        new_money = self.money_converter.change_money(money, to_currency)

        # Display result in UI element
        self.result_entry.config(state="normal")
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, f"{new_money.amount} {new_money.currency}")
        self.result_entry.config(state="readonly")


# Create objects using dependency injection
simple_exchange_rate = SimpleExchangeRate({
    'USD': {'EUR': 0.85, 'GBP': 0.75},
    'EUR': {'USD': 1.18, 'GBP': 0.88},
    'GBP': {'USD': 1.34, 'EUR': 1.14}
})

complex_exchange_rate = ComplexExchangeRate('USD', {
    'EUR': 0.85,
    'GBP': 1.25
})

money_changer = MoneyChanger(complex_exchange_rate)
money_converter = MoneyConverter(money_changer)

# Create Tkinter app
root = tk.Tk()
app = MoneyConverterGUI(root, money_converter)
root.mainloop()
