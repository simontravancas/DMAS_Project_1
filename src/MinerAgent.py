from Block import Block
from BlockChain import BlockChain
from BlockChainUtilities import BlockChainUtilities
from Strategy import Strategy
import mesa
import numpy

class MinerAgent(mesa.Agent):

    def __init__(self, unique_id, model, compute_power, position, strategy, genesis_blockChain):
        super().__init__(unique_id, model)
        self.unique_id = unique_id
        self.model = model
        self.compute_power = compute_power
        self.position = position
        self.strategy = strategy
        self.blockChain = genesis_blockChain
        # self.blockChain = BlockChainUtilities.create_genesis_blockchain()
        # print("agent " + str(self.unique_id) + " started at position (" + str(position.x) + ", " + str(position.y) + ")" )

    def step(self):
        if (self.runLottery()):
            print("agent " + str(self.unique_id) + "(mining strategy " + str(self.strategy) + ") mined a block at time " + str(self.model.time))
            self.blockChain = self.createNewBlockChain()
            if (self.strategy == Strategy.NORMAL):
                self.model.broadcastMessage(self.blockChain, self)
            elif (self.strategy == Strategy.SELFISH):
                if self.blockChain.getLastBlock().miner_id == self.unique_id:
                    self.model.broadcastMessage(self.blockChain, self)

    def handleMessage(self, blockChain):
        if (self.strategy == Strategy.NORMAL):
            if self.blockChain.getLastBlockNumber() < blockChain.getLastBlockNumber():
                self.blockChain = blockChain
        elif (self.strategy == Strategy.SELFISH):
            if blockChain.getLastBlock().miner_id == self.unique_id:
                return
            if self.blockChain.getLastBlockNumber() <= blockChain.getLastBlockNumber():
                self.blockChain = blockChain
            else:
                self.model.broadcastMessage(self.blockChain, self)


    def createNewBlockChain(self):
        newBlockChain = self.blockChain.block_array.copy()
        newBlockChain.append(self.createNewBlock())
        return BlockChain(newBlockChain)


    def createNewBlock(self):
        return Block(self.blockChain.getLastBlock().block_number + 1, self.unique_id)
    

    def runLottery(self):
        # The following ifs are for testing purpose only
        if ((self.unique_id == 1 and self.model.time == 0) or (self.unique_id == 2 and self.model.time == 2)):
            return 1
        # else:
        #     return 0
        # if ((self.unique_id == 4 and (self.model.time == 9 or self.model.time == 26 or self.model.time == 5009))):
        if ((self.unique_id == 4 and (self.model.time == 26 or self.model.time == 5009))):
            return 1

        # The following ifs are real
        if (numpy.random.rand() < 0.0000016666): #1.666 10e-6
            return 1
        else:
            return 0
