from FilesReaderTypes.IFIle import IFile

class FileReader(IFile):
    file_path: str
    result_text: str

    def __init__(self, path: str):
        self.file_path = path

    def Read(self):
        IFile.Read()