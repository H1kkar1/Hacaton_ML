import re


def find_info_regular(text, keywords, regular):
    for keyword in keywords:
        try:
            text = text.split(keyword)
            text = text[1].split('\n')[0]
            result = re.sub("['\t'|-|:|_]", '', text)
            result = re.search(regular, text).group()
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
