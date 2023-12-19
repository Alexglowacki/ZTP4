from views.view import ProductView
from controllers.productController import ProductController
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

controller = ProductController()


@app.route('/')
def index():
    controller.get("", get_one="False")
    return render_template('index.html', products=controller.product_list)


@app.route('/list')
def list():
    controller.get("", get_one="False")
    return render_template('list.html', products=controller.product_list)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/details')
def details():
    return render_template('details.html')


@app.route('/delete/<string:id>')
def delete(id):
    ProductController.delete(id)
# view = ProductView(app, controller)

if __name__ == '__main__':
    app.run(debug=True)
