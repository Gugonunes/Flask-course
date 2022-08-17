from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gustavo'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Bom dia pessoal!'
        },
        {
            'author': {'username': 'Jorge'},
            'body': 'Hoje está frio :D'
        }
    ]
    return  render_template('index.html', title='Página inicial', user=user, posts=posts)

