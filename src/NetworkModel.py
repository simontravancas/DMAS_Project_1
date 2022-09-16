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
        genesis_blockchain = BlockChainUtilities.create_genesis_blockchain()
        # Create agents
        for i in range(self.num_agents):
            a = MinerAgent(i, self, 1, Position(numpy.random.rand(), numpy.random.rand()), genesis_blockchain)
            self.agents_array.append(a)
            self.schedule.add(a)

    def step(self):
        """Advance the model by one step."""
        # pprint(vars(self))
        self.schedule.step()

        self.time+=1

        if (len(self.message_queue) > 0):
            # while first message is supposed to arrive now
            while(self.message_queue[0].time <= self.time):
                # send message to destination
                self.message_queue[0].destination.handleMessage(self.message_queue[0].blockchain)
                # remove first message from queue (it has already been processed)
                self.message_queue.remove(self.message_queue[0])
                # if queue is empty, do not crash
                if (len(self.message_queue) <= 0):
                    break

    def broadcastMessage(self, blockchain, miner):
        for miner in self.agents_array:
            # "10" is not supposed to be hardcoded - we will calculate it later
            msg = Message(blockchain, self.time + 10 + numpy.random.rand()*10, miner)
            self.message_queue.append(msg)
        self.message_queue.sort(key=lambda msg: msg.time)

        self.printQueueState()

    def printQueueState(self):
        for msg in self.message_queue:
            print("time: " + str(msg.time) + ", destination: " + str(msg.destination.unique_id))

    def printState(self):
        for i in self.agents_array:
            print("agent " + str(i.unique_id) + " has blockchain " + BlockChainUtilities.getBlockchainString(i.blockChain))