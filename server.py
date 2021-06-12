from flask import Flask, render_template
import script1
app = Flask(__name__)

file = open('myfile.txt', 'r')
b_lines = file.readlines()

@app.route('/', methods=["GET", "POST"])
def index():
  return render_template('index.html',b_lines=b_lines)

@app.route('/record_audio/')
def record_audio():
  script1.myCommand()
  print ('Recording Stopped!')
  return render_template('success.html')

if __name__ == '__main__':
  app.run(debug=True)
