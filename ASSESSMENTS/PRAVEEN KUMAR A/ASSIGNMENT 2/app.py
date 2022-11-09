from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id

    with app.app_context():
        db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        userName = request.form.get('name')
        userEmail = request.form.get('email')
        userPwd = request.form.get('password')

        newUser = Users(email=userEmail, name=userName, password=userPwd)
        
        try:
            db.session.add(newUser)
            db.session.commit()
            return redirect('/')
        except:
            return redirect('/')

    else:
        return render_template('signup.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)