from NetworkModel import NetworkModel

network_model = NetworkModel(10)
for i in range(300):
    network_model.step()

network_model.printState()
