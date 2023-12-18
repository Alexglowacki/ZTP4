from views.view import ProductView
# import tkinter as tk
from controllers.productController import ProductController

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def index():
    return render_template('index.html')


view_model = ProductController()
view = ProductView(app, view_model)

app.mainloop()
