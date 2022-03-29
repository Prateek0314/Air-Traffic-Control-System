# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 07:42:11 2022

@author: prate
"""

#function to display list of planes at given place
import mysql.connector as sqlconnect

#connection
con=sqlconnect.connect(host="localhost",user="root",passwd="password",database="ATC")

if con.is_connected():
    True

cursor=con.cursor()

def display(place):
    cursor.execute("use ATC;")
    a="select "+place+" from flqueues;"
    cursor.execute(a)
    data=cursor.fetchall()
    k=1
    for i in data:
        if i[0]==None:
            break
        print(k,'',i[0])
        k+=1
