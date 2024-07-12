from flask import Flask, request, render_template
from werkzeug.security import generate_password_hash
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

@app.route('/')
def register_form():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_user():
    name = request.form['name']
    surname = request.form['surname']
    email = request.form['email']
    password = generate_password_hash(request.form['password'])

    # Сохранение данных в базе данных
    new_user = User(first_name=name, last_name=surname, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
 

    return 'Пользователь зарегистрирован успешно!'

if __name__ == '__main__':
  
  
    app.run(debug=True)
    