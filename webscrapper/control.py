import requests
import filter
from bs4 import BeautifulSoup


def retrieve_contents(address: str):
    response = requests.get(address)
    html_content = response.content
    return html_content


def find_all_links(context):
    result = context.find_all("a")
    # you can use get on class to find attribute
    return [res.get("href") for res in result if res.get("href")]


def find_all_paragraphs(context):
    paragraphs = context.find_all("p")

    return [paragraph.text for paragraph in paragraphs]


def images(context):
    result = context.find_all("img")
    return [res.get("src") for res in result]


# filter.set_paragraphs(find_all_paragraphs(soup))
# filter.get_paragraph_tag_information()

def start():
    url = "https://shadowfox.in/"

    # url = input("please provide url for site")
    return BeautifulSoup(retrieve_contents(url), 'html.parser')


def main_loop(context):
    filter.add(find_all_links(context))
    while True:
        command = input("what would you like to search :")

        if command.__contains__("social media"):
            print(filter.get_socials())
        elif command.__contains__("contact"):
            print(filter.get_possible_contact())


if __name__ == '__main__':
    soup = start()
    main_loop(soup)
