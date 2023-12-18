Feature: 

  Scenario: Add new product with correct parameters
    Given the Flask API is running
    When a POST request is made to "product/Ferrari/2/103000.0/Bardzo fajne auto/Available"
    Then the response status code should be 200

  Scenario: Add new product with negative price
    Given the Flask API is running
    When a POST request is made to with negative price to "product/Ferrari/2/%9610.0/Bardzo fajne auto/Available"    Then the response status code should be 400
    Then the response status code should be 400

  Scenario: Automatic change of status to unavailable when amount  is equal to 0
    Given the Flask API is running
    When a PUT request is made to a product changing the amount to 0 to "product/6567a5930237fad20caffd87/amount/0"
    Then the response status code should be 200
    When a GET request is made to a product with amount = 0 to "product/6567a5930237fad20caffd87/True"
    Then the response status code should be 200

# # this will always fail since the feature is not implemented
#   Scenario: Show product history
#     Given the Flask API is running
#     When a GET request is made to a product show the document with its changes "product/65676aa7d72d2a977fe9f1f1/True/True"
#     Then the response status code should be 200
#     And There should be response with all the data requested
