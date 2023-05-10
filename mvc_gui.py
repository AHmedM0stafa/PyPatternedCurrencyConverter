from MVC import *
import tkinter as tk

class MoneyViewGUI:
    def __init__(self, model, master):
        self._model = model
        self._master = master
        self._frame = tk.Frame(master)

        # Create labels and entry widgets for amount and currency
        tk.Label(self._frame, text="Amount:").grid(row=0, column=0)
        self._amount_entry = tk.Entry(self._frame)
        self._amount_entry.grid(row=0, column=1)

        tk.Label(self._frame, text="Currency:").grid(row=1, column=0)
        self._currency_entry = tk.Entry(self._frame)
        self._currency_entry.grid(row=1, column=1)

        # Create a button to set the money values
        set_button = tk.Button(self._frame, text="Set", command=self._set_money)
        set_button.grid(row=2, column=1)

        # Create a label to display the current money values
        self._money_label = tk.Label(self._frame, text="")
        self._money_label.grid(row=3, column=1)

        # Create a dropdown menu to select the target currency for the money conversion
        tk.Label(self._frame, text="Convert to:").grid(row=4, column=0)
        self._to_currency_var = tk.StringVar()
        self._to_currency_var.set("EUR")
        to_currency_options = ["EUR", "GBP"]
        self._to_currency_menu = tk.OptionMenu(self._frame, self._to_currency_var, *to_currency_options)
        self._to_currency_menu.grid(row=4, column=1)

        # Create a button to change the money values to the target currency
        convert_button = tk.Button(self._frame, text="Convert", command=self._change_money)
        convert_button.grid(row=5, column=1)

        self._frame.pack()

    def _set_money(self):
        amount = float(self._amount_entry.get())
        currency = self._currency_entry.get()
        self._model.set_money(amount, currency)
        self._update_money_label()

    def _change_money(self):
        to_currency = self._to_currency_var.get()
        self._model.change_money(to_currency)
        self._update_money_label()

    def _update_money_label(self):
        money = self._model.get_money()
        self._money_label.config(text=f"{money.amount:.2f} {money.currency}")

if __name__ == "__main__":
    root = tk.Tk()
    model = MoneyModel()
    view = MoneyViewGUI(model, root)
    controller = MoneyController(model, view)
    root.mainloop()
