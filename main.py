from flask import Flask, request, render_template, url_for
from wtforms import Form

from linear_system_of_equations import gauss_seidel, is_diagonal, jacobi, listoflist
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/gauss_jacobi', methods = ["GET", "POST"])
def gauss_jacobi():
    if request.method == "POST":
        data = request.form

        result= {}

        A = listoflist.string_to_list_of_lists(data.get('A')) # string to list(list(int))
        Y = json.loads(data.get('Y')) # string to list 
        X = json.loads(data.get('x')) # for gauss
        x = json.loads(data.get('x')) # for jacobi
        iterations = int(data.get('iterations'))
        if is_diagonal.Is_DiagonalDominant(A):
            for i in range(iterations):
                X = gauss_seidel.gauss_seidel(A, Y, X)
                x = jacobi.jacobi(A, Y, x)

            result['gauss'] = X
            result['jacobi'] = x
            result['iterations'] = i+1


        return render_template("gauss_jacobi.html", result=result)
    
    return render_template("gauss_jacobi.html")


if __name__ == "__main__":
    app.run(debug=True)