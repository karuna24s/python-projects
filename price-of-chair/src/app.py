import requests
from bs4 import BeautifulSoup

user_budget = int(input("What is your budget? Enter a whole number: "))

request = requests.get("https://www.johnlewis.com/john-lewis-monaco-gaming-chair-black-steel/p3348021")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})

string_price = element.text.strip()
price_no_currency = string_price[1:]  # This would copy all except the index 0, which is the pound sign
price = float(price_no_currency)

if price > user_budget:
  print("This item is over your budget... Sorry!")
else:
  print("Lets buy it!")
