from app.infrastacture.FilesReaderTypes.IFIle import IFile
import docx

class DocxReader(IFile):

    def Read(self, path: str) -> str:
        doc = docx.Document(path)
        text = []
        for paragraph in doc.paragraphs:
            text.append(paragraph.text)
        return '\n'.join(text)