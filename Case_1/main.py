from app.infrastacture.FileReader import FileReader
from app.core.Algorithms.PersinAlgorithm import PersonAlg
from app.core.JsonGenerator import JsonGenerator
import json


def main():
    text = FileReader("Nick Vinogradov.docx").Read()
    person = PersonAlg(text).PersonCreate()



if __name__ == '__main__':
    main()