from app.infrastacture.FilesReaderTypes.IFIle import IFile


class TxtReader(IFile):

    def Read(self, path: str) -> str:
        try:
            with open(path, 'r', encoding="utf-8") as file:
                return file.read()
        except TypeError:
            raise TypeError
