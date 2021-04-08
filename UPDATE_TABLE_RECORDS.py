import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Salal@007',database='db1')
#OBTAINING CURSOR OBJECT
cobj=mydb.cursor()
#CREATING QUERY VARIABLE
update_query="UPDATE book SET price=price-10 WHERE price>200"
#EXECUTING THE QUERY
cobj.execute(update_query)
#UPDATING THE DATABASE
mydb.commit()