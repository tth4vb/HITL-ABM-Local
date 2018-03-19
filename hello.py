from flask import Flask
from main import *
from run import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    model = HITLAdopt(50, 50, 0.8, 5000, 1000, 1000, 10000, 0.05, 0.5)
    for i in range(100):
        model.step()
    results = model.dc_master.get_model_vars_dataframe()
    return results.transpose().to_json()
