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
                    s1+=("[ BLOCK " + str(j.block_number) + " (miner " + str(j.miner_id) + ") " + str(j.time_mined) + "] -> ")
                s2 = ""
                blockchain = BlockChainManager.blockChainList[i+1]
                for j in blockchain.block_array:
                    s2+=("[ BLOCK " + str(j.block_number) + " (miner " + str(j.miner_id) + ") " + str(j.time_mined) + "] -> ")
                
                print("TEMPORARY FORK between blockchains:")
                print(s1)
                print(s2)


    @staticmethod
    def get_forks_data():
        forks_data = []
        BlockChainManager.blockChainList.sort(key=lambda blockchain: len(blockchain.block_array))
        for i in range(len(BlockChainManager.blockChainList) - 1):
            if len(BlockChainManager.blockChainList[i].block_array) == len(BlockChainManager.blockChainList[i+1].block_array):
                x = min(BlockChainManager.blockChainList[i].block_array[-1].time_mined, \
                    BlockChainManager.blockChainList[i+1].block_array[-1].time_mined)
                # Blockchain array ends ordered also by time mined, so diff is always positive
                diff = BlockChainManager.blockChainList[i].block_array[-1].time_mined - BlockChainManager.blockChainList[i+1].block_array[-1].time_mined
                # -1 because python indexes from 0
                current_block_index = len(BlockChainManager.blockChainList[i].block_array) - 1
                true_miner_id = BlockChainManager.blockChainList[-1].block_array[current_block_index].miner_id
                y = diff
                if (BlockChainManager.blockChainList[i].block_array[-1].miner_id == true_miner_id):
                    y *= -1
                forks_data.append([x, y])
        return forks_data


    # Notes:
    # Time block was mined
    # (positive or negative) diff

    @staticmethod
    def printAllBlockchains():
        for i in range(len(BlockChainManager.blockChainList)):
            print("Blockchain " + str(i))
            s1 = ""
            for j in BlockChainManager.blockChainList[i].block_array:
                s1+=("[ BLOCK " + str(j.block_number) + " (miner " + str(j.miner_id) + ") ] -> ")
                print(s1)
