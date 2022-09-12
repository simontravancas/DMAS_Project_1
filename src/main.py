from NetworkModel import NetworkModel

network_model = NetworkModel(100)
for i in range(1000):
    network_model.step()
