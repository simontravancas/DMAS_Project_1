from BlockChainManager import BlockChainManager
from NetworkModel import NetworkModel

network_model = NetworkModel(1000)
for i in range(60000):
    if (not i % 1000):
        print("iteration "+str(i)+"...")
    network_model.step()

#network_model.printState()

BlockChainManager.findAllTemporaryForks()
# BlockChainManager.printAllBlockchains()