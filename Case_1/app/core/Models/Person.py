from typing import List


class Person:
    first_name: str
    last_name = ""
    middle_name: str
    birth_date: str
    birth_date_year_only: int
    country: str
    city: str
    about: str
    key_skills: List[str]
    salary_expectations_amount: float
    salary_expectations_currency: float
    photo_path = ""
    gender: bool
    language: str
    resume_name: str