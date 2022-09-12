import mesa
import numpy

class MinerAgent(mesa.Agent):

    def __init__(self, unique_id, model, compute_power, position):
        super().__init__(unique_id, model)
        self.compute_power = compute_power
        self.position = position
        # print("agent " + str(self.unique_id) + " started at position (" + str(position.x) + ", " + str(position.y) + ")" )

    def step(self):
        if (self.runLottery()):
            # pass
            print("agent " + str(self.unique_id) + " mined a block at time .")


    def runLottery(self):
        if (numpy.random.rand() < 0.001):
            return 1
        else:
            return 0