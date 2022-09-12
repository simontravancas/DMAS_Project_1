from Block import Block 
from BlockChain import BlockChain

class BlockChainUtilities():
    @staticmethod
    def create_genesis_block():
        return Block(0, -1)

    @staticmethod
    def create_genesis_blockchain():
        return BlockChain([Block(0, -1)])

    @staticmethod
    def getBlockchainString(blockchain):
        s = ""
        for i in blockchain.block_array:
            s+=("BLOCK " + str(i.block_number) + " (miner " + str(i.miner_id) + ") -> ")
        return s