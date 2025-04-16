from flask import (Flask, render_template, request, redirect, 
    url_for, flash)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
app = Flask(__name__)

app.config['SECRET_KEY'] = 'IFSC2025'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Configuração do Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

#Modelo do usuário
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

#Modelo da tarefa
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    complete =db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
@login_required
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:
            flash('Usuário não existe!')
            return redirect(url_for('login'))
        if not check_password_hash(user.password, password):
            flash("Senha inválida!")
            return redirect(url_for('login'))
        
        login_user(user)
        return redirect(url_for('home'))
        
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
            senha_hash = generate_password_hash(password1)
            user = User(name=name, email=email, password=senha_hash)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home'))
    
    return render_template('signup.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    # import os
    # if not os.path.isfile(os.path.join(os.path.abspath(__file__), 'todo.db')):
    #     create_tables()
    create_tables()
    app.run(debug=True)