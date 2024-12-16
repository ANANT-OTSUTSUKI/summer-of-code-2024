Admin:-  (username,password)=(anant,iamadmin),(admin,admin)
Staff:- (username,password) = (msd007,hello),(ronaldo007,hii)

download postgreSQL. open folder and activate virtual environment and select python interpreter. open terminal and install flask,flask-login,flask-sqlalchemy and psycopg2 using pip. open psql and create database "week2_db"(using "create database week2_db;"). open init_db.py, app.py,admin.py and staff.py and change required fields like port,password etc accordingly. run init_db.py which creates required tables in database week2_db. run app.py and open http://127.0.0.1:1224/ in browser to open the application

in this application, CRUD operations are implemented.Blueprints are made for code to be simpler.Admins and staffs has seperare.UPdate form is given for admin to update product table. Different role and permissions are assigned to ADMIN,STAFF and USER.Login pages are created for admin and staff to login.
Admin can perform  any CRUD Operation to Products table like read tableadd a new item to table, delete a item , and update the table.
Staff can read product table and can update the quantities of products (updating prices etc are permitted to admins only).
User (Customer) can only read the product table.

1. ADvanced CRUD Operation - Admin can Sort Product table on various basis like ID, Prices, Qty etc.
2. Testing - CRUD Operations were mainly be accessed in admin interface, which required login so I was not able to test CRUD Operations and API endpoints using pytest
3. Error Handling - error hadnling mechanisms for respomses like 404 not found, 500 internal server error aur implemented using flask error handlers.
