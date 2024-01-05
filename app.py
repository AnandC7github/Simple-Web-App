from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
  return render_template('view.html')


@app.route('/home')
def hello_home():
  return 'Hello, home!'


@app.route('/view')
def hello_view():
  return render_template('index.html')


@app.route('/book')
def hello_book():
  return 'Hello, Books !'


#testing
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
  #print("Hello!")
