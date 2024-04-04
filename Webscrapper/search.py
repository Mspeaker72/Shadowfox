from bs4 import BeautifulSoup
import requests

from Webscrapper.bread import Bread

bread = "https://www.checkers.co.za/c-545/All-Departments/Food/Bakery/Bread-and-Rolls"
response = requests.get(bread)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')
elements = soup.find_all(class_="product-listening-click")
prices = soup.find_all(class_="now")
filter_prices =[str(price).replace(f"<span class=\"now\">", "").replace("<sup>", "")
      .replace("</span>", "").replace("</sup>", "").strip() for price in prices]
checkers_bread = Bread()
i = 0
previous = ""
for bread in elements:

    title = bread.get('title')

    if previous != title:
        checkers_bread.__add__(" - ".join([title, filter_prices[i]]))
        i += 1
        previous = title
print(checkers_bread.get_products())
