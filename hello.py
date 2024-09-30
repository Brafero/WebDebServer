# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, make_response, redirect, abort
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello from Flask!</p><table><tr><td><b>Professor:</b></td><td>Professor Fabio Teixeira</td></tr><tr><td><b>Prontuário:</b></td><td>PT23820X</td></tr></table>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-agent')
    return '<p>Seu navegador é {}! </p>'.format(user_agent);

@app.route('/codigostatusdiferente')
def codigostatusdiferente():
    return '<p>Bad request</p>'

@app.route('/objetoresposta')
def objetoresposta():
    msg = '<h1>Esse site retorna cookies!</h1>'
    resp = make_response(msg)
    resp.set_cookie('MeuCookie', '42')
    return resp

@app.route('/redirecionamento')
def redirecionamento():
    return redirect("https://ptb.ifsp.edu.br/")

@app.route('/abortar')
def abortar():
    return abort(404)