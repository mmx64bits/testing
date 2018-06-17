#!-*- coding: utf-8 -*-
import os

def welcome():
    print('------------')
    print('Hello there!')
    print('------------')

if __name__ == '__main__':
    welcome()
    for i in range(11):
        print('*' * i)

    os.system('PAUSE')
