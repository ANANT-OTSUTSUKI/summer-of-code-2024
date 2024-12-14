from flask import Flask,render_template,redirect,request,url_for
from flask_login import UserMixin,LoginManager,login_user,logout_user,current_user,login_required
import psycopg2
from admin import admin
from staff import staff
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key="hello motto"

app.config['SESSION_PERMANENT'] = False
app.config['REMEMBER_COOKIE_DURATION'] = 0

app.register_blueprint(admin)
app.register_blueprint(staff)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost:5432/week2_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager=LoginManager(app)
login_manager.login_view='products'

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    usern=db.Column(db.String(100),primary_key=True)
    pwd=db.Column(db.String(100))
    role=db.Column(db.String(10))

    def get_id(self):
        return self.usern
    def __init__(self, usern):
        self.usern = usern

    
@login_manager.user_loader
def load_user(usern):
    return User.query.filter_by(usern=usern).first()



def db_conn():
    conn = psycopg2.connect(database = "week2_db", host="localhost", user="postgres", password="12345678", port="5432")
    return conn


@app.errorhandler(404)
def not_found(error):
    return "PAGE NOT FOUND"

@app.errorhandler(500)
def internal_server(error):
    return "Internal server Error"


@app.route('/')
def index():
    return ('<a href = /products>PRODUCTS</a>')


@app.route('/products', methods=['get','post'])
def products():
    conn = db_conn()
    cur = conn.cursor()

    cur.execute('''SELECT * FROM products''')
    data = cur.fetchall()    
    conn.commit()
    cur.close()
    conn.close()

    return render_template('index.html',data=data)

@app.route('/products/admin_login')
def admin_login():
    if not current_user.is_authenticated:
        return render_template('admin_login.html')
    elif current_user.role == 'admin':
        return redirect(url_for('admin',sort='id'))
    elif current_user.role == 'staff':
        return redirect(url_for('staff'))
        
    

@app.route('/products/staff_login')
def staff_login():
    if not current_user.is_authenticated:
        return render_template('staff_login.html')
    elif current_user.role == 'admin':
        return redirect(url_for('admin',sort='id'))
    elif current_user.role == 'staff':
        return redirect(url_for('staff'))

@app.route('/products/Alogin',methods=['post'])
def Alogin():
    usern = request.form['a_user']
    pwd = request.form['a_pwd']

    user = User.query.filter_by(usern=usern,role='admin').first()
    
    if user and pwd==user.pwd:
        login_user(user)
        return redirect(url_for('admin',sort='id'))
    else:
        return redirect(url_for('admin_login'))
    


    
@app.route('/products/Slogin',methods=['post'])
def Slogin():
    usern = request.form['s_user']
    pwd = request.form['s_pwd']

    users = User.query.filter_by(usern=usern,role='staff').first()
    
    if users and pwd==users.pwd:
        login_user(users)
        return redirect(url_for('staff'))
    else:
        return redirect(url_for('staff_login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('products'))

@app.route('/products/admin')
@login_required
def admin():
    if current_user.role != 'admin':
        return redirect(url_for('products'))
    
    sort = request.args.get('sort')
    queri = f"SELECT * FROM products ORDER BY {sort}"
    conn=db_conn()
    cur=conn.cursor()
    cur.execute(queri)
    data = cur.fetchall()

    conn.commit()
    cur.close()
    conn.close()
    return render_template('admin.html',data=data,user=current_user)

@app.route('/products/staff')
@login_required
def staff():
    if current_user.role != 'staff':
        return redirect(url_for('products'))
    
    conn=db_conn()
    cur=conn.cursor()
    cur.execute('''SELECT * FROM products ORDER BY id''')
    data = cur.fetchall()

    conn.commit()
    cur.close()
    conn.close()
    return render_template('staff.html',data=data,user=current_user)



if __name__ == ('__main__'):
    app.run(debug="True", port=1224)
