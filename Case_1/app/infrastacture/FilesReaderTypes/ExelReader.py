from app.infrastacture.FilesReaderTypes.IFIle import IFile
import openpyxl

class ExelReader(IFile):
    def Read(self, path: str) -> str:
        try:
            workbook = openpyxl.load_workbook('test.xlsx')
            sheet = workbook.active

            for row in sheet.iter_rows(values_only=True):
                 return row
        except TypeError:
            raise TypeError