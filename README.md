download postgreSQL. open folder and activate virtual environment and select python interpreter. open terminal and install flask and psycopg2 using pip. open psql and create database "week1_db"(using "create database week1_db;"). open init_db.py, app.py and change required fields like port,password etc accordingly. run init_db.py creates required tables in database week1_db. run app.py and open http://127.0.0.1:8000/ in browser to access and edit tables.

As per I understood the models, I linked the different models.

model validation: 
1.prices and quantity in Inventory are non negative. if user give input negative integers in price or quantity , error will show in terminal but entry won't be added in inventory.
2. contact number are of valid format are allowed. but format can be of any country.

custom model methods:
1. in inventory column calculated total value of items present in inventory is written.
2. quantity of items in inventory can be updated just by giving input the quantity is sold or purchased. 
  (ex - if 45 pens are in inventory and purchased  more pens so to update these 5 pens in inventory , give input +5 items, not 50)
