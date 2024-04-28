from datetime import datetime

import requests


def write(content: str, file_name: str):
    try:
        with open("output/" + file_name, "w", encoding="utf-8") as file:
            file.write(content)
    except IOError as e:
        print(f"Error writing to {file_name}: {e}")


def download(url, file_name: str):
    try:

        if file_name.startswith("/"):
            file_name = file_name[1:]

        ext = ".png"

        if "webp" in file_name:
            ext = ".webp"
        request = url + "/" + file_name
        print(request)
        response = requests.get(request)

        if response.status_code != 200:
            return

        current_time = datetime.now().strftime("%Y%m%d%H%M%S")

        filename_with_timestamp = f"{current_time + ext}"

        with open(f"output/Downloads/{filename_with_timestamp}", "wb") as file:
            file.write(response.content)

        print("Download Complete.")
    except Exception as error:
        print(error)
