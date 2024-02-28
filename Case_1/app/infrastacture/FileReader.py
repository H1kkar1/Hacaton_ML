from app.infrastacture.FilesReaderTypes.IFIle import IFile
from app.infrastacture.FilesReaderTypes.PDFRaeder import PDFReader
from app.infrastacture.FilesReaderTypes.DocxReader import DocxReader


class FileReader(IFile):
    file_path: str
    type: str

    def __init__(self, path: str):
        self.file_path = path
        self.type = path.split('.')[-1]

    def Read(self) -> str:
        match self.type:
            case "pdf":
                response = PDFReader.Read(self, path=self.file_path)
                return response
            case "docx":
                response = DocxReader.Read(self, path=self.file_path)
                return response
            case _:
                return "Такой тип файлов не поддерживается"