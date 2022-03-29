# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 06:39:55 2022

@author: prate
"""

#module to compute movement time from sql to python
import mysql.connector as sqlconnect

#connection
con=sqlconnect.connect(host="localhost",user="root",passwd="password",database="ATC")

if con.is_connected():
    True

cursor=con.cursor()


def time_taken(runway=1,terminal='t2',status='taxiingr'):
    cursor.execute("use ATC;")
    if status=='taxiingr':
        if runway==1:
                b="select south_terminal_runway_1 from groundtime where terminal='"+terminal+"';"
        else:
                b="select south_terminal_runway_2 from groundtime where terminal='"+terminal+"';"
    else:
        if runway==1:
                b="select north_terminal_runway_1 from groundtime where terminal='"+terminal+"';"
        else:
                b="select north_terminal_runway_2 from groundtime where terminal='"+terminal+"';"
    cursor.execute(b)
    data=cursor.fetchall()
    for i in data:
        return i[0]
