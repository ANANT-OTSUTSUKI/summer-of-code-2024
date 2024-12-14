import psycopg2

conn = psycopg2.connect(database = "week2_db", host="localhost", user="postgres", password="12345678", port="5432")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS products(id serial PRIMARY KEY, name varchar(100), descr varchar(500), price integer, qty integer);''')
cur.execute('''INSERT INTO products(name,descr,price,qty) VALUES('Pen','Stationary',10,10),('Pencil','Stationary',5,20)''')

cur.execute('''CREATE TABLE IF NOT EXISTS users(usern varchar(100) UNIQUE, pwd varchar(100),role varchar(10));''')
cur.execute('''INSERT INTO users(usern,pwd,role) VALUES('msd007','hello','staff'),('ronaldo007','hii','staff'),('anant','iamadmin','admin'),('week2','project','admin')''')

conn.commit()
cur.close()
conn.close()