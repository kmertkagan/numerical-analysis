from flask import Flask, render_template
from wtforms import Form


app = Flask(__name__)

@app.route('/', methods = ["GET"])
def gauss_seidal():
    return render_template("gauss_seidal.html")


if __name__ == "__main__":
    app.run(debug=True)