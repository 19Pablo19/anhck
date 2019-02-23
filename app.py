from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/<name>')
def index(name):
    return render_template('index.html', name=name)


@app.route("/echo", methods=['POST'])
def echo():
    return "You said: " + request.form['text']



if __name__ == '__main__':
    app.run(host='0.0.0.0')
