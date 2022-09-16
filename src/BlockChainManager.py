class BlockChainManager():

    # holds ALL blockchains ever created
    # might cause memory use to skyrocket if simulation goes long enough?
    blockChainList =[]

    @staticmethod
    def register(blockchain):
        BlockChainManager.blockChainList.append(blockchain)

    @staticmethod
    def findAllTemporaryForks():
        BlockChainManager.blockChainList.sort(key=lambda blockchain: len(blockchain.block_array))
        for i in range(len(BlockChainManager.blockChainList) - 1):
            if len(BlockChainManager.blockChainList[i].block_array) == len(BlockChainManager.blockChainList[i+1].block_array):
                blockchain = BlockChainManager.blockChainList[i]
                # copy-pasted code! bad!
                s1 = ""
                for j in blockchain.block_array:
                    s1+=("[ BLOCK " + str(j.block_number) + " (miner " + str(j.miner_id) + ") ] -> ")
                s2 = ""
                blockchain = BlockChainManager.blockChainList[i+1]
                for j in blockchain.block_array:
                    s2+=("[ BLOCK " + str(j.block_number) + " (miner " + str(j.miner_id) + ") ] -> ")
                
                print("TEMPORARY FORK between blockchains:")
                print(s1)
                print(s2)
