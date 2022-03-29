#module to grant permission to land
import cap_check,time
import mysql.connector as sqlconnect

#connection
con=sqlconnect.connect(host="localhost",user="root",passwd="password",database="ATC")

if con.is_connected():
    True

cursor=con.cursor()


def land():
    if cap_check.plane_check_remove("approach"):
        return True
    list_of_terminals=[1,2,3,4]
    a='select approach from ATC.flqueues;'
    cursor.execute(a)
    data=cursor.fetchall()
    l=[]
    for i in data:
        l.append(i[0])
    l2=l[1:]
    tk=l[0]
    #prompting user for runway on which to land
    r=''
    while True:
        x=input("Assign runway: ")
        if x=='back':
            return True
        elif int(x) not in list_of_terminals[:2]:
            print("invalid input")
            continue
        r='r'+x+'_landed'
        if cap_check.plane_check_add(r):
            print("Runway full, choose another runway")
            continue
        break
    #displaying that the plane is landing
    print(tk," landing",end='')
    time.sleep(0.3)
    print('.',end='')
    time.sleep(0.5)
    print('.',end='')
    time.sleep(0.5)
    print('.',end='')
    time.sleep(0.3)
    print()
    #removing plane from approach column
    m=0
    for i in range(len(l2)):
        if l2[i]==None:
            break
        a="update ATC.flqueues set approach='"+l2[i]+"' where pos="+str(i+1)+";"
        cursor.execute(a)
        m=i+2
    a="update ATC.flqueues set approach=null where pos="+str(m)+";"
    cursor.execute(a)
    #adding plane to runway on which it has landed
    a='select '+r+' from ATC.flqueues;'
    cursor.execute(a)
    data=cursor.fetchall()
    l=[]
    for i in data:
        l.append(i[0])
    fl=l.index(None)
    a="update ATC.flqueues set "+r+"='"+tk+"' where pos="+str(fl+1)+";"
    cursor.execute(a)
    con.commit()
