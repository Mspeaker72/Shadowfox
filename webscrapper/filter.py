import lists_and_ref

filtered_information = {'emails': [],
                        'mobile_telephone_numbers': [],
                        "paragraphs": [],
                        "social_media_links": [],
                        "general_links": []}
social_media_platforms = lists_and_ref.common_socials


def add(links: list):
    """
    Extracts mobile telephone numbers and email addresses from a list of links.

    Args:
        links (list): A list of strings representing links.

    Returns:
        None
    """
    for link in links:
        if 'tel' in link:
            filtered_information['mobile_telephone_numbers'].append(link)
        elif '@' in link and link not in filtered_information['emails']:
            filtered_information['emails'].append(link)
        else:
            # Check if the link contains any substrings representing social media platforms
            for socials in social_media_platforms:
                if str(link).title().__contains__(socials):
                    filtered_information["social_media_links"].append(link)
                    break
            else:
                # If the link doesn't match any category, add it to a general list of links
                filtered_information['general_links'].append(link)


def get_possible_contact():
    """
    Returns possible phone numbers contained in the list of links.

    Returns:
        str: A message containing the possible phone numbers, or an error message if none were found.
    """
    phone_numbers = filtered_information['mobile_telephone_numbers']
    if not phone_numbers:
        return "Sorry, no mobile or telephone numbers were found."

    tel = ",".join(phone_numbers)
    return f"Possible phone numbers contained: {tel}"


def get_email_contact():
    """
    Returns the email addresses found in the list of links.

    Returns:
        str: A message containing the email addresses found, or an error message if none were found.
    """
    emails = filtered_information['emails']
    if not emails:
        return "Sorry, no email addresses were found."

    email = ",".join(emails)
    return f"The following email addresses were found: {email}"


def get_paragraph_tag_information():
    text_list = filtered_information["paragraphs"]

    for paragraph in text_list:
        print(paragraph)


def set_paragraphs(text: list):
    filtered_information["paragraphs"] = text
