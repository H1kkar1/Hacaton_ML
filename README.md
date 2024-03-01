# Кейс 1. Алгоритм для структурирования резюме



## Реализованно

- Поиск основной информации о сотрудкине
- JSON генератор
- архетиктура для расширения

Ссылка на скринкаст работы программы:
https://drive.google.com/file/d/1D0flAq_7YOdPGvWY5ARRePNjOYKpvvU9/view?usp=drivesdk


Как пользоваться:

### Первый шаг
Устанавливаем библиотеки, используя команду pip install:

1) PyPDF2
2) pdfminer.six
3) pdfplumber
4) pdf2image
5) Pillow
6) pytesseract (Для того, чтобы он корректно работал на Windows неоходимо скачать и установить файл exe по ссылке https://linuxhint.com/install-tesseract-windows/) а также для корректной работы отдельно установить poppler и поместить его по пути (C:\Program Files)
7) python-docx


### Второй шаг
```sh
def main():
    text = FileReader("ПУТЬ ДО ФАЙЛА").Read()
```
### Третий шаг
Запускаете программу и переходите в созданный json файл
