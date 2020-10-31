from LogicGates.AndGate import AndGate
from LogicGates.OrGate import OrGate
from LogicGates.NotGate import NotGate
from LogicGates.Connector import Connector


def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(f"Gate {g4.getLabel()} output: {g4.getOutput()}")


if __name__ == "__main__":
    main()
