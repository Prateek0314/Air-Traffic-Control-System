#module to assign runway for takeoff to plane at terminal
import mysql.connector as sqlconnect
import time,cap_check

#connection
con=sqlconnect.connect(host="localhost",user="root",passwd="password",database="ATC")

if con.is_connected():
    True

cursor=con.cursor()

def assign_runw(term):
    if cap_check.plane_check_remove(term):
        return True
    list_of_terminals=[1,2,3,4]
    a='select '+term+' from ATC.flqueues;'
    cursor.execute(a)
    data=cursor.fetchall()
    l=[]
    for i in data:
        l.append(i[0])
        print()
    l2=l[1:]
    tk=l[0]
    x=0
    r=''
    while True:
        x=input("Assign runway: ")
        if x=='back':
            return True
        elif int(x) not in list_of_terminals[:2]:
            print("invalid input")
            continue
        r='r'+x+'_takeoff'
        if cap_check.plane_check_add(r):
            print("Runway full, choose another runway")
            continue
        break
    #displaying that plane is moving to terminal
    print(tk," moving to runway",x,end='')
    time.sleep(0.3)
    print('.',end='')
    time.sleep(0.5)
    print('.',end='')
    time.sleep(0.5)
    print('.',end='')
    time.sleep(0.3)
    print()
    #adding plane to runway
    a='select '+r+' from ATC.flqueues;'
    cursor.execute(a)
    data=cursor.fetchall()
    l3=[]
    for i in data:
        l3.append(i[0])
    
    empt=l3.index(None)
    a="update ATC.flqueues set "+r+"='"+tk+"' where pos="+str(empt+1)+";"
    cursor.execute(a)
    con.commit()
    m=0
    if l2[0]==None:
        a="update ATC.flqueues set "+term+"=null where pos=1;"
        cursor.execute(a)    
        con.commit()
        
    for i in range(len(l2)):
        if l2[i]==None:
            break
        a="update ATC.flqueues set "+term+"='"+l2[i]+"' where pos="+str(i+1)+";"
        m=i+2
        cursor.execute(a)    
    a="update ATC.flqueues set "+term+"=null where pos="+str(m)+";"
    cursor.execute(a)    
    con.commit()
