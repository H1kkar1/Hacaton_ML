from app.infrastacture.FileReader import FileReader
from app.core.Algorithms.PersinAlgorithm import PersonAlg
from app.core.JsonGenerator import JsonGenerator
import json


def main():
    text = FileReader("Nick Vinogradov.docx").Read()
    person = PersonAlg(text).PersonCreate()
    print(person.first_name)
    print(person.last_name)
    print(person.middle_name)
    print(person.country)
    print(person.contacts[0].value)



if __name__ == '__main__':
    main()