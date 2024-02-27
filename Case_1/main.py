from app.infrastacture.FileReader import FileReader


def main():
    text = FileReader("Bakend_lab_14.pdf")
    print(text.Read())

    text = FileReader("test.pdf")
    print(text.Read())


if __name__ == '__main__':
    main()