import mysql.connector as a
con=a.connect(host="localhost",user="root",password="groot",database="hotel")
c=con.cursor()
def acheckin():
    n=input("PERSON NAME:")
    c=input("ROOM NO:")
    r=input("CONTACT NO:")
    a=input("TIME_IN:")
    p=input("TIME_OUT:")
    x=input("DAYS_TO_RESIDE:")
    y=input("DATE:")
    data=(n,c,r,a,p,x,y)
    sql='insert into checkin values(%s,%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Succeessfully")
    print(">---------------------------------------<")
    main()    
def dcheckin():
    sql="select * from checkin"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print("PERSON_NAME:",i[0])
        print("ROOM_NO:",i[1])
        print("CONTACT_NO:",i[2])
        print("TIME_IN:",i[3])
        print("TIME_OUT:",i[4])
        print("DAYS_TO_RESIDE:",i[5])
        print("DATE:",i[6])
        print(">-----------------------------<")
    print(">-----------------------------<")
    main()
def fcheckin():
    name=input("NAME:")
    data=(name,)
    sql="select*from checkin where name =%s"
    c=con.cursor()
    c.execute(sql,data)
    d=c.fetchall()
    for i in d:
        print("NAME:",i[0])
        print("ROOM_NO:",i[1])
        print("CONTACT_NO:",i[2])
        print("TIME_IN:",i[3])
        print("TIME_OUT:",i[4])
        print("DAYS_RESIDED:",i[5])
        print("DATE:",i[6])
        print(">-----------------------------<")
    print(">-----------------------------<")
    main()
def main():
    print("""
                ---------->HOTEL MANAGEMENT SYSTEM<----------


                    
       1.ADD CUSTOMER DETAIL                  2.DISPLAY CUSTOMER LIST
                         3.SEARCH CUSTOMER DETAILS


       **NOTE:-
         1)ENTER THE DATE IN YEAR-DATE-MONTH FORMAT.
       

 """)
    
    choice=input("ENTER THE TASK NO:")
    print(">--------------------------<")
    if(choice=='1'):
       acheckin()
    elif(choice=='2'):
        dcheckin()
    elif(choice=='3'):
        fcheckin()
    else:
        print("WRONG CHOICE.............")
        main()
def pswd():
    p=input("PASSWORD:")
    if p=="12345":
        main()
    else:
        print("WRONG PASSWORD")
        pswd()
pswd() 

