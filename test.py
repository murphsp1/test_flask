from flask import Flask, abort, redirect, render_template, request, session, url_for

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required


#Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

db = SQLAlchemy(app)

#Define models
roles_users = db.Table('roles_users',
                  db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                  db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary = roles_users,
                            backref=db.backref('users', lazy='dynamic'))


# Setup Flask Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


#Define forms

class NameForm(Form):
    name = StringField('What is your name?', validators = [Required()])
    submit = SubmitField('Submit')

#class LoginForm(Form):

#class Registration(Form):


# Create a user to test with
@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.create_user(email='murphsp1@gmail.com', password='password')
    db.session.commit()



# Views
@app.route('/')
@login_required
def index():
    return redirect('/login')

@app.route('/login', methods=['GET'])
def login_get():
    name = None
    form = NameForm()
    return render_template('login.html', form=form, name=name)


@app.route('/login', methods=['POST'])
def login_post():
    name = None
    form = NameForm()
    if form.validate():
        name = form.name.data
        form.name.data = ''
    return render_template('login.html', form=form, name=name)

@app.route('/registration', methods=['GET'])
def registration_get():
    return redirect(url_for('index'))


@app.route('/registration', methods=['PUT'])
def registration_put():
    return redirect(url_for('index'))






'''
@app.route('/user/<id>')
def get_user(id):
    user = id
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % id
'''


if __name__ == '__main__':
    app.run(debug = True)


    sys.exit(main())
