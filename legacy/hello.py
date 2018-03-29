from flask import Flask
from main import *
from run import *
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/YOURAPP/*": {"origins": "*"}})

@app.route('/')
def hello_world():
    '''model = HITLAdopt(50, 50, 0.8, 5000, 1000, 1000, 10000, 0.05, 0.5)
    for i in range(100):
        model.step()
    results = model.dc_master.get_model_vars_dataframe()
    return results.transpose().to_json()'''
    data = request.get_json(silent=True)
    item = {'density': data.get('density'), 'wms': data.get('wms'), 'wts': data.get('wts'), 'wus': data.get('wus'),
    'trainingDataWeeklyInput': data.get('trainingDataWeeklyInput'), 've': data.get('ve'), 'ae': data.get('ae')}
    print (item)
