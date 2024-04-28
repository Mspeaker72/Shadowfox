import requests



def write(content: str, file_name: str):
    try:
        with open("output/"+file_name, "w",encoding="utf-8") as file:
            file.write(content)
    except IOError as e:
        print(f"Error writing to {file_name}: {e}")


def download(url,file_name):
    try:
        response = requests.get(url+"/"+file_name)
        file = open(f"output/Downloads/{file_name}", "wb")
        file.write(response.content)
        print("Download Complete.")
    except Exception as error:
        print(error)

