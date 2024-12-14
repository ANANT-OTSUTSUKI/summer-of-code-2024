from flask import Blueprint,request,Flask,render_template,redirect,url_for
import psycopg2
from flask_sqlalchemy import SQLAlchemy

admin = Blueprint('admin',__name__,template_folder='templates')

def db_conn():
    conn = psycopg2.connect(database = "week2_db", host="localhost", user="postgres", password="12345678", port="5432")
    return conn
db=SQLAlchemy()
class User(db.Model):
    __tablename__ = 'users'
    usern=db.Column(db.String(100),primary_key=True)
    pwd=db.Column(db.String(100))
    role=db.Column(db.String(10))

    def get_id(self):
        return self.usern
    def __init__(self, usern):
        self.usern = usern


@admin.route('/products/admin/create',methods=['post'])
def createA():
    conn = db_conn()
    cur = conn.cursor()
    name = request.form['name']
    descr = request.form['descr']
    price = request.form['price']
    qty = request.form['qty']

    cur.execute('''INSERT INTO products(name,descr,price,qty) VALUES(%s,%s,%s,%s)''',(name,descr,price,qty))
    conn.commit()
    cur.close()
    conn.close
    return redirect(url_for('admin',sort='id'))

@admin.route('/products/admin/delete', methods=['post'])
def deleteA():
    conn = db_conn()
    cur = conn.cursor()
    id = request.form['id']
    cur.execute('''DELETE FROM products WHERE id=(%s)''',(id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('admin',sort='id'))

@admin.route('/products/admin/update', methods=['post'])
def UpdateA():
    conn=db_conn()
    cur=conn.cursor()
    name = request.form['name']
    descr = request.form['descr']
    price = request.form['price']
    qty = request.form['qty']
    id = request.form['id']

    cur.execute('''UPDATE products SET (name,descr,price,qty) = (%s,%s,%s,%s) WHERE id=(%s)''',(name,descr,price,qty,id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('admin',sort='id'))



