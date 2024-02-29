from app.core.Algorithms.FindAlg import find_info, find_info_regular
from app.core.Models.LanguageItems import Language

key_words_language = ["Language", "Languages", "language", "languages", "LANGUAGE", "LANGUAGES"]

class LanguageAlg:
    text: str

    def __init__(self, text: str):
        self.text = text

    def language_create(self) -> Language:
        text = self.text
        return Language(
                language=find_info(text, key_words_language),
                language_level="Processing..."
                )