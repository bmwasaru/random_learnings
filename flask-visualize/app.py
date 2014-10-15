import os

from flask import Flask
from flask import render_template
from flask import jsonify
from open_data_scraper import get_data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify(get_data())

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
