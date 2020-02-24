import urllib.request as ur
import re

url = "http://www.pythonchallenge.com/pc/def/ocr.html"


def main():
    global url

    response = ur.urlopen(url)
    body = response.read()

    text = re.search("<!--\n%(.|\s)+", body.decode())
    dic = {}
    # print(text.group(0))
    for x in text.group(0):
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1

    print(dic)
    for i in dic:
        if (dic[i] == 1 and 'a' <= i <= 'z'):
            print(i)


if __name__ == '__main__':
    main()
