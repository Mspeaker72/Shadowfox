mobile_telephone_numbers = []


def add(collective: list):
    for link in collective:
        if str(link).__contains__("tel"):
            mobile_telephone_numbers.append(link)


def get_possible_contact():
    if len(mobile_telephone_numbers) == 0:
        return "Sorry no mobile or telephone numbers were found"

    tel = ",".join(mobile_telephone_numbers)
    return f"possible phone numbers contained : {tel}"
