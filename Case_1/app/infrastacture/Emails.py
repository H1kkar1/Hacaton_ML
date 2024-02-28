import re

class Emails():
    pattern: str
    newline: str

    def SearchEmail(self,paragraph:str) -> str:
        pattern = r'^[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$'
        regexp = re.compile(pattern)
        newline = regexp.search(paragraph)
        return newline.group()