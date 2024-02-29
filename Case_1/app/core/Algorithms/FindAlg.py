import re

def find_info_regular(text, keywords, regular):
    for keyword in keywords:
        print(keyword)
        try:
            text = text.split(keyword)
            print(text)
            text = text[1].split('\n')[0]
            print(text)
            result = re.sub("['\t'|-|:|_]", '', text)
            print(result)
            result = re.search(regular, text).group()
            print(result)

            return result
        except Exception:
            string = ""
    return string


def find_info(text, keywords):
    for keyword in keywords:
        try:
            text = text.split(keyword)
            text = text[1].split('\n')[0]
            return re.sub("[' '|-|:|_]", '', text)
        except IndexError:
            string = ""
        return string
