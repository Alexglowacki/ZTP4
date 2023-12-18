from flask import Flask
from flask_restful import Api, Resource
from flask import Response

from api import database_connection
from models import product_model
from api import database_operations

app = Flask(__name__)
api = Api(app)


# new resource
class ProductController(Resource):
    db = database_connection.connect2db()

    product_list = list()
    product = {}

    # get product here
    def get(self, id_product, get_one: str):
        return_document = {}

        if get_one == "True":
            try:
                return_document = database_operations.getfromDB(self.db, id_product)
                self.product = return_document
            except TypeError as e:
                print(e)
                return Response(status=500)
            return Response(return_document, status=200)
        elif get_one == "False":
            try:
                return_list = database_operations.getAllFromDB(self.db)
                self.product_list = return_list
            except TypeError as e:
                print(e)
                return Response(status=500)
            return Response(status=200)

    def post(self, name: str, amount: int, price: float, description: str, status: str):

        document = product_model.ProductModel.get_model()
        document["name"] = name
        document["amount"] = amount
        document["price"] = price
        document["description"] = description
        document["status"] = status

        if price < 0.0:
            return Response(status=400)

        try:
            database_operations.insertInDB(self.db, document=document)
        except TypeError as e:
            print(e)
            return Response(status=500)
        return Response(document, status=200)

    # Update product
    # def put(self, id_product: int, item2update: str, value2update):
    def put(self, id_product: int, document):
        update_dict = document
        try:
            database_operations.updateDocument(self.db, id_product, update_dict)
        except Exception as e:
            print(e)
            return Response(status=404)
        return Response(status=200)

    def delete(self, id_product):
        try:
            result = database_operations.deleteDocument(self.db, document_id=id_product)
            if result:
                return Response(status=200)
            else:
                return Response(status=404)
        except Exception as e:
            print(e)
            return Response(status=500)


api.add_resource(ProductController,
                 "/product/<string:id_product>",  # for delete
                 "/product/<string:id_product>/<string:get_one>",  # for get and get list
                 "/product/<string:name>/<int:amount>/<float:price>/<string:description>/<string:status>",  # for post
                 "/product/<string:id_product>/<string:item2update>/<value2update>")  # for put/patch

if __name__ == '__main__':
    app.run(debug=True)
