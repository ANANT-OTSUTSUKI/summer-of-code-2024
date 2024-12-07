import psycopg2
from psycopg2 import IntegrityError
from flask import Flask, render_template,redirect,request,url_for

app = Flask(__name__)

def db_conn():
    conn = psycopg2.connect(database = "week1_db", host="localhost", user="postgres", password="12345678", port="5432")
    return conn



@app.route('/')
def index():
    conn = db_conn()
    cur = conn.cursor()

    cur.execute('''SELECT * FROM customers ORDER BY c_id''')
    c_data = cur.fetchall()

    cur.execute('''SELECT * FROM transactions ORDER BY t_id''')
    t_data = cur.fetchall()

    cur.execute('''SELECT * FROM inventory ORDER BY item_sku''')
    i_data = cur.fetchall()

    sum=0
    for row in i_data:
        sum = sum+(row[4]*row[5])
    cur.execute('''SELECT * FROM staffs ORDER BY s_id''')
    s_data = cur.fetchall()

    cur.close()
    conn.close()
    return render_template('index.html', c_data= c_data, t_data=t_data, i_data=i_data,s_data=s_data, sum=sum)


#CUSTOMERS
@app.route('/create_customers', methods=['POST'])
def create_customers():
    conn = db_conn()
    cur = conn.cursor()
    c_name = request.form['c_name']
    c_mail = request.form['c_mail']
    c_contact = request.form['c_contact']
    cur.execute('''INSERT INTO customers (c_name ,c_mail ,c_contact  ) VALUES(%s,%s,%s)''',(c_name,c_mail,c_contact))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update_customers', methods=['POST'])
def update_customers():
    conn = db_conn()
    cur = conn.cursor()
    c_name = request.form['c_name']
    c_mail = request.form['c_mail']
    c_contact = request.form['c_contact']
    c_id = request.form['c_id']

    cur.execute('''UPDATE customers SET c_name =%s,c_mail  =%s,c_contact  =%s WHERE c_id=%s''',(c_name,c_mail,c_contact,c_id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

#TRANSACTIONS
@app.route('/add_transactions', methods=['POST'])
def add_transactions():
    conn = db_conn()
    cur = conn.cursor()
    c_id = request.form['c_id']
    s_id = request.form['s_id']
    t_amount = request.form['t_amount']
    t_desc = request.form['t_desc']
    try:
        cur.execute('''INSERT INTO transactions (c_id ,s_id,t_amount ,t_desc) VALUES(%s,%s,%s,%s)''',(c_id,s_id ,t_amount ,t_desc))
        conn.commit()
    except IntegrityError as e:
        conn.rollback() 
        print("Integrity error:", e)
    cur.close()
    conn.close()
    return redirect(url_for('index'))

#INVENTORY
@app.route('/add_item', methods=['POST'])
def add_item():
    conn = db_conn()
    cur = conn.cursor()
    item_name = request.form['item_name']
    item_desc = request.form['item_desc']
    item_price = request.form['item_price']
    item_qty = request.form['item_qty']
    s_id=request.form['s_id']
    
    try:
        if int(item_price)>=0 and int(item_qty)>=0:
            cur.execute('''INSERT INTO inventory (s_id,item_name ,item_desc,item_price,item_qty) VALUES(%s,%s,%s,%s,%s)''',(s_id,item_name ,item_desc,item_price,item_qty))
            conn.commit()
        else:
            print("PRICE and QUANTITY SHOULD BE POSITIVE")
    except IntegrityError as e:
        conn.rollback() 
        print("Integrity error:", e)
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update_qty',methods=['POST'])
def update_qty():
    conn = db_conn()
    cur = conn.cursor()
    item_sku = request.form['item_sku']
    qty_update = request.form['qty_update']

    cur.execute('''UPDATE inventory SET item_qty= item_qty+%s WHERE item_sku=%s''',(int(qty_update),item_sku))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

#STAFFS
@app.route('/create_staffs', methods=['POST'])
def create_staffs():
    conn = db_conn()
    cur = conn.cursor()
    s_name = request.form['s_name']
    s_isAdmin=request.form['s_isAdmin']
    s_mail = request.form['s_mail']
    s_contact = request.form['s_contact']
    cur.execute('''INSERT INTO staffs (s_name ,s_mail  ,s_isAdmin,s_contact  ) VALUES(%s,%s,%s,%s)''',(s_name,s_mail,s_isAdmin,s_contact))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update_staffs', methods=['POST'])
def update_staffs():
    conn = db_conn()
    cur = conn.cursor()
    s_name = request.form['s_name']
    s_isAdmin=request.form['s_isAdmin']
    s_mail = request.form['s_mail']
    s_contact = request.form['s_contact']
    s_id = request.form['s_id']
    
    cur.execute('''UPDATE staffs SET s_name =%s,s_mail  =%s,s_isAdmin=%s,s_contact  =%s WHERE s_id=%s''',(s_name,s_mail,s_isAdmin,s_contact,s_id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True,port=8000)
