
# coding: utf-8

# This is a first attempt to build an agent-based model of the integration of a human in the loop algorithm and visualization tool into a system. For now, we're going to just focus on modeling the adoption of the tool with the Mesa python package. This will be adapted from a "forest fire" example adoption model.

# In[1]:


import random

import numpy as np

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import Grid
from mesa.datacollection import DataCollector
from mesa.batchrunner import BatchRunner


# Creating the consultant agent:

# In[2]:


class Consultant(Agent):
   
    def __init__(self, model, pos, ps, tfs, te):
        super().__init__(pos, model)
        self.pos = pos
        self.unique_id = pos
        self.condition = "Potential Trialer"
        self.personalityScore = ps
        self.techFluencyScore = tfs * (1+(self.model.weeklyTrainingSpend/10000))
        self.timeEffect = te
        
        #adding activities for consultant
        self.dataCollection = 5
        self.dataInterpretation = 2
        self.identifyingActions = 2
        self.coaching = 10
        self.review = 1
        
        #initializing deltas for agent
        self.dataCollectionDelta = 0
        self.dataInterpretationDelta = 0
        self.identifyingActionsDelta = 0
        self.coachingDelta = 0
        self.reviewDelta = 0

    def step(self):
        #tagging time starts at 10% of time but decreases with algo accuracy increases
        self.taggingTime = 0.1 - self.model.algoEffect
        
        
        if self.condition == "Potential Trailer":
            self.dataCollection = 5
            self.dataInterpretation = 2
            self.identifyingActions = 2
            self.coaching = 10
            self.review = 1
        
        if self.condition == "Trialer" or self.condition=="Adopter":
            
            #creating time delta variables 
            #data collection takes longer because of tagging time
            self.dataCollectionDelta = self.dataCollection * self.taggingTime
            #data interpreration takes less time because of visualization and algo benefits
            self.dataInterpretationDelta = self.dataInterpretation * -1 * (self.model.vizEffect+self.model.algoEffect)
            #indentifying actions gets more efficient because of viz and algo benefits, also gets 1/3 of DI time savings
            self.identifyingActionsDelta = (self.identifyingActions * (self.model.vizEffect + self.model.algoEffect)) + (self.dataInterpretationDelta/3)
            #1/3 of time savings for data interpretation goes to coaching
            self.coachingDelta = (self.dataInterpretationDelta/3)
            #review gets more efficient because of viz and algo benefits, also gets 1/3 of DI time savings
            self.reviewDelta = (self.review * (self.model.vizEffect + self.model.algoEffect)) + (self.dataInterpretationDelta/3)
            
            #modifying output based on algo effectiveness
            self.dataCollection = 5 + self.dataCollectionDelta
            self.dataInterpretation = 2 + self.dataInterpretationDelta
            self.identifyingActions = 2 + self.identifyingActionsDelta
            self.coaching = 10 + self.coachingDelta
            self.review = 1 + self.reviewDelta
            
        #setting global variable of output value
        self.outputValue = (self.dataCollection * 50) + (self.dataInterpretation * 100) + (self.identifyingActions*150) + (self.coaching * 200) + (self.review * 200)
        
        if self.condition == "Trialer":
            random_num = np.random.randint(1,100)
            if (random_num + self.timeEffect) < 70:
                self.condition == "PotentialTrialer"
            else:  
                neighbors = self.model.grid.get_neighbors(self.pos, moore=False)
                for neighbor in neighbors:
                    if neighbor.condition == "Potential Trialer":
                        if ((neighbor.personalityScore + neighbor.techFluencyScore)/2) + neighbor.timeEffect > 50:
                            neighbor.condition = "Trialer"
                        else:
                            #usability spending increases chances that user will adopt after several times connecting with those who use it
                            neighbor.timeEffect += 5
            if ((self.personalityScore + self.techFluencyScore)/2) + self.timeEffect > 80:
                        self.condition = "Adopter"
            else:
                self.timeEffect += 1 * (1+(self.model.weeklyUsabilitySpend/10000))
                        
            
            


# In[3]:


#tracking output and its components

def compute_avg_output(model):
    agent_outputs = [agent.outputValue for agent in model.schedule.agents]
    avg_output = np.mean(agent_outputs)
    return avg_output

#tracking/computing components
def compute_avg_dc (model):
    agent_dc = [agent.dataCollection for agent in model.schedule.agents]
    avg_dc = np.mean(agent_dc)
    return avg_dc
def compute_avg_di (model):
    agent_di = [agent.dataInterpretation for agent in model.schedule.agents]
    avg_di = np.mean(agent_di)
    return avg_di
def compute_avg_ia (model):
    agent_ia = [agent.identifyingActions for agent in model.schedule.agents]
    avg_ia = np.mean(agent_ia)
    return avg_ia
def compute_avg_coaching (model):
    agent_coaching = [agent.coaching for agent in model.schedule.agents]
    avg_coaching = np.mean(agent_coaching)
    return avg_coaching
def compute_avg_review (model):
    agent_review = [agent.review for agent in model.schedule.agents]
    avg_review = np.mean(agent_review)
    return avg_review

#tracking algorithm accuracy
def compute_algo_accuracy (model):
    algoAccuracy = model.algoAccuracy
    return algoAccuracy

def compute_algo_effect (model):
    algoEffect = model.algoEffect
    return algoEffect

#tracking time deltas
def compute_avg_coaching_delta (model):
    agent_acd = [agent.coachingDelta for agent in model.schedule.agents if agent.condition == "Trialer" or "Adopter"]
    avg_acd = np.mean(agent_acd)
    return avg_acd

#tracking advantages of algo
def hitl_adv_differential (model):
    agent_output_differentials = [(agent.outputValue - 2950) for agent in model.schedule.agents]
    avg_od = np.mean(agent_output_differentials)
    totalDifferential = avg_od * len(agent_output_differentials)
    return totalDifferential


# Creating the model class:

# In[4]:


class HITLAdopt(Model):

    def __init__(self, height, width, density, wms, wts, wus, td, ve, ae):
        
        # Initialize model parameters
        self.height = height
        self.width = width
        self.density = density
        self.weeklyMarketingSpend = wms
        self.weeklyTrainingSpend = wts
        self.weeklyUsabilitySpend = wus

        #initialize algorithm effectiveness parameters
        self.trainingDataWeeklyInput = td
        self.vizEffect = ve
        
        self.learningRate = 0
        self.dataInstances = 10000
        self.algoAccuracy = ae
        
        self.algoEffect = self.algoAccuracy *0.1
        
        # Set up model objects
        
        self.schedule = RandomActivation(self)
        self.grid = Grid(height, width, torus=False)
        self.dc_output = DataCollector(model_reporters={"Avg Output Value Per Person Per Week": compute_avg_output})
        self.dc_tracker = DataCollector(model_reporters={"Average IA": compute_avg_ia})
        self.dc_adoption = DataCollector({"Potential Trialer": lambda m: self.count_type(m, "Potential Trialer"),
                                "Trialer": lambda m: self.count_type(m, "Trialer"),
                                "Adopter": lambda m: self.count_type(m, "Adopter")})
        self.dc_trialers =DataCollector({"Trialer": lambda m: self.count_type(m, "Trialer")})
        self.dc_algo = DataCollector({"Algo Effect": compute_algo_effect})
        for x in range(self.width):
                for y in range(self.height):
                    if random.random() < self.density:
                        new_consultant = Consultant(self, (x, y), np.random.normal(60, 10), np.random.normal(70, 10), 0)
                        if y == 0:
                            new_consultant.condition = "Trialer"
                        self.grid[y][x] = new_consultant
                        self.schedule.add(new_consultant)
        
        self.running = True
        
        
       
        
    def step(self):
        ##update algorithm accuracy
        self.learningRate = 10000/self.dataInstances/13
        self.algoAccuracy += self.learningRate
        self.dataInstances += self.trainingDataWeeklyInput
        self.algoEffect = self.algoAccuracy * 0.1
        '''
        For every 1000 of additional weekly marketing spend, we get 1 new trialer consultant each step aka week
        '''
        
        for i in range (1,(int(self.weeklyMarketingSpend/100))):
            #take a random agent that's a trialer and log their x y location
            prospect = random.choice(model.schedule.agents)
            #change that agent's state to the next one up depending on what it is
            if prospect.condition == "Potential Trialer":
                prospect.condition = "Trialer"
            if prospect.condition == "Trialer":
                prospect.condition = "Adopter"
       
        '''for i in range (1,(int(self.weeklyMarketingSpend/50))):
            #take a random agent that's a trialer and log their x y location
            prospect = random.choice(model.schedule.agents)
            #change that agent's state to the next one up depending on what it is
            random_num = np.random.randint(1,100)
            if prospect.condition == "Trialer":
                if (prospect.techFluencyScore <70):
                    if random_num > 50:
                        prospect.condition = "PotentialTrialer"
        '''
                
        self.schedule.step()
        self.dc_output.collect(self)
        self.dc_adoption.collect(self)
        self.dc_tracker.collect(self)
        self.dc_algo.collect(self)
        self.dc_trialers.collect(self)
        #if self.count_type(self, "Trialer") == 0:
         #   self.running = False
    
    @staticmethod
    def count_type(model, consultant_condition):
        count = 0
        for consultant in model.schedule.agents:
            if consultant.condition == consultant_condition:
                count += 1
        return count


# In[5]:


model = HITLAdopt(50, 50, 0.8, 5000, 1000, 1000, 10000, 0.05, 0.5)
for i in range(100):
    model.step()


# In[6]:


results = model.dc_output.get_model_vars_dataframe()
results.head(25)


# In[7]:


print ("Total increase in value ($):")
print(int(results.sum()))
print("Total increase in value (%):")
print((int(results.sum())/(2950*2000*100)))


# In[8]:


results_adoption = model.dc_adoption.get_model_vars_dataframe()
results_adoption.plot()


# Now let's do it with batch runs:

# In[9]:


#height, width, wus, and density are fixed
fixed_params = {"height": 50, "width": 50, "density": 0.7, "wus": 1000, "wts": 1000, "wms":1000, "td":10000, "ve": 0}
# Vary wms, wts, wus
variable_params = {"ae": np.arange(0.5, 0.8, 0.01)}
model_reporter={"AlgoEffect": compute_algo_effect}
param_run = BatchRunner(HITLAdopt, variable_parameters=variable_params, 
                        fixed_parameters=fixed_params, max_steps = 100, model_reporters=model_reporter)


# In[10]:


param_run.run_all()


# In[11]:


df = param_run.get_model_vars_dataframe()
df.head()


# In[12]:


plt.scatter(df.ae, df.AlgoEffect)
plt.xlim(0.5, 0.8)
plt.ylim(0,.2)


# Visualization Time.

# In[13]:


from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from mesa.visualization.UserParam import UserSettableParameter


# In[16]:


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}
    if agent.condition == "Trialer":
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 0
    elif agent.condition == "Adopter":
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.7
    else:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.2
    return portrayal

ae_slider = UserSettableParameter('slider', "Starting Algo Effectiveness", 0.6, 0.5, 0.8, 0.01)
wms_slider = UserSettableParameter('slider', "Weekly Marketing Spend", 2000, 1000, 10000, 100)
wts_slider = UserSettableParameter('slider', "Weekly Training Spend", 2000, 1000, 10000, 100)
wus_slider = UserSettableParameter('slider', "Weekly Usability Spend", 2000, 1000, 10000, 100)
ve_slider = UserSettableParameter('slider', "Visualization effectiveness (in % time saved)", 0.01, 0.01, 0.2, 0.01)
agent_density_slider = UserSettableParameter('slider', "Starting Algo Effectiveness", 0.5, 0, 1, 0.01)

grid = CanvasGrid(agent_portrayal, 50, 50, 500, 500)

chart1 = ChartModule([{"Label":"Potential Trialer",
                     "Color": "grey"}, {"Label":"Trialer",
                     "Color": "blue"}, {"Label":"Adopter",
                     "Color": "red"}],
                   data_collector_name='dc_adoption')

chart2 = ChartModule([{"Label":"Avg Output Differential Value",
                     "Color": "blue"}],
                   data_collector_name='dc_output')
#create and launch the actual server
server = ModularServer(HITLAdopt,
                      [grid, chart1, chart2],
                      "HITL Adopt",
                      {"height": 50, "width": 50, "density": agent_density_slider, "wus": wus_slider, "wts": wts_slider, "wms":wms_slider, "td":10000,"ae":ae_slider, "ve": ve_slider})
#launching the server
server.port = 8538
server.launch()

