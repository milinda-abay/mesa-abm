from mesa import Agent, Model
from mesa.time import RandomActivation  # makes the order of agent actions random
from mesa.space import MultiGrid  # Multiple agents per cell
from mesa.datacollection import DataCollector

import random


class Person_Agent(Agent):
    def __init__(
        self,
        unique_id: int,
        model: Model,
        initial_infection,
        transmissibility,
        level_of_movement,
        mean_length_of_disease,
    ) -> None:
        super().__init__(unique_id, model)
        self.transmissibility = transmissibility
        self.level_of_movement = level_of_movement
        self.mean_length_of_disease = mean_length_of_disease
        if random.uniform(0, 1) < initial_infection:
            self.infected = True
            self.disease_duration = int(
                round(random.expovariate(1.0 / self.mean_length_of_disease), 0)
            )
        else:
            self.infected = False

    def move(self):

        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def infect(self):

        cellmates = self.model.grid.get_cell_list_contents([self.pos])

        if len(cellmates) > 1:

            for inhabitant in cellmates:

                if inhabitant.infected is False:
                    if random.uniform(0, 1) < self.transmissibility:
                        inhabitant.infected = True
                        inhabitant.disease_duration = int(
                            round(
                                random.expovariate(1.0 / self.mean_length_of_disease), 0
                            )
                        )

    def step(self):

        if random.uniform(0, 1) < self.level_of_movement:
            self.move()

        if self.infected == True:
            self.infect()

            self.disease_duration -= 1

            if self.disease_duration <= 0:
                self.infected = False
