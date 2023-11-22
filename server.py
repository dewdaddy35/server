from flask import Flask
import json
from config import me
from mock_data import catalog

#flask is helping us create the APIs

app = Flask(__name__)#name of the folder (Server)

@app.get("/")
def home():
    return "Hello from Flack!"

@app.get("/test")
def test():
    return "This is a test page!"

######################################
############ API - Products ##########
######################################


@app.get("/api/about")
def about():
    return json.dumps({"version": 1.03, "name": 'stables3'})

@app.get("/api/about/me")
def about_me():
    
    return json.dumps(me)

@app.get("/api/product")
def get_products():
    return json.dumps(catalog)


@app.get("/api/product/count")
def product_count():
    total = len(catalog)
    return json.dumps({"total": total})



app.run(debug=True)#applying the changes to the code