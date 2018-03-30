
import random
import mesa
import run_hitl
from flask import Flask, render_template

app = Flask(__name__, static_folder='../client/build/static', template_folder='../client/build/')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/model') # take note of this decorator syntax, it's a common pattern
def hello():
    # It is good practice to only call a function in your route end-point,
    # rather than have actual implementation code here.
    # This allows for easier unit and integration testing of your functions.
    return get_hello()


def get_hello():
    return run_hitl.model_run()

if __name__ == '__main__':
    app.run()
