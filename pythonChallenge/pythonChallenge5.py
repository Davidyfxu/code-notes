import urllib.request as ur
import pickle


url = "http://www.pythonchallenge.com/pc/def/banner.p"


def main():
    global url

    httpresponse = ur.urlopen(url)
    dataBytes = httpresponse.read()

    obj = pickle.loads(dataBytes)
    # print(obj)
    for ele in obj:
        # print(ele)
        s = ""
        for i in ele:
            # print(i)
            # print(i[0]*i[1])
            s += i[0]*i[1]
        print(s)


if __name__ == '__main__':
    main()
