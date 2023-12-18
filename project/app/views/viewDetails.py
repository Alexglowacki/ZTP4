import tkinter as tk
from tkinter import ttk
from controllers.productController import ProductController


class ProductDetailsView:
    def __init__(self, root, controller, product_id):
        self.root = root
        self.controller = controller
        self.product_id = product_id

        self.root.title("Product Details")
        self.root.geometry("300x250")

        self.label_id = ttk.Label(self.root, text="Product ID:")
        self.label_id.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.label_name = ttk.Label(self.root, text="Product Name:")
        self.label_name.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.label_amount = ttk.Label(self.root, text="Product Amount:")
        self.label_amount.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.label_price = ttk.Label(self.root, text="Product Price:")
        self.label_price.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        self.label_description = ttk.Label(self.root, text="Product Description:")
        self.label_description.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

        self.label_status = ttk.Label(self.root, text="Product Status:")
        self.label_status.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

        self.button_close = ttk.Button(self.root, text="Close", command=self.root.destroy)
        self.button_close.grid(row=6, column=0, pady=10)

        self.populate_details()

    def populate_details(self):
        self.controller.get(self.product_id, 'True')
        details = self.controller.product
        if 'message' in details:
            tk.messagebox.showerror("Error", details['message'])
        else:
            self.label_id.config(text=f"Product ID: {details['_id']}")
            self.label_name.config(text=f"Product Name: {details['name']}")
            self.label_amount.config(text=f"Product Amount: {details['amount']}")
            self.label_price.config(text=f"Product Price: {details['price']}")
            self.label_description.config(text=f"Product Description: {details['description']}")
            self.label_status.config(text=f"Product Status: {details['status']}")
