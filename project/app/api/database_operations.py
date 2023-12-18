import pymongo

from pymongo import MongoClient
from pymongo import collection

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId


def insertInDB(db, document):
    """_summary_

    Args:
        db (_type_): _description_
        document (_type_): _description_
    """
    collection = db['products']

    print(f"DEBUG: {document}")

    try:
        collection.insert_one(document)
        print("DEBUG: Inserted a document into DB")
    except Exception as e:
        print(e)
        return False
    return True


def deleteDocument(db, document_id):
    """_summary_

    Args:
        db (_type_): _description_
    """

    collection = db['products']

    print(f"DEBUG: Deleting product with id: {document_id}")
    document_id = str(document_id)

    if collection.find_one({"_id": ObjectId(document_id)}) is not None:
        try:
            collection.delete_one({"_id": ObjectId(document_id)})
            if collection.find_one({"_id": ObjectId(document_id)}) is None:
                print("DEBUG: Deleted a document from DB")
            else:
                print("DEBUG: Not deleted")
        except Exception as e:
            print(e)
            return False
        return True
    else:
        return False


def updateDocument(db, id, update_data: dict):
    """_summary_

    Args:
        id (int): _description_
        item2update (str): _description_
        value2update (str): _description_
    """
    collection = db['products']

    id = str(id)

    args = update_data.items()

    if update_data == {"amount": "0"}:
        update_data = {"amount": 0}

        try:
            result = collection.update_one({'_id': ObjectId(id)}, {'$set': update_data})
            result = collection.update_one({'_id': ObjectId(id)}, {'$set': {'status': 'Unavailable'}})
            if result.modified_count > 0:
                print(f"DEBUG: Document with ID {id} updated successfully")
                return True
            else:
                print(f"DEBUG: Document with ID {id} not found or not modified")
                return False
        except Exception as e:
            print(e)
            return False
    else:
        for key, value in args:
            if key == 'amount':
                update_data = {"amount": int(value)}
                break

            if key == 'price':
                update_data = {"price": float(value)}
                break

            if key == "price" and float(value) < 0:
                return False

        try:
            result = collection.update_one({'_id': ObjectId(id)}, {'$set': update_data})
            if result.modified_count > 0:
                print(f"DEBUG: Document with ID {id} updated successfully")
                return True
            else:
                print(f"DEBUG: Document with ID {id} not found or not modified")
                return False
        except Exception as e:
            print(e)
            return False


def getfromDB(db, id):
    """Retrieve a document from the database.

    Args:
        db (pymongo.database.Database): The MongoDB database.
        document_id (str): The ID of the document to retrieve.

    Returns:
        dict or None: The retrieved document or None if not found.
    """
    collection = db['products']

    id = str(id)

    try:
        document = collection.find_one({'_id': ObjectId(id)})
        if document:
            print(f"DEBUG: Retrieved document from DB: {document}")
            return document
        else:
            print(f"DEBUG: Document with ID {id} not found in DB")
            return None
    except Exception as e:
        print(e)
        return None


def getAllFromDB(db):
    """_summary_

    Args:
        db (_type_): _description_

    Returns:
        _type_: _description_
    """
    collection = db['products']
    try:
        all_json = collection.find({})
        products = list(all_json)
        x = dict()
        [print(x) for x in products]
        print(f"DEBUG: Retrieved {len(products)} items from the collection")
        return products
    except Exception as e:
        print(e)
        return False
