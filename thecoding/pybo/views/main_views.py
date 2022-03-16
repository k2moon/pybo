from flask import Blueprint

route = Blueprint('main', __name__, url_prefix='/')

@route.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!!'

@route.route('/')
def index():
    return 'Hello, Index!!'
