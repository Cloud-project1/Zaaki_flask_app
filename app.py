import requests
import sqlite3 as sql
import urllib
from random import randint
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

FILENAME = "../../Downloads/Cloud-master/ZKHP.html"
con = sql.connect(FILENAME)
C = con.cursor()

# ID set is used to make sure the recipes have a unique ID
# APP_ID and API_KEY were given by Edamame to create an account to use the API

IDS = {-1}
APP_ID = '8228a6c6'
API_KEY = 'bd00528170e470eae3f228cb5bc7a1fc'
URL = f'https://api.edamam.com/search?/app_id=8228a6c6&app_key=bd00528170e470eae3f228cb5bc7a1fc'




# The following code is for the Recipe APP

@app.route('/')
@app.route('/home')
def home():
    return render_template("ZKHP.html")

# The following lines are for searching recipes from the API
