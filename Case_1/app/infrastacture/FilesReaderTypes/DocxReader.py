import docx
import re
from app.infrastacture.FilesReaderTypes.IFIle import IFile
from app.infrastacture.NumberPhone import NumPhone


class DocxReader(IFile):

    def Read(self, path: str) -> str:
        doc = docx.Document(path)
        text = []
        for paragraph in doc.paragraphs:
            text.append(paragraph.text)
            index = paragraph.text.find('+')
            if (index != -1):
                phoneRead = NumPhone()
                print("Ваш номер телефона: "+phoneRead.SearchPhone(paragraph.text))
        return ""

