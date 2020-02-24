import urllib.request as ur
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022"


def main():
    global url
    global body
    while 1:
        print(url)
        response = ur.urlopen(url)
        # print(type(response))

        body = response.read()
        # print(type(body))
        # print(body)
        # print(body.decode())

        pattern = "and the next nothing is ([0-9]+)"
        # match从string的开头查找
        # search从string的anywhere开始找
        result = re.search(pattern, body.decode())
        if result:
            num = result.group(1)
            print(result.group(0))
            print(num)
            url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % num
        else:
            # print(type(result),result)
            break
    print(body)


if __name__ == '__main__':
    main()
