"""This file contains the defintion of sector objects

This file needs an InstructionClass to hold the information
about an instruction

"""

import sys
from instruction import Instruction

"""Parent Class, left empty"""
class SectorObj:

    def __init__(self):

        """do nothing"""

    def processLine(self, readLine):

        """overridden"""
        
from keywords import GlobalDict

"""This object processes statements in the header sector

"""
class HeaderSectorObj(SectorObj):

    def __init__(self):
        super().__init__()
        self.globalDictRef = GlobalDict.getDict()
    
    def _getHeaderFieldValue(self, readLine):
        fieldList = readLine.strip('#')
        return fieldList

    def processLine(self, readLine):
        fieldKV = self._getHeaderFieldValue(readLine)
        splitKV = fieldKV.split(' ')
        if not GlobalDict.setValue(splitKV[0], splitKV[1]):
            """better to throw error but whatever"""
            sys.stderr.write(splitKV[0] + ' variable of type ' + type(splitKV[1]) + 'does not exist.')
            return False
        """i forget what i had here"""
        return True
        

        
    """This object processes statements in the data sector"""
class DataSectorObj(SectorObj):

    def __init__(self):
        super().__init__()
        self.globalDict = GlobalDict.getDict()
    """this class is dead for the moment"""

    def processLine(self, readLine):
        """do nothing"""



from binarygen import BinaryGenerator

"""This object processes statements in the data sector

As of 1.0, there will be no checking for hex or binary
Everything will be assumed base 10 and will be cast to lower case

1.0 does not support routines,  branching, comments, hex or octal representation

"""
class ProgramSectorObj(SectorObj):
    
    def __init__(self):
        self.resourceFilename = "/home/sean/git-repos/microcompiler/resources/opcode.txt"
        self.resourceFile = open(self.resourceFilename)
        self.globalDict = GlobalDict.getDict()
        self.currentInstruction = Instruction()
        """maybe create an instruction object"""
        constInstruction = False
        super().__init__()


    def getInstruction(self):
        return self.currentInstruction

    def getResourceFile(self):
        return self.resourceFile

    """Check if the instruction takes a constant"""
    def _checkIfConstInstruction(self):
        if '_c' in self.getInstruction().getOpcode():
            self.getInstruction().setIsConst(True)
        else:
            self.getInstruction().setIsConst(False)

    def _seekInstruction(self):
        self.resourceFile.seek(0,0)
        rfile = self.resourceFile
        for line in rfile:
            if self.getInstruction().getOpcode() in line:
                self.getInstruction().instruct = line.split(' ')[0].strip()
                self.getInstruction().setOpcode(line.split(' ')[1].strip())
                return 1
        return 0

    """Break the instruction line into individual components
    and remove all excess characters, assign members
    """
    def _conditionInstruction(self, line):
        lineList = (line.strip()).split(' ', 1)
        tempOpcode = lineList[0].strip(' ,')
        tempOperands = lineList[1].split(',')

        self.getInstruction().setOpcode(tempOpcode)
        self.getInstruction().setOperand(tempOperands[0].strip(), 0)
        self.getInstruction().setOperand(tempOperands[1].strip(), 1)
        self.getInstruction().setOperand(tempOperands[2].strip(), 2)

            
    def _hasSpecialFormatting(self, operandTuple):
        if '$' in operandTuple[0]:
            return -1
        if '$' in operandTuple[1]:
            return -1
        if '$' in operandTuple[2]:
            return 1
        return 0

    

    """Ensure operands are appropriate for instruction
    ex: there are no constants present in an instruction which
    only uses registers

    """


    def _checkForConstant(self):
        presentConstant = self._hasSpecialFormatting(self.getInstruction().getOperands())
        if presentConstant == -1:
            sys.stderr.write("Inappropriate constant operand in instruction.")
            return False
        elif presentConstant == 0:
            if self.getInstruction().getIsConst() == 0:
                self._seekInstruction()
                return True
            else:
                self.getInstruction().setOpcode(self.getInstruction().getOpcode().rstrip('_c'))
                """get the non-constant instruction"""
                if self._seekInstruction() == 1:
                    return True
                else:
                    sys.stderr.write("Non-Constant form of instruction not defined")
                    return False
        else:
            
            if self.getInstruction().getIsConst() == 1:
                self._seekInstruction()
                return True
            else:
                """get constant instruction"""
                self.getInstruction().setOpcode(self.getInstruction().getOpcode() + '_c')
                if self._seekInstruction == 1:
                    return True
                else:
                    sys.stderr.write("Constant form of instruction not defined")
                    return False

        
    
    def processLine(self, readLine):
        """condition the instruction"""
        self._conditionInstruction(readLine)
        """check for if instruction is constant"""
        self._checkIfConstInstruction()
        """check if operands are constant"""
        if not self._checkForConstant():
            return False
        binaryGenerator = BinaryGenerator(self.getInstruction().getIsConst())
        out = binaryGenerator.generateLineBinary_test(self.getInstruction())
        
        outfile = open("instruction.mbin", 'a')
        outfile.write(out)
        outfile.write('\n')
        outfile.close
        return True
