import requests
from bs4 import BeautifulSoup
url = "https://kapiva.in/daily-diet/kapiva-a2-desi-cow-ghee-500gms/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
price_element = soup.find('span', class_='leading-[1.4]')
if price_element is None:
    print("Price not found.")
else:
    price = price_element.text
    print("Price:", price) 
