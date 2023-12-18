import requests
# from flask import request
# TODO DELETE THIS FILE
BASE = "http://127.0.0.1:5000/"

# not existing document:
response = requests.get(BASE + "product/65676a3c91ea9e8e62d577f3/True")
print("Expect 200")
print(response)

# existing document:
response = requests.get(BASE + "product/65676aa7d72d2a977fe9f1f1/True")
print("Expect 200")
print(response)

response = requests.put(BASE + "product/65676aa7d72d2a977fe9f1f1/name/Chevy")
print("Expect 200")
print(response)

response = requests.put(BASE + "product/65676aa7d72d2a977fe9f1f1/amount/100000")
print("Expect 200")
print(response)

response = requests.put(BASE + "product/65676aa7d72d2a977fe9f1f1/price/8.0")
print("Expect 200")
print(response)

# check if updated:
response = requests.get(BASE + "product/65676aa7d72d2a977fe9f1f1/True")
print("Expect 200")
print(response)

# bring back to prev state
response = requests.put(BASE + "product/65676aa7d72d2a977fe9f1f1/name/Porsche")
print("Expect 200")
print(response)

# delete
response = requests.delete(BASE + "product/656769667ddc11fbdadd9e14")
print("Expect 200 once and then 404")
print(response)

# post
response = requests.post(BASE + "product/Ferrari/2/103000.0/Bardzo fajne auto/Available")
print("Expect 200")
print(response)

# get list
response = requests.get(BASE + "product/65676aa7d72d2a977fe9f1f1/False")
print("Expect 200")
print(response)

# update document with amount = 0
response = requests.put(BASE + "product/656f90e228e0ccb23df2247a/amount/0")
print("Expect 200")
print(response)
