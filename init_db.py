import psycopg2

conn = psycopg2.connect(database = "week1_db", host="localhost", user="postgres", password="12345678", port="5432")

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS customers(c_id serial PRIMARY KEY, c_name varchar(100) , c_mail varchar(100) UNIQUE , c_contact VARCHAR(13) CONSTRAINT valid_phone CHECK (c_contact ~ '^\+?[0-9\s\-()]+$')  UNIQUE);''')

cur.execute('''CREATE TABLE IF NOT EXISTS staffs(s_id serial PRIMARY KEY, s_name varchar(100) , s_mail varchar(100)  UNIQUE ,s_isAdmin varchar(10), s_contact VARCHAR(13) CONSTRAINT valid_phone CHECK (s_contact ~ '^\+?[0-9\s\-()]+$') UNIQUE);''')

cur.execute('''CREATE TABLE IF NOT EXISTS inventory(item_sku serial PRIMARY KEY,s_id integer , item_name varchar(100), item_desc varchar(1000), item_price integer , item_qty integer , FOREIGN KEY (s_id) REFERENCES staffs(s_id));''')

cur.execute('''CREATE TABLE IF NOT EXISTS transactions(t_id serial PRIMARY KEY, c_id integer , s_id integer , t_amount integer , t_desc varchar(500), FOREIGN KEY (c_id) REFERENCES customers(c_id), FOREIGN KEY (s_id) REFERENCES staffs(s_id));''')

cur.execute('''INSERT INTO staffs (s_name,s_mail,s_isAdmin,s_contact) VALUES(%s,%s,%s,%s)''',("Anant","anant@iitd.ac.in","YES","7690869544"))
cur.execute('''INSERT INTO customers (c_name,c_mail,c_contact) VALUES ('Ram','ram@gmail.com','9632587411'),('shyam','shyam@hotmail.com','8747456123')''')
cur.execute('''INSERT INTO inventory (s_id,item_name,item_desc,item_price,item_qty) VALUES (1,'Pen','BLUE INK PEN',10,40)''')
conn.commit()

cur.close()
conn.close()