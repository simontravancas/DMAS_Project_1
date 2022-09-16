from BlockChainManager import BlockChainManager
from NetworkModel import NetworkModel

network_model = NetworkModel(1000)
for i in range(100):
    network_model.step()

#network_model.printState()

BlockChainManager.findAllTemporaryForks()