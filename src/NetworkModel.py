from BlockChainUtilities import BlockChainUtilities
import numpy
import mesa
from MinerAgent import MinerAgent
from Position import Position
from pprint import pprint
from Message import Message

class NetworkModel(mesa.Model):
    def __init__(self, N):
        self.num_agents = N
        self.time = 0
        self.schedule = mesa.time.RandomActivation(self)
        self.agents_array = []
        self.message_queue = []
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

    def broadcastMessage(self, blockchain, miner):
        for miner in self.agents_array:
            # "10" is not supposed to be hardcoded - we will calculate it later
            msg = Message(blockchain, self.time + 10 + numpy.random.rand()*10, miner)
            self.message_queue.append(msg)

        self.printQueueState()

    def printQueueState(self):
        for msg in self.message_queue:
            print("time: " + str(msg.time) + ", destination: " + str(msg.destination.unique_id))

    def printState(self):
        for i in self.agents_array:
            print("agent " + str(i.unique_id) + " has blockchain " + BlockChainUtilities.getBlockchainString(i.blockChain))