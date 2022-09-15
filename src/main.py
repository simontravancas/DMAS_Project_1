from NetworkModel import NetworkModel

network_model = NetworkModel(5)
for i in range(21):
    network_model.step()

#network_model.printState()