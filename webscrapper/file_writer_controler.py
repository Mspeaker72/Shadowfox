def write(content: str, file_name: str):
    try:
        with open("output/"+file_name, "w",encoding="utf-8") as file:
            file.write(content)
    except IOError as e:
        print(f"Error writing to {file_name}: {e}")

