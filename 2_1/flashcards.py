from flask import (Flask, render_template, abort, jsonify, request,
                   redirect, url_for)
from model import db
#from datetime import datetime

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template(
                 "welcome.html",
                 message="Here's a message from the view.",
                 x=42
            )

@app.route("/card")
def card_view():
    card = db[0]
    return render_template("card.html", card=card)
















#views = 0
#@app.route("/count_views")
#def count_views():
#    global views
#    views += 1
#    return "Number of views is equal to "+str(views)

#@app.route("/date")
#def date():
#    return "This page was server at " + str(datetime.now())
