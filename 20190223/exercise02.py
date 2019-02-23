'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
test_str='We Are Happy.'

'''
Python的强大之处，一行爆菊大法，直接调string内置的replace()函数,
第一个参数为old string，第二个为要替换的字符串
'''
def replaceSpace(s):
    return s.replace(" ","%20")


if __name__ == '__main__':
    str=replaceSpace(test_str)
    print(str)