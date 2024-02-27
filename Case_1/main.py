from app.infrastacture.FileReader import FileReader


def main():
    text = FileReader("test.txt")
    print(text.Read())


if __name__ == '__main__':
    main()


