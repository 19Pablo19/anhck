from flask import Flask, render_template, request

app = Flask(__name__)

users = [{"Pilar": "123"},
         {"Marcos": "123"}]

# Example for the login
# for user in range(len(users)):
#     if "Pilar" in users[user]:
#         print("SIUUH")
#     else:
#         print("NOP")


questions = [{"": ""},
             {"": ""}]



@app.route('/login', methods=['POST'])
def index(name, password):
    for user in range(len(users)):
        if name in users[user] and users[user][name]:
            return render_template('index.html', user=name, password=passsword)
        else:
            return print("User or password incorrect")



@app.route("/echo", methods=['POST'])
def echo():
    return "You said: " + request.form['text']



if __name__ == '__main__':
    app.run(host='0.0.0.0')
