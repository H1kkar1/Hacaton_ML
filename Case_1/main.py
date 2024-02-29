import json

from app.core.JsonGenerator import JsonGenerator
from app.core.Models.PersonItems import Person
from app.core.Models.LanguageItems import Language
from app.core.Models.ExperienceItems import Experience
from app.core.Models.EducationItems import Education
from app.infrastacture.FileReader import FileReader
from app.core.Algorithms.PersinAlgorithm import PersonAlg
from app.core.JsonGenerator import JsonGenerator
import json


def main():
    text = FileReader("Nick Vinogradov.docx").Read()
    person = PersonAlg(text).person_create()



if __name__ == '__main__':
    main()