from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def Index():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


# to run the app in debug mode, run ```flask --app app.py --debug run``` in the terminal