from BlockChainUtilities import BlockChainUtilities
import numpy
import mesa
from MinerAgent import MinerAgent
from Position import Position
from pprint import pprint
from Message import Message

class NetworkModel(mesa.Model):
    def __init__(self, N, num_clusters, cluster_size, agents_per_cluster):
        self.num_agents = N
        self.num_clusters = num_clusters
        self.cluster_size = cluster_size
        self.agents_per_cluster = agents_per_cluster
        self.space = mesa.space.ContinuousSpace(1,1,True,0,0)
        self.time = 0
        self.schedule = mesa.time.RandomActivation(self)
        self.agents_array = []
        self.message_queue = []
        genesis_blockchain = BlockChainUtilities.create_genesis_blockchain()
        self.timeMultiplier = 10
        self.timeRandomnessMultiplier = 10
        self.lag_spike_time = 10
        self.cluster_positions = []
        # Create clusters
        for i in range(self.num_clusters):
            pos = Position(self.cluster_size + numpy.random.rand() * (1 - 2*self.cluster_size),\
                           self.cluster_size + numpy.random.rand() * (1 - 2*self.cluster_size))
            #TODO: Fix overlapping clusters
            self.cluster_positions.append(pos)

        # Populate clusters
        for i in range(self.num_clusters):
            for j in range(self.agents_per_cluster):
                pos = Position(self.cluster_positions[i].x + ((numpy.random.rand() * 2) - 1) * (self.cluster_size),\
                               self.cluster_positions[i].y + ((numpy.random.rand() * 2) - 1) * (self.cluster_size))
                a = MinerAgent(i * self.agents_per_cluster + j, self, 1, pos, i, genesis_blockchain)
                self.space.place_agent( a, (pos.x, pos.y) )
                self.agents_array.append(a)
                self.schedule.add(a)
        
        # Populate clusterless agents
        for i in range(self.num_clusters * self.agents_per_cluster, self.num_agents):
            pos = Position(numpy.random.rand(), numpy.random.rand())
            a = MinerAgent(i, self, 1, pos, -1, genesis_blockchain)
            self.space.place_agent( a, (pos.x, pos.y) )
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
        for destination in self.agents_array:
            if destination.unique_id == miner.unique_id:
                # print("Trying to broadcast a message to myself (" + str(destination.unique_id) + ")")
                continue
            pos1 = miner.position
            pos2 = destination.position
            distance = self.space.get_distance([pos1.x, pos1.y], [pos2.x, pos2.y])
            time_of_arrival = self.time + distance*self.timeMultiplier + numpy.random.rand()*self.timeRandomnessMultiplier
            if (miner.cluster_id != destination.cluster_id):
                # print(f"hey, agents {miner.unique_id} and {destination.unique_id} have different cluster ids! ({miner.cluster_id} and {destination.cluster_id})")
                time_of_arrival += self.lag_spike_time
            msg = Message(blockchain, time_of_arrival, destination)
            self.message_queue.append(msg)
        self.message_queue.sort(key=lambda msg: msg.time)

        # self.printQueueState()

    def printQueueState(self):
        for msg in self.message_queue:
            print("time: " + str(msg.time) + ", destination: " + str(msg.destination.unique_id))

    def printState(self):
        for i in self.agents_array:
            print("agent " + str(i.unique_id) + " has blockchain " + BlockChainUtilities.getBlockchainString(i.blockChain))