from behave import given, when, then
import requests
import json

# Scenario: Add new product with correct parameters
@given('the Flask API is running')
def step_given_flask_api_running(context):
    context.api_url = "http://127.0.0.1:5000/"


@when('a POST request is made to "{endpoint}"')
def step_when_post_request_made(context, endpoint):
    req = f"{context.api_url}{endpoint}"
    context.response = requests.post(req)


@then('the response status code should be {status_code:d}')
def step_then_status_code_should_be(context, status_code):
    assert context.response.status_code == status_code, f"Expected status code {status_code}, but got {context.response.status_code}"


@when('a POST request is made to with negative price to "{endpoint}"')
def step_when_post_request_made(context, endpoint):
    req = f"{context.api_url}{endpoint}"
    context.response = requests.post(req)


@then('the response status code should be {status_code:d}')
def step_then_status_code_should_be(context, status_code):
    assert context.response.status_code == status_code, f"Expected status code {status_code}, but got {context.response.status_code}"

# Scenario: Automatic change of status to unavailable when amount  is equal to 0
@when('a PUT request is made to a product changing the amount to 0 to "{endpoint}"')
def step_then_response_should_contain_user_info(context, endpoint):
    req = f"{context.api_url}{endpoint}"
    context.response = requests.put(req)


@then('the response status code should be {status_code:d}')
def step_then_status_code_should_be(context, status_code):
    assert context.response.status_code == status_code, f"Expected status code {status_code}, but got {context.response.status_code}"


@when('a GET request is made to a product with amount = 0 to "{endpoint}"')
def step_then_response_should_contain_user_info(context, endpoint):
    req = f"{context.api_url}{endpoint}"
    context.response = requests.get(req)


@then('the response status code should be {status_code:d}')
def step_then_status_code_should_be(context, status_code):
    assert context.response.status_code == status_code, f"Expected status code {status_code}, but got {context.response.status_code}"
