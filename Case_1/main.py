from app.infrastacture.FileReader import FileReader

def main():
    text = FileReader("Document.docx")
    print(text.Read())

if __name__ == '__main__':
    main()