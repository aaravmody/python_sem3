import mysql.connector as ms

myconn=ms.connect(host="localhost",user="root",password="12345678")
print(myconn)

c=myconn.cursor()

c.execute("Create database pytest")
print("done")

c.execute("use pytest")

c.execute("create table student(name varchar(20))")


c.execute("insert into student values('aarav')")
print("okay")

c.execute("insert into student values('deev')")

c.execute("insert into student values('virat')")

c.execute("select * from student")
result=c.fetchall()
for row in result:
    print(row)

c.execute("Drop database pytest")

c.execute("show databases")
result=c.fetchall()
for row in result:
    print(row)
