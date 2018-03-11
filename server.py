from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from mesa.visualization.UserParam import UserSettableParameter
from main import HITLAdopt

#defining the method that places the agent in the visualization
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

#creating interactive parameters for user to set in the visualization
ae_slider = UserSettableParameter('slider', "Starting Algo Effectiveness", 0.6, 0.5, 0.8, 0.01)
wms_slider = UserSettableParameter('slider', "Weekly Marketing Spend", 2000, 1000, 10000, 100)
wts_slider = UserSettableParameter('slider', "Weekly Training Spend", 2000, 1000, 10000, 100)
wus_slider = UserSettableParameter('slider', "Weekly Usability Spend", 2000, 1000, 10000, 100)
ve_slider = UserSettableParameter('slider', "Visualization effectiveness (in % time saved)", 0.01, 0.01, 0.2, 0.01)
agent_density_slider = UserSettableParameter('slider', "Starting Algo Effectiveness", 0.5, 0, 1, 0.01)

#initialize the grid for the visualization
grid = CanvasGrid(agent_portrayal, 50, 50, 500, 500)

#create dynamic for the visualization
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

#launching the server and visualization - default port to start is 8521
server.port = 8521
server.launch()