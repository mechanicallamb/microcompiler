"""This small class holds all the information about instructions
This helps keep things tidy and modular

This class serves only to hold information

"""

class Instruction:


    def __init__(self):
        self.opcodePositionInFile = 0
        self.isConst = False
        self.operands = [None]*3
        self.opcode = ""
        self.instruct = ""

    def getIsConst(self):
        return self.isConst

    def getOperands(self):
        return self.operands

    def getOpcode(self):
        return self.opcode

    def getOpcodePositionInFile():
        return self.opcodePositionInFile

    def setIsConst(self, newConst):
        self.isConst = newConst

    def setOperand(self, newOperands, k):
        self.operands[k] = newOperands

    def setOpcode(self, newOpcode):
        self.opcode = newOpcode.strip()

    def setOpcodePositionInFile(newPos):
        self.opcodePositionInFile = newPos
