# Option C: Chain complex abstraction of Pachner moves

from collections import defaultdict

class ChainComplex:
    def __init__(self):
        self.C0 = set()  # triangulations
        self.C1 = set()  # moves
        self.boundary = defaultdict(set)

def build_chain_complex():
    CC = ChainComplex()

    # abstract generators
    CC.C0 = {"T_n"}
    CC.C1 = {"2-3", "3-2", "1-4", "4-1"}

    # boundary operator (symbolic)
    CC.boundary["2-3"] = {"T_n"}
    CC.boundary["3-2"] = {"T_n"}
    CC.boundary["1-4"] = {"T_n"}
    CC.boundary["4-1"] = {"T_n"}

    return CC
