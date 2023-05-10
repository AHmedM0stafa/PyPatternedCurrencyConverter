import tkinter as tk
from observer import *


class MoneyChangerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Money Changer")

        # Input fields
        self.amount_var = tk.StringVar()
        self.currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.amount_entry = tk.Entry(self.window, textvariable=self.amount_var)
        self.currency_entry = tk.Entry(self.window, textvariable=self.currency_var)
        self.to_currency_entry = tk.Entry(self.window, textvariable=self.to_currency_var)
        self.amount_label = tk.Label(self.window, text="Amount:")
        self.currency_label = tk.Label(self.window, text="Currency:")
        self.to_currency_label = tk.Label(self.window, text="To Currency:")

        # Output field
        self.output_var = tk.StringVar()
        self.output_label = tk.Label(self.window, textvariable=self.output_var)

        # Buttons
        self.convert_button = tk.Button(self.window, text="Convert", command=self.convert)
        self.clear_button = tk.Button(self.window, text="Clear", command=self.clear)

        # Layout
        self.amount_label.grid(row=0, column=0)
        self.amount_entry.grid(row=0, column=1)
        self.currency_label.grid(row=1, column=0)
        self.currency_entry.grid(row=1, column=1)
        self.to_currency_label.grid(row=2, column=0)
        self.to_currency_entry.grid(row=2, column=1)
        self.convert_button.grid(row=3, column=0)
        self.clear_button.grid(row=3, column=1)
        self.output_label.grid(row=4, columnspan=2)

        # Money changer object and logger object
        self.money_changer = MoneyChanger()
        self.logger = Logger()
        self.money_changer.add_observer(self.logger)

    def convert(self):
        amount = float(self.amount_var.get())
        currency = self.currency_var.get().upper()
        to_currency = self.to_currency_var.get().upper()
        money = Money(amount, currency)
        new_money = self.money_changer.change_money(money, to_currency)
        self.output_var.set(f"{amount} {currency} was changed to {new_money.amount} {new_money.currency}")

    def clear(self):
        self.amount_var.set("")
        self.currency_var.set("")
        self.to_currency_var.set("")
        self.output_var.set("")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = MoneyChangerGUI()
    gui.run()
