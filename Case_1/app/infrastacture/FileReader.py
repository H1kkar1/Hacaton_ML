from app.infrastacture.FilesReaderTypes.IFIle import IFile
from app.infrastacture.FilesReaderTypes.TxtRaeder import TxtReader
from app.infrastacture.FilesReaderTypes.PDFRaeder import PDFReader
from app.infrastacture.FilesReaderTypes.ExelReader import ExelReader

class FileReader(IFile):
    file_path: str
    type: str

    def __init__(self, path: str):
        self.file_path = path
        self.type = path.split('.')[-1]

    def Read(self) -> str:
        match self.type:
            case "txt":
               response = TxtReader.Read(self, path=self.file_path)
               return response
            case "pdf":
                response = PDFReader.Read(self, path=self.file_path)
                return response
            case "xlsx":
                response = ExelReader.Read(self, path=self.file_path)
                return response
            case _:
                return "Такой тип файлов не поддерживается"