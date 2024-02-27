from app.infrastacture.FileReader import FileReader


def main():
    text = FileReader("test.txt")
    print(text.Read())

    text = FileReader("test.pdf")
    print(text.Read())

    text = FileReader("test.xlsx")
    print(text.Read())


if __name__ == '__main__':
    main()