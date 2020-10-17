# Set up your imports here!
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to this page!Go to /puppy_latin/name to see your puppy's name</h1>"

@app.route('/puppy_latin/<name>')
def puppylatin(name):
    if name[-1] != 'y':
        #newname = name + "y"
        return "<h1>Your puppy's latin name is {}</h1>".format(name + "y")
    else:
        #newname = name[:-1] + "iful"
        return "<h1>Your puppy's latin name is {}</h1>".format(name[:-1] + "iful")
    #return "<h1>Good day {}, you puppy's name is {}!</h1>".format(name,newname)

if __name__ == '__main__':
    app.run(debug=True)
