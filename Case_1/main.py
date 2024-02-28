from app.infrastacture.FileReader import FileReader

def main():
    text = FileReader("Artur Yapparov.docx")
    print(text.Read())

import json

from app.core.JsonGenerator import JsonGenerator
from app.core.Models.Person import Person
from app.core.Models.Language import Language
from app.core.Models.Experience import Experience
from app.core.Models.Education import Education
from app.infrastacture.FileReader import FileReader


def main():
    # text = FileReader("test.txt")
    # print(text.Read())

    text = FileReader("Safronov Leonid.pdf")
    print(text.Read())
    text = FileReader("Artur Yapparov.docx")
    print(text.Read())

    # text = FileReader("test.xlsx")
    # print(text.Read())
    person = Person(
        first_name="lsdvl",
        last_name="asd",
        middle_name="assd",
        birth_date="12.12.1222",
        birth_date_year_only=1222,
        country="asd",
        city="asd",
        about="asd",
        key_skills=["asd"],
        salary_expectations_amount=120301.0120,
        salary_expectations_currency=91293.8128,
        photo_path="http=//la,lc",
        gender=True,
        language="asd",
        resume_name="asd",
    )
    language = Language(
        language="En",
        language_level="loh"
    )
    education = Education(
        year="add",
        organization="add",
        faculty="add",
        specialty="add",
        result="add",
        education_type="add",
        education_level="add",
    )
    exp = Experience(
        starts="asd",
        ends="asd",
        employer="asd",
        city="asd",
        url="asd",
        position="asd",
        description="asd",
        order="asd",
    )

    generator = JsonGenerator(person, education, exp, language)
    data = generator.Generate_json()
    with open("result.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    main()