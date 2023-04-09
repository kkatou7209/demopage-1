from flask import \
  Flask, \
  render_template, \
  request,\
  url_for

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', user='Kenshiro')

app.run(
  host='0.0.0.0', 
  port=3000, 
  debug=True
)