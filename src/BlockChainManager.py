class BlockChainManager():

    # holds ALL blockchains ever created
    # might cause memory use to skyrocket if simulation goes long enough?
    blockChainList =[]

    @staticmethod
    def register(blockchain):
        BlockChainManager.blockChainList.append(blockchain)

    # @staticmethod
    # findAllTemporaryForks():