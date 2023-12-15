from bs4 import BeautifulSoup
html = "<html><head><title>Test</title></head><body><h1 >Parse me!</h1></body></html>"
import requests
response = requests.get('https://www.google.com')
print (type(response), response.url,  response)
print ("Response.text=", response.text)
soup = BeautifulSoup(response.text, 'html.parser')
