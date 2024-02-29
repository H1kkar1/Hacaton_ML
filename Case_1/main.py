import json

from app.core.JsonGenerator import JsonGenerator
from app.core.Models.PersonItems import Person
from app.core.Models.LanguageItems import Language
from app.core.Models.ExperienceItems import Experience
from app.core.Models.EducationItems import Education
from app.infrastacture.FileReader import FileReader
from app.core.Algorithms.PersinAlgorithm import PersonAlg
from app.core.Algorithms.EducationAlgoritm import EducationAlg
from app.core.Algorithms.ExperienceAlgoritm import ExperienceAlg
from app.core.Algorithms.LanguageAlgoritm import LanguageAlg
from app.core.JsonGenerator import JsonGenerator
import json


def main():
    text = FileReader("Nick Vinogradov.docx").Read()

    person = PersonAlg(text).person_create()

    person = PersonAlg(text).person_create()
    education = EducationAlg(text).education_create()
    experience = ExperienceAlg(text).experience_create()
    language = LanguageAlg(text).language_create()

    generator = JsonGenerator(person, education, experience, language)
    data = generator.Generate_json()
    with open("result.json", "w") as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    main()