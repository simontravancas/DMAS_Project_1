import numpy
import mesa
from MinerAgent import MinerAgent
from Position import Position
from pprint import pprint

class NetworkModel(mesa.Model):
    def __init__(self, N):
        self.num_agents = N
        self.time = 0
        self.schedule = mesa.time.RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = MinerAgent(i, self, 1, Position(numpy.random.rand(), numpy.random.rand()))
            self.schedule.add(a)

    def step(self):
        """Advance the model by one step."""
        self.time+=1
        # pprint(vars(self))
        self.schedule.step()