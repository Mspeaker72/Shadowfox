import lists_and_ref

filtered_information = {
    'emails': set(),
    'mobile_telephone_numbers': set(),
    "paragraphs": [],
    "social_media_links": [],
    "general_links": [],
    "images": []
}
social_media_platforms = [platform.lower() for platform in lists_and_ref.common_socials]


def add(links: list):
    for link in links:
        link = link.lower()  # Convert link to lowercase for case-insensitive comparison
        if 'tel' in link:
            filtered_information['mobile_telephone_numbers'].add(link)
        elif '@' in link and link not in filtered_information['emails']:
            filtered_information['emails'].add(link)
        else:
            # Check if the link contains any substrings representing social media platforms
            if any(platform in link for platform in social_media_platforms):
                filtered_information["social_media_links"].append(link)
            else:
                # If the link doesn't match any category, add it to a general list of links
                filtered_information['general_links'].append(link)


def get_possible_contact():
    phone_numbers = filtered_information['mobile_telephone_numbers']
    if not phone_numbers:
        return "Sorry, no mobile or telephone numbers were found."
    print("Possible phone numbers contained: ")
    return f"{"\n".join(phone_numbers)}"


def get_email_contact():
    emails = filtered_information['emails']
    if not emails:
        return "Sorry, no email addresses were found."
    print("The following email addresses were found:")
    return f" {"\n".join(emails)}"


def get_paragraph_tag_information():
    print("text elements :")
    return "\n".join(filtered_information["paragraphs"])


def set_paragraphs(text: list):
    filtered_information["paragraphs"] = text


def set_images(text: list):
    filtered_information["images"] = text


def get_socials():
    print("Possible social media links : \n")
    return "\n".join(set(filtered_information["social_media_links"]))


def get_all_links():
    print("Possible social media links : \n")
    return "\n".join(set(filtered_information["general_links"]))


def get_images():
    print(filtered_information["images"])
    print("Present images : \n")
    return "\n".join(set(filtered_information["images"]))
