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


questions = [{"¿En Horario?": ["Horario Lectivo",
                               "Actividad extraescolar",
                               "Actividad complementario"]},
             {"Suceso": [{"Pelea": ["Puñetazos",
                                    "Patadas",
                                    "Mordiscos",
                                    "Lanzamiento de objetos (bolígrafos, lápices, gomas, sillas, piedras…)"]},
                         "Caída (A mismo nivel de altura)",
                         "Precipitación (A nivel de altura diferente)",
                         "Muerte",
                         "Intoxicación alimentaria",
                         "Desmayo",
                         "Alergias",
                         "Plagas de piojos",
                         "Pérdida/ desaparición",
                         "Fuga/ escapada",
                         "Quemaduras",
                         "Destrucción de mobiliario",
                         "Asfixia"]},
            {"¿Quiénes han participado?": []},
            {"Resultado": ["Arañazos",
                           "Moratones",
                           "Rotura de huesos",
                           "Rotura de la vestimenta",
                           "Cortes",
                           "Puntos",
                           "Grapas"]}]




################################
######## INDEX #################
################################
@app.route('/index')
def index():
    return render_template('index.html')



################################
######## LOGIN #################
################################
@app.route('/form', methods=['POST'])
def form():
    userF = request.form['user']
    passwordF = request.form['password']
    print(userF)
    for user in range(len(users)):
        if userF in users[user] and users[user][userF] == passwordF:
            return render_template('form.html', user=userF)
        else:
            return index()


################################
######## FORM ##################
################################
@app.route('/report', methods=['POST'])
def report():
    #Coger las opciones elegidas
    respuesta1 = request.form[' ¿Dónde ha sucedido?']
    respuesta2 = request.form['Suceso']
    respuesta3 = request.form['¿Quiénes han participado?']
    respuesta4 = request.form[' Resultado:']
    respuesta5 = request.form['¿Ha sido necesaria asistencia médica?']
    respuesta6 = request.form['Esa asistencia ha sido']

    respuestas = [respuesta1, respuesta2, respuesta3, respuesta4, respuesta5, respuesta6]
    print(respuestas)
    file = open("report.txt", "w")
    for respuesta in respuestas:
        file.write("%s \n" % respuesta)
    file.close()
    return render_template('reports.py')

################################
######## ALL REPORTS ##################
################################
# @app.route('/allreports', methods=['POST'])
# def report():
#     #Coger las opciones elegidas
#     respuesta1 = request.form[' ¿Dónde ha sucedido?']
#     respuesta2 = request.form['Suceso']
#     respuesta3 = request.form['¿Quiénes han participado?']
#     respuesta4 = request.form[' Resultado:']
#     respuesta5 = request.form['¿Ha sido necesaria asistencia médica?']
#     respuesta6 = request.form['Esa asistencia ha sido']
#
#     respuestas = [respuesta1, respuesta2, respuesta3, respuesta4, respuesta5, respuesta6]
#     print(respuestas)
#     file = open("report.txt", "w")
#     for respuesta in respuestas:
#         file.write("%s \n" % respuesta)
#     file.close()
#     return render_template('allreports.py')






if __name__ == '__main__':
    app.run(host='0.0.0.0')
