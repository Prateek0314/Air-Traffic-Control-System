#importing library modules

import mysql.connector as sqlconnect

import time 

#importing program modules
import display,ex_handler,Landing,main_menu,rw_assign,takeoff,term_assign


#============================================================================================================================================================================================================

#connection
con=sqlconnect.connect(host="localhost",user="root",passwd="password")
if con.is_connected():
    print("loading",end='')
    time.sleep(0.5)
    print('.',end='')
    time.sleep(0.5)
    print('.',end='')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)   
cursor=con.cursor()


       
          
#============================================================================================================================================================================================================

#main
main_menu.main_menu()        


while True:
    print("choose: ")
    print("1.terminal 1 \n2.terminal 2 \n3.terminal 3 \n4.terminal 4 \n5.Planes taking off \n6.planes landed\n7.planes approaching\n8.main menu")

#    choice=int(input("enter choice: "))
    l=[1,2,3,4,5,6,7,8]
    choice=ex_handler.ex_handler(l,"enter choice: ")
    if choice==8:
        main_menu()
        continue

    elif choice<5:
        if choice==1:
            display.display('t1')
            time.sleep(0.5)
            t=input("assign runway to plane?(y/n): ")
            if t=='n':
                continue
            rw_assign.assign_runw("t1")

        elif choice==2:
            display.display('t2')
            time.sleep(0.5)
            t=input("assign runway to plane?(y/n): ")
            if t=='n':
                continue
            rw_assign.assign_runw("t2")

        elif choice==3:
            display.display('t3')
            time.sleep(0.5)
            t=input("assign runway to plane?(y/n): ")
            if t=='n':
                continue
            rw_assign.assign_runw("t3")

        elif choice==4:
            display.display('t4')
            time.sleep(0.5)
            t=input("assign runway to plane?(y/n): ")
            if t=='n':
                continue
            rw_assign.assign_runw("t4")
        
    elif choice==5:
        print("1.runway 1 \n2.runway 2")
        c=int(input("enter runway: "))
        if c==1:
            display.display("r1_takeoff")
            time.sleep(0.5)
            t=input("grant permission to takeoff?(y/n): ")
            if t=='n':
                continue
            takeoff.takeoff('r1_takeoff')

        if c==2:
            display.display("r2_takeoff")
            time.sleep(0.5)
            t=input("grant permission to takeoff?(y/n): ")
            if t=='n':
                continue
            takeoff.takeoff('r2_takeoff')

    elif choice==6:
        print("1.runway 1 \n2.runway 2")
        c=int(input("enter runway: "))
        if c==1:
            display.display("r1_landed")
            time.sleep(0.5)
            t=input("assign terminal to plane?(y/n): ")
            if t=='n':
                continue
            a=term_assign.assign_term("r1_landed")

        elif c==2:
            display.display("r2_landed")
            time.sleep(0.5)
            t=input("assign terminal to plane?(y/n): ")
            if t=='n':
                continue
            a=term_assign.assign_term("r2_landed")

    elif choice==7:
        display.display("approach")
        time.sleep(0.5)
        t=input("grant permission to land?(y/n): ")
        if t=='n':
            continue
        Landing.land()
    
    else:
        print("invalid input")
        continue        

