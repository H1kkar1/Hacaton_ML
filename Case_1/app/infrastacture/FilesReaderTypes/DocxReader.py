
import docx
import re

from app.infrastacture.Emails import Emails
from app.infrastacture.FilesReaderTypes.IFIle import IFile
from app.infrastacture.NumberPhone import NumPhone

from app.infrastacture.FilesReaderTypes.IFIle import IFile
import docx



class DocxReader(IFile):

    def Read(self, path: str) -> str:
        doc = docx.Document(path)
        text = []
        for paragraph in doc.paragraphs:
            text.append(paragraph.text)
            index = [paragraph.text.find('+'), paragraph.text.find('@')]
            if (index[0] != -1):
                phoneRead = NumPhone()
                print("Ваш номер телефона: " + phoneRead.SearchPhone(paragraph.text))
            if (index[1] != -1):
                emails = Emails()
                for adress in paragraph.text.split():
                    if (adress.find('@') != -1):
                        print("Ваша почта: "+emails.SearchEmail(adress))
        return '\n'.join(text)


