import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Salal@007',database='db1')
#OBTAINING CURSOR OBJECT
cobj=mydb.cursor()
#CREATING QUERY VARIABLE
insert_query="INSERT INTO book (bookid,title,price) VALUES(%s,%s,%s)"
data=[(5,'BUSINESS',120),(6,'ACCOUNTS',322),(7,'ENGLISH',671)]
cobj.executemany(insert_query,data)
mydb.commit()