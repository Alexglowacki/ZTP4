from views.view import ProductView
# import tkinter as tk
from controllers.productController import ProductController

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def index():
    return render_template('index.html')

controller = ProductController()
# view = ProductView(app, controller)

if __name__ == '__main__':
    app.run(debug=True)