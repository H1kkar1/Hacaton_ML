from app.infrastacture.FileReader import FileReader

def main():
    text = FileReader("Alex Konev.docx")
    print(text.Read())

if __name__ == '__main__':
    main()