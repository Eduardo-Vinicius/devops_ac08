from flask import Flask

App = Flask(__name__)

@app.route('/')

def index():
  '''
  Indentação 'INDEX PAGE'
  '''
    return 'Index Page!'

if __name__ == '__main__':
    app.run()
