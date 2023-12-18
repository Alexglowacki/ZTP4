from behave import given, when, then
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# from flask import request
# TODO DELETE THIS FILE
BASE = "http://127.0.0.1:5000/"

@given('the Flask API is running')
def step_given_flask_api_running():
    uri = f'mongodb+srv://root:passwd@ztp.8oefhja.mongodb.net/?retryWrites=true&w=majority'
    # Set up your Flask application or other necessary resources
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    client.admin.command('ping')

@when('a GET request is made to "/api/data"')
def step_when_get_request_made():
    # Make a GET request to your Flask API

    # get nonexisting document
    response = requests.get(BASE + "product/65676a3c91ea9e8e62d577f3/True")

    # get existing document:
    response = requests.get(BASE + "product/65676aa7d72d2a977fe9f1f1/True")

@then('the response status code should be 200')
def step_then_status_code_should_be_200():
    # Check that the response status code is 200

@then('the response should contain "Hello, World!"')
def step_then_response_should_contain_hello_world():
    # Check that the response contains the expected content
