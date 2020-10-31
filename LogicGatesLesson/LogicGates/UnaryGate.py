from LogicGates.LogicGate import LogicGate


class UnaryGate(LogicGate):

    def __init__(self, n):
        super().__init__(n)
        self.pin = None

    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS.")
