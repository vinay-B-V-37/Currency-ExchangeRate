import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class RealTimeCurrencyConverter():
    def __init__(self,url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD' :
            amount = amount / self.currencies[from_currency]

        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount

class App(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title('Vinay ExchangeRate')
        self.currency_converter = converter

        self.geometry('600x400')

        # Create a label for displaying the animated text
        self.intro_label = Label(self, text='Welcome to Real Time Currency Converter', fg='green', relief=tk.RAISED,
                                 borderwidth=3)
        self.intro_label.config(font=('Courier', 15, 'bold'))
        self.intro_label.pack()

        # Define the animation variables
        self.animation_text = "Welcome to Real Time Currency Converter"
        self.displaced_text = ""

        # Start the animation
        self.animate_text()

    def animate_text(self):
        # Update the displaced text by adding one letter at a time
        if len(self.animation_text) > 0:
            self.displaced_text += self.animation_text[0]
            self.animation_text = self.animation_text[1:]

        # Update the text label with the displaced text
        self.intro_label.config(text=self.displaced_text)

        # Check if there are more letters remaining in the animation text
        if len(self.animation_text) > 0:
            # Schedule the next animation after a delay (in milliseconds)
            self.after(100, self.animate_text)

        self.date_label = Label(self, text=f"1 Indian Rupee equals = {self.currency_converter.convert('INR','USD',1)} USD \n Date: {self.currency_converter.data['date']}", relief=tk.GROOVE, borderwidth=5)

        self.intro_label.place(x=10, y=5)
        self.date_label.place(x=160, y=50)

        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER, validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, text='', fg='black', bg='white', relief=tk.RIDGE, justify=tk.CENTER, width=20, borderwidth=4)

        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("INR")
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD")

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable, values=list(self.currency_converter.currencies.keys()), font=font, state='readonly', width=12, justify=tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable, values=list(self.currency_converter.currencies.keys()), font=font, state='readonly', width=12, justify=tk.CENTER)

        self.from_currency_dropdown.place(x=30, y=120)
        self.amount_field.place(x=36, y=150)
        self.to_currency_dropdown.place(x=340, y=120)
        self.converted_amount_field_label.place(x=346, y=150)

        self.convert_button = Button(self, text="Convert", fg="black", command=self.perform)
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.place(x=225, y=135)

        # Add Reset button
        self.reset_button = Button(self, text="Reset", fg="black", command=self.reset_fields)
        self.reset_button.config(font=('Courier', 10, 'bold'))
        self.reset_button.place(x=200,y=200)
        # Add Exit button
        self.exit_button = Button(self, text="Exit", fg="black", command=self.exit_app)
        self.exit_button.config(font=('Courier', 10, 'bold'))
        self.exit_button.place(x=250, y=200)

    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field_label.config(text=str(converted_amount))

    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))

    def reset_fields(self):
        self.amount_field.delete(0, 'end')
        self.converted_amount_field_label.config(text='')

    def exit_app(self):
        self.destroy()

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)

    App(converter)
    mainloop()
