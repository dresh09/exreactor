import re

#The welcome message
print('''Welcome to @Dresh09 email extractor,
please paste your clipboard in input.txt to extractor emails''')

def emailReg():
    fi = open('input.txt', 'r', encoding='utf_8')
    fo = open('result.txt', 'a')

    for line in fi :
        pattern = re.compile('[a-zA-Z0-9\-\.]+@[a-zA-Z0-9\-\.]+\.[a-zA-Z0-9]+')
        result = pattern.findall(line)
        for i in result:
            print('extracted =>', i)
            print(i, file = fo)
    print('Done')
emailReg()
