from Block import Block
from BlockChain import BlockChain
from BlockChainUtilities import BlockChainUtilities
import mesa
import numpy

class MinerAgent(mesa.Agent):

    def __init__(self, unique_id, model, compute_power, position, genesis_blockChain):
        super().__init__(unique_id, model)
        self.unique_id = unique_id
        self.model = model
        self.compute_power = compute_power
        self.position = position
        self.blockChain = genesis_blockChain
        # self.blockChain = BlockChainUtilities.create_genesis_blockchain()
        # print("agent " + str(self.unique_id) + " started at position (" + str(position.x) + ", " + str(position.y) + ")" )

    def step(self):
        if (self.runLottery()):
            print("agent " + str(self.unique_id) + " mined a block at time " + str(self.model.time))
            self.blockChain = self.createNewBlockChain()
            
            # broadcast
            self.model.broadcastMessage(self.blockChain, self)

    def handleMessage(self, blockChain):
        if self.blockChain.getLastBlockNumber() < blockChain.getLastBlockNumber():
            self.blockChain = blockChain

    def createNewBlockChain(self):
        newBlockChain = self.blockChain.block_array.copy()
        newBlockChain.append(self.createNewBlock())
        return BlockChain(newBlockChain)


    def createNewBlock(self):
        return Block(self.blockChain.getLastBlock().block_number + 1, self.unique_id)
    

    def runLottery(self):
        if ((self.unique_id == 1 and self.model.time == 0) or (self.unique_id == 2 and self.model.time == 2)):
            return 1
        # else:
        #     return 0

        if (numpy.random.rand() < 0.0000016666): #1.666 10e-6
            return 1
        else:
            return 0
