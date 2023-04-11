import sys

sys.path.append("/usr/local/lib/python3.12/site-packages")

from flask import \
  Flask, \
  render_template, \
  request,\
  url_for

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', user='Kenshiro')

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3000)