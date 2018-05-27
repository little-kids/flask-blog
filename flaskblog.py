from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '1752fdb6f887ea1957b58a604f5c9875'

posts = [
    {
        'author': 'Dat Nguyen',
        'title': 'Blog post 1',
        'content': 'First blog post',
        'date_posted': 'May 24, 2018'
    },
    {
        'author': 'Nguyen Dat',
        'title': 'Blog post 2',
        'content': 'Second blog post',
        'date_posted': 'May 25, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'dat@gmail.com' and form.password.data == '123123':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)











if __name__ == "__main__":
    app.run(debug=True)
