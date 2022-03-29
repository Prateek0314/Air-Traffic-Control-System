# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 06:37:55 2022

@author: prate
"""

#creator and deletion modules to create structure and data in sql
import mysql.connector as sqlconnect

#connection
con=sqlconnect.connect(host="localhost",user="root",passwd="password")

if con.is_connected():
    True

cursor=con.cursor()


def createdb():
    cursor.execute("create database ATC;")

def createtables():
    cursor.execute("use ATC;")
    cursor.execute("create table groundtime (terminal varchar(2) primary key,north_terminal_runway_1 int(2),south_terminal_runway_1 int(2),north_terminal_runway_2 int(2),south_terminal_runway_2 int(2));")
    cursor.execute("create table flqueues (pos int(2),t1 varchar(6),t2 varchar(6),t3 varchar(6),t4 varchar(6),r1_takeoff varchar(6),r2_takeoff varchar(6),r1_landed  varchar(6),r2_landed varchar(6),approach varchar(6));")

def insertion():
    cursor.execute("use ATC;")
    cursor.execute("insert into groundtime values('t1',10,12,5,25);")
    cursor.execute("insert into groundtime values('t2',20,10,7,15);")
    cursor.execute("insert into groundtime values('t3',15,7,10,20);")
    cursor.execute("insert into groundtime values('t4',30,7,17,5);")

    #for inserting flnos
    for i in range(5):
        a='insert into flqueues values('+str(i+1)+','
        for j in range(9):
            if j!=8:
                a+="'"+FLNO_generator.plane_gen()+"'"+','
            else:
                a+="'"+FLNO_generator.plane_gen()+"'"+');'
        cursor.execute(a)
    a="null,"*8
    b='insert into flqueues values(6,'+a+'null);'
    cursor.execute(b)
    con.commit()

def deletedb():
    cursor.execute("drop database ATC;")