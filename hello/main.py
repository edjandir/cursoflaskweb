from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return '''<h1>Hello from Flask!</h1>
            <p> Este é um exemplo do roteamento no Flask</p>
            <p> bla bla bla bla </p>
        '''

@app.route('/goodbye')
def goodbye():
    return '<h1>Goodbye from PHP!</h1>'

@app.route('/aluno/<nome_aluno>')
def saudacao(nome_aluno):
    return render_template('saudacao.html', nome=nome_aluno)

@app.route('/soma/<int:num1>/<int:num2>')
def soma(num1, num2):
    return render_template('soma.html', num1=num1, num2=num2)

if __name__ == '__main__':
    app.run(debug=True)