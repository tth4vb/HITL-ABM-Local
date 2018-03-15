from main import *

model = HITLAdopt(50, 50, 0.8, 5000, 1000, 1000, 10000, 0.05, 0.5)
for i in range(100):
    model.step()

#print results of master data collectors
results = model.dc_master.get_model_vars_dataframe
#convert to json
results_json = results.to_json("/Users/trevorhinkle/Desktop/AlloyWork/HITL_ABM_Local")


'''#print results of output data collector
results = model.dc_output.get_model_vars_dataframe()
print(results.head(25))

#print impact of HITL
print ("Total increase in value ($):")
print(int(results.sum()))
print("Total increase in value (%):")
print((int(results.sum())/(2950*2000*100)))
'''
'''#print adoption metrics of model output
results_adoption = model.dc_adoption.get_model_vars_dataframe()
print(results_adoption.head(50))
'''
'''
#now we'll do a Batch Run, which is where we run several iterations of the model changing certain variables to see impact
fixed_params = {"height": 50, "width": 50, "density": 0.7, "wus": 1000, "wts": 1000, "wms":1000, "td":10000, "ve": 0}
variable_params = {"ae": np.arange(0.5, 0.8, 0.01)}
model_reporter={"AlgoEffect": compute_algo_effect}
param_run = BatchRunner(HITLAdopt, variable_parameters=variable_params,
                        fixed_parameters=fixed_params, max_steps = 100, model_reporters=model_reporter)

#run the batch run
param_run.run_all()

#get dataframe from batch run
df = param_run.get_model_vars_dataframe()
df.head()

#create plot of results of batch run
plt.scatter(df.ae, df.AlgoEffect)
plt.xlim(0.5, 0.8)
plt.ylim(0,.2)'''c
