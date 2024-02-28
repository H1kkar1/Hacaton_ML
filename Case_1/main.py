from typing import List

from app.core.JsonGenerator import JsonGenerator
from app.core.Models.Person import Person
from app.core.Models.Language import Language
from app.core.Models.Experience import Experience
from app.core.Models.Education import Education
from app.infrastacture.FileReader import FileReader


def main():
    # person = Person(
    #     first_name="lsdvl",
    #     last_name="asd",
    #     middle_name="assd",
    #     birth_date="12.12.1222",
    #     birth_date_year_only=1222,
    #     country="asd",
    #     city="asd",
    #     about="asd",
    #     key_skills=List["asd"],
    #     salary_expectations_amount=120301.0120,
    #     salary_expectations_currency=91293.8128,
    #     photo_path="http=//la,lc",
    #     gender=True,
    #     language="asd",
    #     resume_name="asd",
    # )
    # language = Language(
    #     language="En",
    #     language_level="loh"
    # )
    # education = Education(
    #     year="add",
    #     organization="add",
    #     faculty="add",
    #     specialty="add",
    #     result="add",
    #     education_type="add",
    #     education_level="add",
    # )
    # exp = Experience(
    #     starts="asd",
    #     ends="asd",
    #     employer="asd",
    #     city="asd",
    #     url="asd",
    #     position="asd",
    #     description="asd",
    #     order="asd",
    # )

    # json = JsonGenerator(person, education, exp, language)
    # return json
    # text = FileReader("Nikita Ivanov.pdf")
    # print(text.Read())

    text = FileReader("Nick Vinogradov.docx")
    print(text.Read())


if __name__ == '__main__':
    main()