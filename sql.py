import sqlite3
con=sqlite3.connect('employee.db')
c=con.cursor()
#c.execute("""CREATE TABLE employees ( 
#       last text,
#       pay integer
#       )""")
#c.execute("INSERT INTO employees VALUES ('ziag','moh',20)")  
c.execute("SELECT * FROM employees WHERE pay=20")  
print(c.fetchone())     
con.commit()
con.close()        