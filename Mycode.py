import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',passwd='monty1994',database='telusko')

mycursor = mydb.cursor()

mycursor.execute("select * from student")

result = mycursor.fetchone()

for i in result:
    print(i)