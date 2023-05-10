import tkinter as tk
from tkinter import ttk
from singleton import *



class MoneyConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Money Converter")

        self.money_changer = MoneyChanger()

        # create input fields for amount and currency
        self.amount_label = ttk.Label(master, text="Amount:")
        self.amount_label.grid(row=0, column=0, padx=5, pady=5)
        self.amount_entry = ttk.Entry(master, width=10)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        self.currency_label = ttk.Label(master, text="Currency:")
        self.currency_label.grid(row=1, column=0, padx=5, pady=5)
        self.currency_entry = ttk.Entry(master, width=10)
        self.currency_entry.grid(row=1, column=1, padx=5, pady=5)

        # create dropdown menu for target currency
        self.to_currency_label = ttk.Label(master, text="Convert to:")
        self.to_currency_label.grid(row=2, column=0, padx=5, pady=5)
        self.to_currency_var = tk.StringVar(value="USD")
        self.to_currency_dropdown = ttk.OptionMenu(master, self.to_currency_var, "USD", "EUR", "GBP")
        self.to_currency_dropdown.grid(row=2, column=1, padx=5, pady=5)

        # create button for conversion
        self.convert_button = ttk.Button(master, text="Convert", command=self.convert_money)
        self.convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # create label to display result
        self.result_label = ttk.Label(master, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def convert_money(self):
        try:
            amount = float(self.amount_entry.get())
            currency = self.currency_entry.get().upper()
            to_currency = self.to_currency_var.get().upper()

            money = Money(amount, currency)
            new_money = self.money_changer.change_money(money, to_currency)

            self.result_label.config(text=f"{money.amount:.2f} {money.currency} = {new_money.amount:.2f} {new_money.currency}")
        except ValueError:
            self.result_label.config(text="Invalid input.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MoneyConverterApp(root)
    root.mainloop()
