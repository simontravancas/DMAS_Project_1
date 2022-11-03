from BlockChainManager import BlockChainManager
from NetworkModel import NetworkModel
from pprint import pprint

network_model = NetworkModel(1000, 3, 0.1 , 300)
# network_model = NetworkModel(10, 3, 0.1 , 3)
for i in range(10000000):
    if (not i % 1000):
        print("iteration "+str(i)+"...")
    network_model.step()

#network_model.printState()

BlockChainManager.findAllTemporaryForks()
a = BlockChainManager.get_forks_data()
pprint(a)
# BlockChainManager.printAllBlockchains()