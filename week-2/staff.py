from flask import Blueprint,request,Flask,render_template,redirect,url_for
import psycopg2

staff = Blueprint('staff',__name__,template_folder='templates')
data_store={}

def db_conn():
    conn = psycopg2.connect(database = "week2_db", host="localhost", user="postgres", password="12345678", port="5432")
    return conn

@staff.route('/products/staff/update',methods=['post'])
def updateS():
    conn = db_conn()
    cur = conn.cursor()
    id = request.form['id']
    qty = request.form['qty']

    cur.execute('''UPDATE products SET qty=qty+%s WHERE id=%s''',(qty,id))

    conn.commit()
    cur.close()
    conn.close
    return redirect(url_for('staff'))