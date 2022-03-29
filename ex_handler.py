# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 07:42:44 2022

@author: prate
"""

def ex_handler(l,a):
    while True:
        try:
            choice=int(input(a))
        except:
            print("invalid input")
            continue
        if choice not in l:
            print("invalid input")
            continue
        break
    return choice