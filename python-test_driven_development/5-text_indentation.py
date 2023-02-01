#!/usr/bin/python3
""" print a text """


def text_indentation(text):
    """ print a text """
    if type(text) is not str:
        raise TypeError("text must be a string")
    x = 0
    for i in text:
        if x == 0:
            if i == ' ':
                continue
            else:
                x = 1
        if x == 1:
            if i == '.' or i == '?' or i == ':':
                print(i + '\n')
                x = 0
        print(i, end='')
