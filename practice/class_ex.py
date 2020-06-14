#!/usr/bin/env python
# coding=utf8
class Calc:
    def sum(self,a,b):
        result=a+b
        print("{0} + {1} = {2} 입니다.".format(a,b,result))
    def sub(self,a,b):
        result=a-b
        print("{0} - {1} = {2} 입니다.".format(a,b,result))
    def mult(self,a,b):
        result=a*b
        print("{0} * {1} = {2} 입니다.".format(a,b,result))
    def div(self,a,b):
        result=a/b
        print("{0} / {1} = {2} 입니다.".format(a,b,result))