#1 connecting to database
'''
import cx_Oracle

con = cx_Oracle.connect(' ce132/ce132@192.168.29.152/xe')
cur = con.cursor()
cur.execute("select sysdate from dual")

for result in cur:
 print(result)
con.close()
'''
#2 creating table

import cx_Oracle
con = cx_Oracle.connect('ce132/ce132@192.168.29.152/xe')
cur = con.cursor()
'''
cur.execute("""CREATE TABLE "test2" ( "id" NUMBER(10,0),
 "NAME" VARCHAR2(20 BYTE),
 "MNAME" VARCHAR2(20 BYTE),
 "LNAME" VARCHAR2(20 BYTE),
 "PHONE" VARCHAR2(20 BYTE),
 "CITY" VARCHAR2(10 BYTE)
 )""")

'''
cur.execute("""select table_name from all_tables""")
tab = cur.fetchall()
for i in range(50):
 print(tab)
con.commit()
con.close()


#3 Displaying data from table

'''
import cx_Oracle
con = cx_Oracle.connect('ce132/ce132@192.168.29.152/xe')
cur = con.cursor()
res = cur.fetchall()
for r in res:
 print(r)
'''