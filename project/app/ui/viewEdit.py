import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from viewModel import Products

class ProductEditView:
    def __init__(self, root, viewModel, product_id):
        self.root = root
        self.viewModel = viewModel
        self.product_id = product_id

        self.root.title("Edit Product")

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

        self.button_add = ttk.Button(self.root, text="Save Changes", command=self.save_changes)
        self.button_add.grid(row=5, column=0, columnspan=2, pady=10)

        self.populate_fields()

    def populate_fields(self):
        self.viewModel.get(self.product_id, "True")
        details = self.viewModel.product
        if 'message' in details:
            tk.messagebox.showerror("Error", details['message'])
        else:
            self.entry_name.insert(0, details['name'])
            self.entry_amount.insert(0, details['amount'])
            self.entry_price.insert(0, details['price'])
            self.entry_description.insert(0, details['description'])
            self.entry_status.insert(0, details['status'])

    def save_changes(self):
        new_name = self.entry_name.get()
        new_amount = self.entry_amount.get()
        new_price = self.entry_price.get()
        new_description = self.entry_description.get()
        new_status = self.entry_status.get()

        update_doc = {"name": new_name,
                      "amount": new_amount,
                      "price": new_price,
                      "description": new_description,
                      "status": new_status}

        try:
            new_name = str(new_name)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid alphabetic name.")
            return

        try:
            new_amount = int(new_amount)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid numeric value for amount.")
            return

        try:
            new_price = float(new_price)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid numeric value for price.")
            return

        try:
            new_description = str(new_description)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid alphabetic description.")
            return

        try:
            new_status = str(new_status)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid alphabetic status.")
            return
        print(f"DEBUG: {self.product_id}")
        self.viewModel.put(self.product_id, update_doc)
        self.root.destroy()
