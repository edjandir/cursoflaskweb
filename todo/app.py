from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Modelo do usuário
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']
        erros = []
        if len(name) < 2:
            erros.append('Nome deve ter pelo menos 2 caracteres')
        if  email.find('@') == -1:
            erros.append('Email inválido')
        if len(password1) < 8:
            erros.append('A senha deve ter pelo menos 8 caracteres')
        if password1 != password2:
            erros.append('As senhas devem ser iguais')
        
        if len(erros) > 0:
            return render_template('signup.html', erros=erros, name=name, email=email)
        else:
            user = User(name=name, email=email, password=password1)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home'))
    
    return render_template('signup.html')


def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    # import os
    # if not os.path.isfile(os.path.join(os.path.abspath(__file__), 'todo.db')):
    #     create_tables()
    create_tables()
    app.run(debug=True)