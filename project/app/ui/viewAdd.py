
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from viewModel import Products

class ProductAddView:
    def __init__(self, root, viewModel):
        self.root = root
        self.viewModel = viewModel

        self.root.title("Add Product")

        self.label_name = ttk.Label(self.root, text="Product Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_name = ttk.Entry(self.root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.label_amount = ttk.Label(self.root, text="Product Amount:")
        self.label_amount.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_amount = ttk.Entry(self.root)
        self.entry_amount.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.label_price = ttk.Label(self.root, text="Product Price:")
        self.label_price.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_price = ttk.Entry(self.root)
        self.entry_price.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.label_description = ttk.Label(self.root, text="Product Description:")
        self.label_description.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_description = ttk.Entry(self.root)
        self.entry_description.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        self.label_status = ttk.Label(self.root, text="Product Status:")
        self.label_status.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_status = ttk.Entry(self.root)
        self.entry_status.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)

        self.button_add = ttk.Button(self.root, text="Add Product", command=self.add_product)
        self.button_add.grid(row=5, column=0, columnspan=2, pady=10)

    def add_product(self):
        name = self.entry_name.get()
        amount = self.entry_amount.get()
        price = self.entry_price.get()
        description = self.entry_description.get()
        status = self.entry_status.get()

        if not name or not price or not amount or not description or not status:
            tk.messagebox.showerror("Error", "Please enter values fields.")
            return

        try:
            name = str(name)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid alphabetic name.")
            return

        try:
            amount = int(amount)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid numeric value for amount.")
            return

        try:
            price = float(price)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid numeric value for price.")
            return

        try:
            description = str(description)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid alphabetic description.")
            return

        try:
            status = str(status)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid alphabetic status.")
            return

        self.viewModel.post(name, amount, price, description, status)
        self.root.destroy()
