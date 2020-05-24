from flask import (Flask, render_template, abort, jsonify, request,
                   redirect, url_for)
#from datetime import datetime

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to my FLash Cards application!"




















#views = 0
#@app.route("/count_views")
#def count_views():
#    global views
#    views += 1
#    return "Number of views is equal to "+str(views)

#@app.route("/date")
#def date():
#    return "This page was server at " + str(datetime.now())
