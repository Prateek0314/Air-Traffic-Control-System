#modulw to display main menu 
import Create,time,os,ex_handler
import mysql.connector as sqlconnect


#connection
con=sqlconnect.connect(host="localhost",user="root",passwd="password",database="ATC")

if con.is_connected():
    True

cursor=con.cursor()

def main_menu():
    print("\t\t\t\t\t  Air Traffic Control System \n\n\t\t\t\t\t      1.Continue\n\t\t\t\t\t      2.New System\n \t\t\t\t\t      3.Exit\n\t\t\t\t\t      4.Install system\n\t\t\t\t\t      5.Uninstall system and exit")
    time.sleep(1)
    print("\t\t\t     Enter all choices in numbers unless otherwise prompted to \n\n")
    l=[1,2,3,4,5]
    
    while True:
        try:
            choice=int(input("Enter: "))
        except:
            print("invalid input enter a number")
            continue
        
        if choice not in l:
            print("invalid input")
            continue
        break
   
    if choice==3:
        print("Closing appication",end='')
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print('.',end='')
        os._exit(0)
        
    elif choice==2:
        a='show databases like \'ATC\';'
        cursor.execute(a)
        data=cursor.fetchall()
        
        if data==[]:
            print("Are you sure you want to remove the current system?(y/n)")
            l=["y","n"]
            c=ex_handler.ex_handler(l,a)
            
            if c=="n":
                main_menu()
            
            elif c=="y":
                print("Deleting old data",end='')
                time.sleep(0.5)
                print('.',end='')
                time.sleep(0.5)
                print('.',end='')
                time.sleep(0.5)
                print('.',end='')
                
        Create.deletedb()
        Create.createdb()
        Create.createtables()
        print("Initializing",end='')
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print()
        Create.insertion()
    
    elif choice==4:
        
        a='show databases like \'ATC\';'
        cursor.execute(a)
        data=cursor.fetchall()
        
        if data!=[]:
            print("System already installed, choose another option: \n\n\n")
            main_menu()
            

        Create.createdb()
        Create.createtables()
        print("Installing",end='')
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print()
        Create.insertion()
    
    elif choice==5:
        a='show databases like \'ATC\';'
        cursor.execute(a)
        data=cursor.fetchall()
        
        if data!=[]:
            Create.deletedb()
            
        print("Uninstalling",end='')
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print('.',end='')
        os._exit(0)
