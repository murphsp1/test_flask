from flask import Flask, abort, redirect, render_template, request, session, url_for

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(Form):
    name = StringField('What is your name?', validators = [Required()])
    submit = SubmitField('Submit')


@app.route('/')
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
