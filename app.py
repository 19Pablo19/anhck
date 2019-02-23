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


@app.route('/index')
def index():
    return render_template('index.html')




@app.route('/form', methods=['POST'])
def form():
    userF = request.form['user']
    passwordF = request.form['password']
    print(userF)
    for user in range(len(users)):
        if userF in users[user] and users[user][userF] == passwordF:
            return render_template('form.html', user=userF)
        else:
            return render_template('index.html')






if __name__ == '__main__':
    app.run(host='0.0.0.0')
