from app.core.Algorithms.FindAlg import find_info, find_info_regular
from app.core.Models.EducationItems import Education

key_words_organization = ["University", "School"]
key_words_speciality = ["Specialization"]
key_words_faculty = ["Faculty of", "Faculty"]

class EducationAlg:
    text: str

    def __init__(self, text: str):
        self.text = text

    def education_create(self) -> Education:

        text = self.text

        return Education(
            year=find_info_regular(text, key_words_organization, r"\b[0-9-]+[0-9]{,15}\b"),
            organization=find_info_regular(text, key_words_organization, r"\b[A-Za-z]+[A-Za-z]+[A-Za-z]{,15}\b"),
            faculty=find_info_regular(text, key_words_faculty, r"\b(\b[A-Za-z]{,15}\b) (\b[A-Za-z]{,15}\b)"),
            specialty=find_info_regular(text, key_words_speciality, r"(\b[A-Za-z]{,15}\b) (\b[A-Za-z]{,15}\b) (\b[A-Za-z]{,15}\b)"),
            result="Processing...",
            education_type="Processing...",
            education_level="Processing...",
        )