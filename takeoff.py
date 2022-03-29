# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 06:41:35 2022

@author: prate
"""

#module to grant permission to takeoff
import cap_check
import mysql.connector as sqlconnect

#connection
con=sqlconnect.connect(host="localhost",user="root",passwd="password",database="ATC")

if con.is_connected():
    True

cursor=con.cursor()


def takeoff(place):
    if cap_check.plane_check_remove(place):
        return True
    a='select '+place+' from ATC.flqueues;'
    cursor.execute(a)
    data=cursor.fetchall()
    l=[]
    for i in data:
        l.append(i[0])
    l2=l[1:]
    tk=l[0]
    
    #displaying that the plane is taking off
    print(tk," taking off from runway",place[1],end='')
    time.sleep(0.3)
    print('.',end='')
    time.sleep(0.5)
    print('.',end='')
    time.sleep(0.5)
    print('.',end='')
    time.sleep(0.3)
    print()
    
    #removing plane from database
    m=0
    for i in range(len(l2)):
        if l2[i]==None:
            break
        a="update ATC.flqueues set "+place+"='"+l2[i]+"' where pos="+str(i+1)+";"
        cursor.execute(a)
        m=i+2
    a="update ATC.flqueues set "+place+"=null where pos="+str(m)+";"
    cursor.execute(a)
    con.commit()
    
    #adding new plane to approach
    a='select approach from ATC.flqueues;'
    cursor.execute(a)
    data=cursor.fetchall()
    l=[]
    for i in data:
        l.append(i[0])

    if plane_check_add("approach")==False:
        f=l.index(None) 
        if f==5:
            print("Approach limit reached grant permission to land before continuing")
        fln=FLNO-generator.plane_gen()
        a="update ATC.flqueues set approach='"+fln+"' where pos="+str(f+1)+";"
        cursor.execute(a)
        con.commit()