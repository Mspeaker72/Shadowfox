import requests
import filter
from bs4 import BeautifulSoup

url = "https://shadowfox.in/"


# url = input("please provide url for site")

def retrieve_contents(address: str):
    response = requests.get(address)
    html_content = response.content
    return html_content


soup = BeautifulSoup(retrieve_contents(url), 'html.parser')


def find_all_links(context):
    result = context.find_all("a")
    # you can use get on class to find attribute
    return [res.get("href") for res in result if res.get("href")]


def images(context):
    result = context.find_all("img")
    return [res.get("src") for res in result]


filter.add(find_all_links(soup))
print(filter.get_possible_contact())
print(images(soup))

