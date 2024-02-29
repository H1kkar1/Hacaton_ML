from app.core.Algorithms.FindAlg import find_info, find_info_regular
from app.core.Models.LanguageItems import Language


class LanguageAlg:
    text: str

    def __init__(self, text: str):
        self.text = text

    def language_create(self) -> Language:
        return Language(
            language="En",
            language_level="loh"
        )