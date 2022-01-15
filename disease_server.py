from disease_model import Disease_Model
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter


def agent_portrayal(agent):
    """[summary]

    Args:
        agent ([type]): [description]

    Returns:
        [type]: [description]
    """

    portrayal = {"Shape": "circle", "Filled": "true", "r": 0.5}

    if agent.infected == True:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.2

    return portrayal


grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)


number_of_agents_slider = UserSettableParameter(
    "slider", "Number of Agents", 20, 2, 100, 1
)

initial_infection_slider = UserSettableParameter(
    "slider", "Probability of initial infection", 0.3, 0.01, 1, 0.01
)

transmissibility_slider = UserSettableParameter(
    "slider", "Transmissibility", 0.2, 0.01, 1, 0.01
)

level_of_movement_slider = UserSettableParameter(
    "slider", "Level of Movement", 0.5, 0.01, 1, 0.01
)

mean_length_of_disease_slider = UserSettableParameter(
    "slider", "Mean length of disease (days)", 10, 1, 100, 1
)

server = ModularServer(
    Disease_Model,
    [grid],
    "Disease Spread Model",
    {
        "N": number_of_agents_slider,
        "width": 10,
        "height": 10,
        "initial_infection": initial_infection_slider,
        "transmissibility": transmissibility_slider,
        "level_of_movement": level_of_movement_slider,
        "mean_length_of_disease": mean_length_of_disease_slider,
    },
)
