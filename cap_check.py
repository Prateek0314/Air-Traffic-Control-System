#capacity checker
import mysql.connector as sqlconnect

#connection
con=sqlconnect.connect(host="localhost",user="root",passwd="password",database="ATC")

if con.is_connected():
    True

cursor=con.cursor()
#checking if given place has any planes
def plane_check_remove(place):
    a='select '+place+' from ATC.flqueues;'
    cursor.execute(a)
    data=cursor.fetchall()
    l=[]
    for i in data:
        l.append(i[0])
    if None in l:
        if l.index(None)==0:
            print("No planes present")
            return True
    return False

#function to check if there is space to assign plane to place
def plane_check_add(place):
    a='select '+place+' from ATC.flqueues;'
    cursor.execute(a)
    data=cursor.fetchall()
    l=[]
    for i in data:
        l.append(i[0])
    if None not in l:
            return True
    return False
