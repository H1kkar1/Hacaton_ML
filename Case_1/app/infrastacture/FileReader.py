from app.infrastacture.FilesReaderTypes.IFIle import IFile
from app.infrastacture.FilesReaderTypes.TxtRaeder import TxtReader


class FileReader(IFile):
    file_path: str
    type: str

    def __init__(self, path: str):
        self.file_path = path
        self.type = path.split('.')[-1]

    def Read(self) -> str:
        match self.type:
            case "rtf" | "txt":
               response = TxtReader.Read(self, path=self.file_path)
               return response
            case _:
                return "Такой тип файлов не поддерживается"