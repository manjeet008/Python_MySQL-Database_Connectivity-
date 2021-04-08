import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Salal@007',database='db1')
#OBTAINING CURSOR OBJECT
cobj=mydb.cursor()
#CREATING QUERY VARIABLE
insert_query="INSERT INTO book (bookid,title,price) VALUES(%s,%s,%s)"
Range=int(input("ENTER HOW MANY TIMES DO YOU ENTER THE DATA... "))
for i in range(0,Range):
    book_id=i
    book_name=input("\nENTER BOOK NAME... ")
    book_price=int(input("\nENTER BOOK PRICE... "))
    #CREATING TUPLE
    data=(book_id,book_name,book_price)
    cobj.execute(insert_query,data)
mydb.commit()