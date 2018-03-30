import random

import numpy as np
import pandas as pd
import matplotlib as plt
from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import Grid
from mesa.datacollection import DataCollector
from mesa.batchrunner import BatchRunner

#defining the consultant class
class Consultant(Agent):

    #initialize the agent and set values of variables and inputs for the agent.
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

        #initializing deltas for agent, these variables represent the changes in activities for the agents
        self.dataCollectionDelta = 0
        self.dataInterpretationDelta = 0
        self.identifyingActionsDelta = 0
        self.coachingDelta = 0
        self.reviewDelta = 0

    #step is everything that happens for each unit of time in the model
    def step(self):

        #tagging time starts at 10% of time but decreases with algo accuracy increases
        self.taggingTime = 0.1 - self.model.algoEffect

        #the base cases, aka what happens if the user has not or is not using HITL solution
        if self.condition == "Potential Trialer":
            self.dataCollection = 5
            self.dataInterpretation = 2
            self.identifyingActions = 2
            self.coaching = 10
            self.review = 1

        if self.condition == "Defector":
            self.dataCollection = 5
            self.dataInterpretation = 2
            self.identifyingActions = 2
            self.coaching = 10
            self.review = 1

        #benefits of model for trialers or adopters
        if self.condition == "Trialer" or self.condition=="Adopter" or self.condition=="Evangelist":

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
            self.coaching = 10 - self.coachingDelta
            self.review = 1 + self.reviewDelta

        #setting global variable of output value, given values of activity varaibles depending on agent state
        self.outputValue = (self.dataCollection * 50) + (self.dataInterpretation * 100) + (self.identifyingActions*150) + (self.coaching * 200) + (self.review * 200)

        #this is the logic for spread of the model via word of mouth
        if self.condition == "Evangelist":
            neighbors = self.model.grid.get_neighbors(self.pos, moore=False)
            for neighbor in neighbors:
                if neighbor.condition == "Potential Trialer":
                    if ((neighbor.personalityScore + neighbor.techFluencyScore)/2) + neighbor.timeEffect > 10:
                        neighbor.condition = "Trialer"
                    else:
                        neighbor.timeEffect += 10
        if self.condition == "Trialer":
            random_num = np.random.randint(1,100)
            if (random_num + self.timeEffect) < 3:
                self.condition = "Defector"

            elif (random_num + self.timeEffect) < 20:
                self.condition = "Potential Trialer"

            else:
                neighbors = self.model.grid.get_neighbors(self.pos, moore=False)
                for neighbor in neighbors:
                    if neighbor.condition == "Potential Trialer":
                        if ((neighbor.personalityScore + neighbor.techFluencyScore)/2) + neighbor.timeEffect > 50:
                            neighbor.condition = "Trialer"
                        else:
                            neighbor.timeEffect += 5
            if ((self.personalityScore + self.techFluencyScore)/2) + self.timeEffect > 75:
                        self.condition = "Adopter"
            else:
                self.timeEffect += 1 * (1+(self.model.weeklyUsabilitySpend/10000))
        if self.condition == "Adopter" and ((self.personalityScore + self.techFluencyScore)/2) + self.timeEffect > 80:
            self.condition = "Evangelist"

#now, we need to set up some methods for the data collectors
#tracking output and its components

def compute_avg_output(model):
    agent_outputs = [agent.outputValue for agent in model.schedule.agents]
    avg_output = np.mean(agent_outputs)
    return avg_output

#tracking/computing components
def compute_avg_dc (model):
    agent_dc = [agent.dataCollection for agent in model.schedule.agents if agent.condition == "Trialer" or "Adopter" or "Evangelist"]
    avg_dc = np.mean(agent_dc)
    return avg_dc
def compute_avg_di (model):
    agent_di = [agent.dataInterpretation for agent in model.schedule.agents if agent.condition == "Trialer" or "Adopter" or "Evangelist"]
    avg_di = np.mean(agent_di)
    return avg_di
def compute_avg_ia (model):
    agent_ia = [agent.identifyingActions for agent in model.schedule.agents if agent.condition == "Trialer" or "Adopter" or "Evangelist"]
    avg_ia = np.mean(agent_ia)
    return avg_ia
def compute_avg_coaching (model):
    agent_coaching = [agent.coaching for agent in model.schedule.agents if agent.condition == "Trialer" or "Adopter" or "Evangelist"]
    avg_coaching = np.mean(agent_coaching)
    return avg_coaching
def compute_avg_review (model):
    agent_review = [agent.review for agent in model.schedule.agents if agent.condition == "Trialer" or "Adopter" or "Evangelist"]
    avg_review = np.mean(agent_review)
    return avg_review

#tracking algorithm accuracy
def compute_algo_accuracy (model):
    algoAccuracy = model.algoAccuracy
    return algoAccuracy

def compute_learning_rate (model):
    learningRate = model.learningRate
    return learningRate

def compute_data_instances (model):
    dataInstances = model.dataInstances
    return dataInstances

def compute_algo_effect (model):
    algoEffect = model.algoEffect
    return algoEffect

#tracking time deltas
def compute_avg_coaching_delta (model):
    agent_acd = [agent.coachingDelta for agent in model.schedule.agents if agent.condition == "Trialer" or "Adopter" or "Evangelist"]
    avg_acd = np.mean(agent_acd)
    return avg_acd

#tracking advantages of algo
def hitl_adv_differential (model):
    agent_output_differentials = [(agent.outputValue - 2950) for agent in model.schedule.agents]
    avg_od = np.mean(agent_output_differentials)
    totalDifferential = avg_od * len(agent_output_differentials)
    return totalDifferential




#now, we're defining the model class
class HITLAdopt(Model):

    #modify init method to accout for new parameters and constants
    def __init__(self, height, width, density, wms, wts, wus, td, ve, ae):

        # Initialize model parameters
        self.height = height
        self.width = width
        self.density = density
        self.weeklyCampaignSpend = wms
        self.weeklyTrainingSpend = wts
        self.weeklyUsabilitySpend = wus

        #initialize HITL related parameters
        self.trainingDataWeeklyInput = td
        self.vizEffect = ve

        self.learningRate = 0
        self.dataInstances = 10000
        self.algoAccuracy = ae

        self.algoEffect = self.algoAccuracy *0.1


        # Set up model objects

        #this sets the activation order of the agents (when they make their moves) to be random each step
        self.schedule = RandomActivation(self)

        #this creates the physical grid we are using to simulate word of mouth spread of the model
        self.grid = Grid(height, width, torus=False)

        #these use the Mesa DataCollector method to create several trackers to collect data from the model run
        self.dc_output = DataCollector(model_reporters={"Avg Output Value Per Person Per Week": compute_avg_output})
        self.dc_tracker = DataCollector(model_reporters={"Average IA": compute_avg_ia})
        self.dc_adoption = DataCollector({"Potential Trialer": lambda m: self.count_type(m, "Potential Trialer"),
                                "Trialer": lambda m: self.count_type(m, "Trialer"),
                                "Adopter": lambda m: self.count_type(m, "Adopter"), "Defector": lambda m: self.count_type(m, "Defector"), "Evangelist": lambda m: self.count_type(m, "Evangelist")})
        self.dc_trialers =DataCollector({"Trialer": lambda m: self.count_type(m, "Trialer")})
        self.dc_algo = DataCollector({"Learning Rate": compute_learning_rate})

        self.dc_master=DataCollector({"Potential Trialer": lambda m: self.count_type(m, "Potential Trialer"),
                                "Trialer": lambda m: self.count_type(m, "Trialer"),
                                "Adopter": lambda m: self.count_type(m, "Adopter"),
                                "Defector": lambda m: self.count_type(m, "Defector"),
                                "Evangelist": lambda m: self.count_type(m, "Evangelist"),
                                "Avg Output Value Per Person": compute_avg_output,
                                "Total Differential in Population": hitl_adv_differential,
                                "Algo Accuracy": compute_algo_accuracy,
                                "Algo Accuracy Increase": compute_learning_rate,
                                "Total Dataset Size": compute_data_instances,
                                "Algorithm Effect": compute_algo_effect,
                                "Avg Data Collection Ouput": compute_avg_dc,
                                "Avg Data Interpretation/Analysis Output": compute_avg_di,
                                "Avg Interpreting Actions Output": compute_avg_ia,
                                "Avg Coaching Output": compute_avg_coaching,
                                "Avg Review Output": compute_avg_review})

        #the logic for the creation of the agents, as well as setting the initial values of the agent parameters
        for x in range(self.width):
                for y in range(self.height):
                    if random.random() < self.density:
                        new_consultant = Consultant(self, (x, y), np.random.normal(60, 10), np.random.normal(70, 10), 0)
                        if y == 0:
                            new_consultant.condition = "Trialer"
                        self.grid[y][x] = new_consultant
                        self.schedule.add(new_consultant)

        #run the model when the class is called
        self.running = True




    #define logic of what happens with each time step model-wide
    def step(self):
        ##update algorithm accuracy, data instances, and effect for new weekly data input
        self.learningRate = 10000/self.dataInstances/13 - ((self.count_type(self, "Trialer") +
                                                           self.count_type(self, "Adopter") +
                                                           self.count_type(self, "Evangelist"))/2000000)
        self.algoAccuracy += self.learningRate
        self.dataInstances += self.trainingDataWeeklyInput
        self.algoEffect = self.algoAccuracy * 0.1
        #logic for adoption from marketing, For every 1000 of additional weekly marketing spend, we get 1 new trialer consultant each week
        for i in range (1,(int(self.weeklyCampaignSpend/100))):
            prospect = random.choice(self.schedule.agents)
            #change that agent's state to the next one up
            if prospect.condition == "Potential Trialer":
                prospect.condition = "Trialer"
            if prospect.condition == "Trialer":
                prospect.condition = "Adopter"
       #an abandoned idea for trial abandonment...I instead decided to model this at an agent level in that class (See above)
        '''for i in range (1,(int(self.weeklyMarketingSpend/50))):
            #take a random agent that's a trialer and log their x y location
            prospect = random.choice(model.schedule.agents)
            #change that agent's state to the next one up depending on what it is
            random_num = np.random.randint(1,100)
            if prospect.condition == "Trialer":
                if (prospect.techFluencyScore <70):
                    if random_num > 50:
                        prospect.condition = "Potential Trialer"
        '''
        #sets the step count
        self.schedule.step()
        #logs appropriate data in each of the data collectors
        self.dc_output.collect(self)
        self.dc_adoption.collect(self)
        self.dc_tracker.collect(self)
        self.dc_algo.collect(self)
        self.dc_trialers.collect(self)
        self.dc_master.collect(self)
        #abandoned logic for stopping model - it was originally when there were no more trialers, now we just give it a set number of steps
    #method for counting the agents and their conditions so we can track adoption methods
    @staticmethod
    def count_type(model, consultant_condition):
        count = 0
        for consultant in model.schedule.agents:
            if consultant.condition == consultant_condition:
                count += 1
        return count

