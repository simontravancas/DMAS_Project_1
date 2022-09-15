class BlockChain():
    
    def __init__(self, block_array):
        super().__init__()
        self.block_array = block_array

    def getLastBlock(self):
        return self.block_array[-1]

    def getLastBlockNumber(self):
        return self.block_array[-1].block_number