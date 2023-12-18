import tkinter as tk
import requests

from bson import ObjectId
from tkinter import ttk
from viewModel import Products
from ui.viewDetails import ProductDetailsView
from ui.viewAdd import ProductAddView
from ui.viewEdit import ProductEditView


class ProductView:
    def __init__(self, root, viewModel):
        self.base = "http://127.0.0.1:5000/"
        self.root = root
        self.root.title("Product Management App")
        self.viewModel = viewModel

        self.tree = ttk.Treeview(self.root, columns=('', 'ID', 'Name', 'Price'))
        self.tree.heading('#0', text='')
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Name')
        self.tree.heading('#3', text='Price')
        self.tree.pack(padx=10, pady=10)

        self.list_products_button = ttk.Button(self.root,
                                             text='List Products',
                                             command=self.list_products)
        self.list_products_button.pack(padx=5, pady=3)

        self.add_product_button = ttk.Button(self.root,
                                             text='Add Product',
                                             command=self.add_product)
        self.add_product_button.pack(padx=5, pady=3)

        self.delete_product_button = ttk.Button(self.root,
                                             text='Delete Product',
                                             command=self.delete_product)
        self.delete_product_button.pack(padx=5, pady=3)

        # go to detailed product view
        self.get_details_button = ttk.Button(self.root,
                                             text='Product details',
                                             command=self.get_details)
        self.get_details_button.pack(padx=5, pady=3)

        # move to a different view -> editProduct view
        self.edit_product_button = ttk.Button(self.root,
                                              text='Edit product',
                                              command=self.edit_product)
        self.edit_product_button.pack(padx=5, pady=3)

        self.refresh_button = ttk.Button(self.root,
                                         text='Refresh',
                                         command=self.list_products)
        self.refresh_button.pack(padx=5, pady=3)

    def list_products(self):
        print("DEBUG: Listing products")
        self.viewModel.get("", "False")
        self.tree.delete(*self.tree.get_children())

        for product in self.viewModel.product_list:
            self.tree.insert(parent='', index='end', values=(product['_id'], product['name'], product['price']))

    def add_product(self):
        print("DEBUG: Adding product")

        add_view = ProductAddView(tk.Toplevel(), self.viewModel)


    def delete_product(self):
        print("DEBUG: Deleting product")

        selected_product = self.tree.selection()

        if selected_product:
            product_id = self.tree.item(selected_product)['values'][0]
            self.viewModel.delete(product_id)

        # After deletion refresh the list :)
        self.list_products()

    def edit_product(self):
        print("DEBUG: Opening EditProduct View")
        selected_product = self.tree.selection()

        if selected_product:
            product_id = self.tree.item(selected_product)['values'][0]
            edit_view = ProductEditView(tk.Toplevel(), self.viewModel, product_id)


    def get_details(self):
        print("DEBUG: Opening the GetDetails View")
        selected_product = self.tree.selection()

        if selected_product:
            product_id = self.tree.item(selected_product)['values'][0]
            details_view = ProductDetailsView(tk.Toplevel(), self.viewModel, product_id)

