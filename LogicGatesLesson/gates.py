from LogicGates.AndGate import AndGate
from LogicGates.OrGate import OrGate
from LogicGates.NotGate import NotGate
from LogicGates.NandGate import NandGate
from LogicGates.NorGate import NorGate
from LogicGates.XorGate import XorGate
from LogicGates.Connector import Connector


def half_adder(and_gate, xor_gate):
    print("Half adder circuit")
    carry_bit = and_gate.getOutput()
    sum_bit = xor_gate.getOutput()
    print(f"sum bit {sum_bit}")
    print(f"carry bit {carry_bit}")


def main():
    g1 = AndGate("G1")
    g2 = XorGate("G2")
    half_adder(g1, g2)


if __name__ == "__main__":
    main()
