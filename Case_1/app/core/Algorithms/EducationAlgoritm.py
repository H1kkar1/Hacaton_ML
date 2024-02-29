from app.core.Algorithms.FindAlg import find_info, find_info_regular
from app.core.Models.EducationItems import Education


class EducationAlg:
    text: str

    def __init__(self, text: str):
        self.text = text

    def education_create(self) -> Education:

        return Education(
            year="add",
            organization="add",
            faculty="add",
            specialty="add",
            result="add",
            education_type="add",
            education_level="add",
        )