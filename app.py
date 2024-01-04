from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hello, World!'


@app.route('/home')
def hello_home():
  return 'Hello, home!'


@app.route('/view')
def hello_view():
  return 'Hello, view!'


@app.route('/book')
def hello_book():
  return 'Hello, Books !'


#testing
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
  #print("Hello!")
