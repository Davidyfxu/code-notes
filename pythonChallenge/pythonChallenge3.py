import urllib.request as ur
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"


def main():
    response = ur.urlopen(url)
    body = response.read()

    # [^A-Z]表示不是A-Z的字母的字符
    pattern = "[^A-Z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][^A-Z]"

    result = re.findall(pattern, body.decode())
    print(result)


if __name__ == '__main__':
    main()
