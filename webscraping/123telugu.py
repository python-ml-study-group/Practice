import requests
import re
from bs4 import BeautifulSoup
url = "https://www.123telugu.com/reviews/f3-telugu-movie-review.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
tags = soup.find_all("strong")
rating_text = ""
for tag in tags:
    if "123telugu.com Rating" in tag.text:
        rating_text = tag.text
if rating_text == "":
    print("Rating not found.")
else:
    rating_text = rating_text.replace("123telugu.com Rating:", "")
    rating_text = rating_text.replace("/5", "")
    print (f"rating: = {rating_text}")
