from flask import Flask

APP = Flask(__name__)

@APP.route('/')

def index():
    '''
    Indentação 'INDEX PAGE'
    '''
    return 'Index Page!'

if __name__ == '__main__':
    APP.run()
