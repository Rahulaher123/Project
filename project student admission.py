import mysql.connector as m

mydatabase=m.connect(host="localhost",user="root",password="manager",database="pythondb1")
cursor=mydatabase.cursor()
#cursor.execute("create database python2")
#cursor.execute("create table student_data (roll_no int primary key auto_increment,std_name varchar(100),standard int,admission_year date default( now()))")


while True:
    print(" for new admission enter 1:","\n","delete student enter 2:","\n","update student data enter 3:","\n","show student enter 4:","\n","enter 0 for exit:","\n")
    process=int(input())
    if process==1:
        name=input("enter a name:")
        std=int(input("enter a standard:"))
        query="insert into student_data (std_name,standard) values(%s,%s)"
        cursor.execute(query,[name,std])
        query1="select roll_no from student_data where std_name=%s"
        cursor.execute(query1,[name])
        result=cursor.fetchall()
        print(result)
        print("your roll number is :",result[0][0])
        mydatabase.commit()
    elif process==2:
        roll_no=int(input("enter a roll number of student:"))
        query="delete from student_data where roll_no=%s"
        cursor.execute(query,[roll_no])
        mydatabase.commit()
        print("deleted successfully!!!")
    elif process==3:
    
    
        while True:
            print("to change name enter 1:","\n","to change roll_no enter 2:","\n","to change standard enter 3:","\n","to chnage admission year enter 4:","\n","enter 0 to exit or after complete process:")
            process1=int(input("enter a choice:"))
            if process1==1:
                roll_no=int(input("enter a roll no whose name is to change:"))
                name=input("enter a new name:")
                query="update student_data set std_name=%s where roll_no=%s"
                cursor.execute(query,[name,roll_no])
                mydatabase.commit()
                print("name changed successfully!!!")
                print("enter 0 to exit or enter 1 to continue:")
                p=int(input("enter  a choice:"))
                if p==0:
                    break
            if process1==2:
                name=input("enter a name whose roll has to be changed:")
                roll_no=int(input("enter a new roll number:"))
                query="update student_data set roll_no=%s where std_name=%s"
                cursor.execute(query,[roll_no,name])
                mydatabase.commit()
                print("roll number changed successfully!!!")
                print("enter 0 to exit or enter 1 to continue:")
                p=int(input("enter  a choice:"))
                if p==0:
                    break
            if process1==3:
                roll_no=int(input("enter a roll number whose standard has to be changed:"))
                std=int(input("enter new standard:"))
                query="update student_data set standard=%s where roll_no=%s"
                cursor.execute(query,[std,roll_no])
                mydatabase.commit()
                print("standard changed successfully!!!")
                print("enter 0 to exit or enter 1 to continue:")
                p=int(input("enter  a choice:"))
                if p==0:
                    break
            if process1==4:
                roll_no=int(input("enter a roll number whose admission year is to be changed"))
                year=input("enter a year in yy-mm-dd format:")
                query="update student_data set admission_year=%s where roll_no=%s"
                cursor.execute(query,[year,roll_no])
                mydatabase.commit()
                print("standard changed successfully!!!")
                print("enter 0 to exit or enter 1 to continue:")
                p=int(input("enter  a choice:"))
                if p==0:
                    break
            if process1==0:
                break
    elif process==4:
        roll_no=input("enter a roll number whose details you want:")
        query="select * from student_data where roll_no=%s"
        cursor.execute(query,[roll_no])
        result=cursor.fetchall()
        for i in result:
        
                print("roll number= ",i[0])
                print("name= ",i[1])
                print("std= ",i[2])
                print("admission year= ",i[3])
    elif process==0:
        break
    






