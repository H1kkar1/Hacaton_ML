from app.infrastacture.FilesReaderTypes.IFIle import IFile
import openpyxl
import pandas

class ExelReader(IFile):
    def Read(self, path: str) -> str:
        try:
            excel_data_df = pandas.read_excel('test.xlsx')

            return excel_data_df.head()
            # workbook = openpyxl.load_workbook('test.xlsx')
            # sheet = workbook.active
            #
            # for row in sheet.iter_rows(values_only=True):
            #      return row
        except TypeError:
            raise TypeError