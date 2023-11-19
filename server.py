from flask import Flask

#flask is helping us create the APIs

app = Flask(__name__)#name of the folder (Server)

@app.get("/")
def home():
    return "Hello from Flack!"


app.run(debug=True)#applying the changes to the code