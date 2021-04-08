import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Salal@007',database='db1')
#OBTAINING CURSOR OBJECT
cobj=mydb.cursor()
#CREATING QUERY VARIABLE
show_query="SELECT * FROM book"
cobj.execute(show_query)
result=cobj.fetchall()
for rec in result:
    print(rec)