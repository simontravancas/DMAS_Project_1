class Block():
    
    def __init__(self, block_number, miner_id, time_mined):
        super().__init__()
        self.block_number = block_number
        self.miner_id = miner_id
        self.time_mined = time_mined