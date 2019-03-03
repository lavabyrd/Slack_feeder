from flask import Flask
from api.main import api

app = Flask(__name__)


app.register_blueprint(api)



@app.route('/')
def home():
    return "hello"