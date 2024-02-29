from dataclasses import dataclass

@dataclass
class Education:
    year: str
    organization: str
    faculty: str
    specialty: str
    result: str
    education_type: str
    education_level: str

    def data(self):
        return {
            "year": self.year,
            "organization": self.organization,
            "faculty": self.faculty,
            "specialty": self.specialty,
            "result": self.result,
            "education_type": self.education_type,
            "education_level": self.education_level,
        }