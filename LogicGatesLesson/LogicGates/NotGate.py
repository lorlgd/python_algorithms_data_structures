from LogicGates.UnaryGate import UnaryGate


class NotGate(UnaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        pin = self.getPin()
        if pin == 1:
            return 0
        else:
            return 1
