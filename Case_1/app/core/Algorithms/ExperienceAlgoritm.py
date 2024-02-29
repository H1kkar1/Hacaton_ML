from app.core.Algorithms.FindAlg import find_info, find_info_regular
from app.core.Models.ExperienceItems import Experience


class ExperienceAlg:
    text: str

    def __init__(self, text: str):
        self.text = text

    def experience_create(self) -> Experience:
        return Experience(
            starts="asd",
            ends="asd",
            employer="asd",
            city="asd",
            url="asd",
            position="asd",
            description="asd",
            order="asd",
        )