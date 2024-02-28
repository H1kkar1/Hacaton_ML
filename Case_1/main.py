from app.infrastacture.FileReader import FileReader

def main():
    text = FileReader("Artur Yapparov.docx")
    print(text.Read())

if __name__ == '__main__':
    main()