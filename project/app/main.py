from views.view import ProductView
from controllers.productController import ProductController
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

controller = ProductController()


@app.route('/')
def index():
    controller.get("", get_one="False")
    return render_template('index.html', products=controller.product_list)


@app.route('/product/<string:name>/<int:amount>/<float:price>/<string:description>/<string:status>', methods=['POST'])
def add(name, amount, price, description, status):

    print(f"DEBUG: {name}\n{amount}\n{price}\n{description}\n{status}")
    addition = controller.post(name=name,
                               amount=amount,
                               price=price,
                               description=description,
                               status=status)

    return index()


@app.route('/edit/<string:id>')
def edit(id):
    controller.get(id, get_one="True")
    return render_template('edit.html', product=controller.product)


@app.route('/edit/product/<string:id>/<string:name>/<int:amount>/<float:price>/<string:description>/<string:status>', methods=['POST'])
def edit_return(id, name, amount, price, description, status):
    update = controller.put(id,
                            {"name": name,
                             "amount": amount,
                             "price": price,
                             "description": description,
                             "status": status})
    return index()


@app.route('/details/<string:id>')
def details(id):
    controller.get(id, get_one="True")
    return render_template('details.html', product=controller.product)


@app.route('/product/<string:id>')
def delete(id):
    deletion = controller.delete(id_product=id)

    return index()


if __name__ == '__main__':
    app.run(debug=True)
