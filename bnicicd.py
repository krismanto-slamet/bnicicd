import requests

print ("Hello World")
print ("Testing bnicicd.py")

response = requests.get("https://www.google.com")

print (response.text)