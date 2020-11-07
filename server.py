from flask import Flask, render_template
import script1
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  script1.myCommand()
  print ('I got clicked!')

  return 'Click.'

if __name__ == '__main__':
  app.run(debug=True)
