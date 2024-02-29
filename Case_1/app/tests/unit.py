import json
from app.core.JsonGenerator import JsonGenerator
from app.core.Models.PersonItems import Person
from app.core.Models.LanguageItems import Language
from app.core.Models.ExperienceItems import Experience
from app.core.Models.EducationItems import Education


def json_create_test():
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