import re

class NumPhone():
    pattern: str
    newline: str

    def SearchPhone(self,paragraph:str) -> str:
        # pattern = r'^((\+?7|8)[ \-] ?)?((\(\d{3}\))|(\d{3}))?([ \-])?(\d{3}[\- ]?\d{2}[\- ]?\d{2})$'
        # pattern = r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'
        pattern = r"(?:(?:8|\+7)[\- ]?)?(?:\(?\d{3}\)?[\- ]?)?[\d\- ]{7,15}"
        regexp = re.compile(pattern)
        newline = regexp.search(paragraph)
        return newline.group()