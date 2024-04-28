import requests
import filter
import file_writer_controler
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


def start():
    global url
    # url = "https://shadowfox.in/"

    url = input("please provide url for site: \n")
    print("currently on : \n"+url)
    return BeautifulSoup(retrieve_contents(url), 'html.parser')


def handle_command(command_function, file_name):
    try:
        result = command_function()
        print(result)
        file_writer_controler.write(result, file_name)
    except Exception as e:
        print(f"Error handling command: {e}")


def user_input():
    print("-" * 60)
    command = input("What would you like to search:\n").lower()
    print("-" * 60)
    return command


def main_loop(context):
    filter.add(find_all_links(context))
    filter.set_images(images(context))
    while True:
        command = user_input()

        if "social media" in command:
            handle_command(filter.get_socials, "Socials.txt")
        elif "contact details" in command:
            handle_command(filter.get_possible_contact, "Contact_details.txt")
        elif "email" in command:
            handle_command(filter.get_email_contact, "email_details.txt")
        elif "images" in command:
            handle_command(filter.get_images, "img_details.txt")

        elif "text" in command:
            filter.set_paragraphs(find_all_paragraphs(context))
            handle_command(filter.get_paragraph_tag_information, "text.txt")
        elif "download" in command:
            file_writer_controler.download(url, input("Please enter file_name :"))


if __name__ == '__main__':
    soup = start()
    main_loop(soup)
