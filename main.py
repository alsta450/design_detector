from pathlib import Path
import os
import json
from flask import Flask, render_template, request
from handler.process_handler import ProcessHandler

app = Flask(__name__)


@app.route("/",methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        path = request.form['path']
        process_handler = ProcessHandler(Path(str(path)))
        result_string = process_handler.run()
        pretty_json = json.dumps(result_string, indent=4, sort_keys=True)
        return render_template("result.html",value=pretty_json)
    else:
        return render_template("index.html")

@app.route("/result")
def result(pretty_json):
    return render_template("result.html",value=pretty_json)


if __name__ == "__main__":
    app.run()
    # process_handler = ProcessHandler(Path(str(r"C:\Users\alexs\Documents\Informatik\Bachelorarbeit\okta-spring-microservices-https-example-main")))
    # process_handler.run()