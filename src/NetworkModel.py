from BlockChainUtilities import BlockChainUtilities
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
        self.agents_array = []
        # Create agents
        for i in range(self.num_agents):
            a = MinerAgent(i, self, 1, Position(numpy.random.rand(), numpy.random.rand()))
            self.agents_array.append(a)
            self.schedule.add(a)

    def step(self):
        """Advance the model by one step."""
        self.time+=1
        # pprint(vars(self))
        self.schedule.step()

    def printState(self):
        for i in self.agents_array:
            print("agent " + str(i.unique_id) + " has blockchain " + BlockChainUtilities.getBlockchainString(i.blockChain))