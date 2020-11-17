from flask import Flask, render_template, flash, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class SimpleForm(FlaskForm):

    breed = StringField('What breed is your puppy?')
    submit = SubmitField('submit')

@app.route("/", methods=['GET','POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        session['breed']=form.breed.data
        flash(f"Your puppy is: {session['breed']}")
        return redirect(url_for('index'))
    return render_template("home.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
