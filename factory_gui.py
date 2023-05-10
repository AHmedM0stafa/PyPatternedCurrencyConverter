# CurrencyConverterGUI

import tkinter as tk
from tkinter import ttk
# import factory.py
from factory import *

class CurrencyConverterGUI:
    # method initializes the GUI and creates the necessary widgets.
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")

        self.currencies = ["USD", "EUR", "GBP"]

        self.from_currency = tk.StringVar(value="USD")
        self.to_currency = tk.StringVar(value="EUR")
        self.amount = tk.StringVar()
        
        # instance of CurrencyConverter class that performs the currency conversion.
        self.converter = CurrencyConverter()

        # Create widgets
        amount_label = ttk.Label(master, text="Amount:")
        amount_entry = ttk.Entry(master, textvariable=self.amount)

        from_currency_label = ttk.Label(master, text="From Currency:")
        from_currency_combobox = ttk.Combobox(master, values=self.currencies, textvariable=self.from_currency)

        to_currency_label = ttk.Label(master, text="To Currency:")
        to_currency_combobox = ttk.Combobox(master, values=self.currencies, textvariable=self.to_currency)

        convert_button = ttk.Button(master, text="Convert", command=self.convert)

        self.result_label = ttk.Label(master, text="")

        # Grid layout
        amount_label.grid(row=0, column=0, padx=5, pady=5)
        amount_entry.grid(row=0, column=1, padx=5, pady=5)

        from_currency_label.grid(row=1, column=0, padx=5, pady=5)
        from_currency_combobox.grid(row=1, column=1, padx=5, pady=5)

        to_currency_label.grid(row=2, column=0, padx=5, pady=5)
        to_currency_combobox.grid(row=2, column=1, padx=5, pady=5)

        convert_button.grid(row=3, column=1, padx=5, pady=5)

        self.result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    
    # method takes the amount, from_currency, and to_currency as arguments, creates Money objects using MoneyFactory, calculates the exchange rate, performs the conversion, and returns the converted amount.
    def convert(self):
        amount = float(self.amount.get())
        from_currency = self.from_currency.get()
        to_currency = self.to_currency.get()

        result = self.converter.convert(amount, from_currency, to_currency)

        self.result_label.configure(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = CurrencyConverterGUI(root)
    root.mainloop()
