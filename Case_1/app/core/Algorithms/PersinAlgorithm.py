from app.core.Models.ContactItems import Contact
from app.core.Models.PersonItems import Person
from app.core.Algorithms.FindAlg import find_info, find_info_regular

key_words_country = ["Citizenship", "Сountry"]
key_words_city = ["City", "My city"]
key_words_telephone = ["Telephone", "telephone", "Phone", "phone"]
key_words_dateBirdth = ["Date", "date", "DATE"]
key_words_email = ["E-mail", "Mail", "Email", "email", "mail"]

class PersonAlg:
    text: str

    def __init__(self, text: str):
        self.text = text

    def person_create(self) -> Person:
        text = self.text
        try:
            textt = self.text.split('\n')
            last_name = textt[0].split(' ')[2]
        except IndexError:
            last_name = "Processing..."
        return Person(
            first_name=text.split('\n')[0].split(' ')[0],
            last_name=last_name,
            middle_name=text.split('\n')[0].split(' ')[1],
            birth_date="Processing...",
            birth_date_year_only="Processing...",
            country=find_info(text, key_words_country),
            city=find_info(text, key_words_city),
            about="Processing...",
            key_skills=["Processing..."],
            salary_expectations_amount=120301.0120,
            salary_expectations_currency=91293.8128,
            photo_path="Processing...",
            gender=find_info(text, "Gender"),
            resume_name="Processing...",
            source_link="Processing...",
            contacts=[
                Contact(
                    resume_contact_item_id=1,
                    value=find_info_regular(text, key_words_telephone, r"(?:(?:8|\+7)[\- ]?)?(?:\(?\d{3}\)?[\- ]?)?[\d\- ]{7,15}"),
                    comment="Processing...",
                    contact_type="Telephone"
                ),
                Contact(
                    resume_contact_item_id=2,
                    value=find_info_regular(text, key_words_email, r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{,2}\b"),
                    comment="Processing...",
                    contact_type="Email"
                )
            ]
        )