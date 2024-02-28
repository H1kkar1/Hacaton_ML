from dataclasses import dataclass

@dataclass
class Language:
    language: str
    language_level: str

    def data(self):
        return {"language": self.language, "language_level": self.language_level}