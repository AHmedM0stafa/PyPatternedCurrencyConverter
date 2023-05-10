from tkinter import *

from strategy import *


class MoneyConverterGUI1:
    def __init__(self, root):
        self.root = root
        self.root.title("Money Converter (ComplexExchangeRate)")

        # Create the GUI elements
        Label(self.root, text="Amount:").grid(row=0, column=0)
        self.amount_entry = Entry(self.root)
        self.amount_entry.grid(row=0, column=1)

        Label(self.root, text="Currency:").grid(row=1, column=0)
        self.currency_entry = Entry(self.root)
        self.currency_entry.grid(row=1, column=1)

        Label(self.root, text="Convert to:").grid(row=2, column=0)
        self.to_currency_entry = Entry(self.root)
        self.to_currency_entry.grid(row=2, column=1)

        self.result_label = Label(self.root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2)

        self.convert_button = Button(self.root, text="Convert", command=self.convert_2)
        self.convert_button.grid(row=4, column=0, columnspan=2)



        complex_exchange_rate = ComplexExchangeRate('USD', {
            'EUR': 0.85,
            'GBP': 1.25
        })


        money_changer = MoneyChanger(complex_exchange_rate)

        self.money_converter = MoneyConverter(money_changer)
    def convert_2(self):
        # Get the user input
        amount = float(self.amount_entry.get())
        currency = self.currency_entry.get()
        to_currency = self.to_currency_entry.get()

        # Create the Money object
        money = Money(amount, currency)

        # Convert the money using the MoneyConverter object
        new_money = self.money_converter.change_money(money, to_currency)

        # Display the result
        self.result_label.config(
            text=f"{money.amount} {money.currency} is equivalent to {new_money.amount} {new_money.currency}")



class MoneyConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Money Converter(SimpleExchangeRate)")

        # Create the GUI elements
        Label(self.root, text="Amount:").grid(row=0, column=0)
        self.amount_entry = Entry(self.root)
        self.amount_entry.grid(row=0, column=1)

        Label(self.root, text="Currency:").grid(row=1, column=0)
        self.currency_entry = Entry(self.root)
        self.currency_entry.grid(row=1, column=1)

        Label(self.root, text="Convert to:").grid(row=2, column=0)
        self.to_currency_entry = Entry(self.root)
        self.to_currency_entry.grid(row=2, column=1)

        self.result_label = Label(self.root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2)

        self.convert_button = Button(self.root, text="Convert", command=self.convert)
        self.convert_button.grid(row=4, column=0, columnspan=2)

        # Create the MoneyConverter object with the SimpleExchangeRate strategy
        simple_exchange_rate = SimpleExchangeRate({
            'USD': {'EUR': 0.85, 'GBP': 0.75},
            'EUR': {'USD': 1.18, 'GBP': 0.88},
            'GBP': {'USD': 1.34, 'EUR': 1.14}
        })




        money_changer = MoneyChanger(simple_exchange_rate)
        self.money_converter = MoneyConverter(money_changer)


    def convert(self):
        # Get the user input
        amount = float(self.amount_entry.get())
        currency = self.currency_entry.get()
        to_currency = self.to_currency_entry.get()

        # Create the Money object
        money = Money(amount, currency)

        # Convert the money using the MoneyConverter object
        new_money = self.money_converter.change_money(money, to_currency)

        # Display the result
        self.result_label.config(
            text=f"{money.amount} {money.currency} is equivalent to {new_money.amount} {new_money.currency}")







# Create the Tkinter GUI
root = Tk()
root1 = Tk()
app = MoneyConverterGUI(root)
app2 = MoneyConverterGUI1(root1)
root.mainloop()
root1.mainloop()
