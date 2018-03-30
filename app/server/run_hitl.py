from hitl_model import *
import pandas as pd
import numpy as np


def model_run():
    model = HITLAdopt(50, 50, 0.8, 5000, 1000, 1000, 10000, 0.05, 0.5)
    for i in range(50):
        model.step()


    results = model.dc_master.get_model_vars_dataframe()
    transposed_results = results.transpose().to_json()
    return transposed_results
    print (transposed_results)
   
model_run()
