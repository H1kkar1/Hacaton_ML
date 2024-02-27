from app.infrastacture.FilesReaderTypes.IFIle import IFile
from pypdf import PdfReader

class PDFReader(IFile):
    def Read(self, path: str) -> str:
        try:
            reader = PdfReader("test.pdf")
            number_of_pages = len(reader.pages)
            page = reader.pages[0]
            text = page.extract_text()
            return text
        except TypeError:
            raise TypeError