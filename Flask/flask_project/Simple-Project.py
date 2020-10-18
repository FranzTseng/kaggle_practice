from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():

    lower_letter=False
    upper_letter=False
    end_num=False
    username = request.args.get('username')

    lower_letter=any(c.islower() for c in username)
    upper_letter=any(c.isupper() for c in username)
    end_num=username[-1].isdigit()

    report=lower_letter and upper_letter and end_num

    return render_template('report.html',report=report,lower_letter=lower_letter,
                           upper_letter=upper_letter, end_num=end_num)





    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    # Return the information to the report page html.
    pass

if __name__ == '__main__':
    app.run(debug=True)
