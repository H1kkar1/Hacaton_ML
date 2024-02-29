from app.core.Models.EducationItems import Education
from app.core.Models.PersonItems import Person
from app.core.Models.LanguageItems import Language
from app.core.Models.ExperienceItems import Experience
from typing import Optional


class JsonGenerator:
    person: Optional[Person]
    education: Optional[Education]
    experience: Optional[Experience]
    language: Optional[Language]

    def __init__(self, person, education, experience, language):
        self.person = person
        self.education = education
        self.language = language
        self.experience = experience

    def Generate_json(self):
        return {
            "resume": {
                "person": self.person.data(),
                "education": self.education.data(),
                "experience": self.experience.data(),
                "language": self.language.data(),
            }
        }
