from dataclasses import dataclass
from typing import Optional

@dataclass
class Person:
    first_name: str
    last_name: Optional[str]
    middle_name: str
    birth_date: str
    birth_date_year_only: int
    country: str
    city: str
    about: str
    key_skills: [str]
    salary_expectations_amount: float
    salary_expectations_currency: str
    photo_path: Optional[str]
    gender: bool
    language: str
    resume_name: str

    def data(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "middle name": self.middle_name,
            "birth date": self.birth_date,
            "birth_date_year_only": self.birth_date_year_only,
            "country": self.country,
            "city": self.city,
            "about": self.about,
            "key skills": self.key_skills,
            "salary_expectations_amount": self.salary_expectations_amount,
            "salary_expectations_currency": self.salary_expectations_currency,
            "photo_path": self.photo_path,
            "gender": "Male" if self.gender else "Female",
            "language": self.language,
            "resume name": self.resume_name
        }