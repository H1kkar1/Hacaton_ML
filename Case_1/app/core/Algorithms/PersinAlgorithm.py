from app.core.Models.ContactItems import Contact
from app.core.Models.PersonItems import Person
import re

key_words_country = ["Citizenship", "Сountry"]
key_words_city = ["City", "My city"]
key_words_telephone = ["Telephone", "telephone", "Phone", "phone"]
key_words_dateBirdth = ["Date", "telephone", "Phone", "phone"]
key_words_email = ["E-mail", "Mail", "Email", "email", "mail"]


def find_info_regular(text, keywords, regular):
    for keyword in keywords:
        print(keyword)
        try:
            text = text.split(keyword)
            print(text)
            text = text[1].split('\n')[0]
            print(text)
            result = re.sub("['\t'|-|:|_]", '', text)
            print(result)
            result = re.search(regular, text).group()
            print(result)

            return result
        except Exception:
            string = ""
    return string


def find_info(text, keywords):
    for keyword in keywords:
        try:
            text = text.split(keyword)
            text = text[1].split('\n')[0]
            return re.sub("[' '|-|:|_]", '', text)
        except IndexError:
            string = ""
        return string


class PersonAlg:
    text: str

    def __init__(self, text: str):
        self.text = text

    def PersonCreate(self) -> Person:
        text = self.text
        try:
            textt = self.text.split('\n')
            last_name = textt[0].split(' ')[2]
        except IndexError:
            last_name = ""
        return Person(
            first_name=text.split('\n')[0].split(' ')[0],
            last_name=last_name,
            middle_name=text.split('\n')[0].split(' ')[1],
            birth_date="",
            birth_date_year_only="",
            country=find_info(text, key_words_country),
            city=find_info(text, key_words_city),
            about="asd",
            key_skills=["asd"],
            salary_expectations_amount=120301.0120,
            salary_expectations_currency=91293.8128,
            photo_path="",
            gender=find_info(text, "Gender"),
            language=find_info(text, "language"),
            resume_name="",
            contacts=[
                Contact(
                    resume_contact_item_id=1,
                    value=find_info_regular(text, key_words_telephone, r"(?:(?:8|\+7)[\- ]?)?(?:\(?\d{3}\)?[\- ]?)?[\d\- ]{7,15}"),
                    comment="adf",
                    contact_type="Telephone"
                ),
                Contact(
                    resume_contact_item_id=2,
                    value=find_info_regular(text, key_words_email, r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b"),
                    comment="adf",
                    contact_type="Email"
                )
            ]
        )