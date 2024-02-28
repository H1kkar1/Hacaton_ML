from app.core.Models.Education import Education
from app.core.Models.Person import Person
from app.core.Models.Language import Language
from app.core.Models.Experience import Experience


class JsonGenerator:
    person: Person
    education: Education
    experience: Experience
    language: Language

    def __init__(self, person, education, experience, language):
        self.person = person
        self.education = education
        self.language = experience
        self.experience = language

    def Generate_json(self):
        return {self.person, self.education, self.experience, self.language}