from app.core.Models.Education import Education
from app.core.Models.Person import Person
from app.core.Models.Language import Language
from app.core.Models.Experience import Experience


class JsonGenerator:
    person: Person
    education: Education
    experience: Experience
    language: Language

    def __init__(self, per, ed, ex, lan):
        self.person = per
        self.education = ed
        self.language = lan
        self.experience = ex

    def Generate_json(self):
        return {self.person, self.education, self.experience, self.language}
