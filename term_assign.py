# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 06:42:38 2022

@author: prate
"""

#module to assign terminal planes that have just landed
import cap_check
import mysql.connector as sqlconnect

#connection
con=sqlconnect.connect(host="localhost",user="root",passwd="password",database="ATC")

if con.is_connected():
    True

cursor=con.cursor()

def assign_term(runway):
    if cap_check.plane_check_remove(runway):
        return True
    list_of_terminals=[1,2,3,4]
    a='select '+runway+' from ATC.flqueues;'
    cursor.execute(a)
    data=cursor.fetchall()
    l=[]
    for i in data:
        l.append(i[0])
    l2=l[1:]
    tk=l[0]
    x=0
    #prompting user for terminal to which to move the plane for disembarkment
    while True:
        print("1.t1 \n2.t2 \n3.t3 \n4.t4")
        x=input("Assign terminal: ")
        if x=='back':
            return True
        elif int(x) not in list_of_terminals:
            print("invalid input")
            continue
        t='t'+str(x)
        if cap_check.plane_check_add(t):
            print("Terminal full, choose another terminal")
            continue
        break
    print(tk," at ",t)
    a='select '+t+' from ATC.flqueues;'
    cursor.execute(a)
    data=cursor.fetchall()
    l3=[]
    for i in data:
        l3.append(i[0])
        print()
    
    empt=l3.index(None)
    a="update ATC.flqueues set "+t+"='"+tk+"' where pos="+str(empt+1)+";"
    cursor.execute(a)
    con.commit()
    m=0
    for i in range(len(l2)):
        if l2[i]==None:
            break
        a="update ATC.flqueues set "+runway+"='"+l2[i]+"' where pos="+str(i+1)+";"
        m=i+2
        cursor.execute(a) 
    a="update ATC.flqueues set "+runway+"=null where pos="+str(m)+";"
    cursor.execute(a)
    con.commit()