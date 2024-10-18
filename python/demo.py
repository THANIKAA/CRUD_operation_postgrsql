import psycopg2
import psycopg2.extras
hostnamme='localhost'
portid =5432
username='postgres'
database='Demo'
owner='postgres'
pwd='Blue0ce@n'
conn=None
try:
  with psycopg2.connect(
                host=hostnamme,
                dbname=database,
                user=username,
                password=pwd,
                port=portid

   ) as conn:
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute('DROP TABLE IF EXISTS employee')
        create_script=''' CREATE TABLE IF NOT EXISTS employee(
                                    id int PRIMARY KEY,
                                    name  varchar(40) NOT NULL, 
                                    salary int,
                                    dept_id varchar(30))'''
        cur.execute(create_script)
        insert_script='INSERT INTO employee(id,name,salary,dept_id)VALUES(%s,%s,%s,%s)'
        insert_value = [(1,'James',1200,'D1'),(2,'Hames',2000,'D2'),(3,'Xavier',3000,'D2'),(4,'Robin',4000,'D3')]
        for record in insert_value:
                cur.execute(insert_script,record)
        update_script='UPDATE employee SET salary =salary*(salary * 0.5)'
        cur.execute(update_script)
        cur.execute('SELECT * FROM employee')
        for cord in cur.fetchall():
                print(cord['salary'])
        delete_script='DELETE FROM employee WHERE name=%s'
        delete_value=('James',)
        cur.execute(delete_script,delete_value)
except Exception as error:
   print(error)
finally:
    if conn is not None:
        conn.close()