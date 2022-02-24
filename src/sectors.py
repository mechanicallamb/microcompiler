"""This file contains the defintion of sector objects

This file needs an InstructionClass to hold the information
about an instruction

"""

import sys

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
        sys.stderr.write('Header Sector processing')
        fieldKV = self._getHeaderFieldValue(readLine)
        splitKV = fieldKV.split(' ')
        if not GlobalDict.setValue(splitKV[0], splitKV[1]):
            """better to throw error but whatever"""
            sys.stderr.write(splitKV[0] + ' variable of type ' + type(splitKV[1]) + 'does not exist.')
            return False
        return True
        
        

        
    """This object processes statements in the data sector"""
class DataSectorObj(SectorObj):

    def __init__(self):
        super().__init__()
        self.globalDict = GlobalDict.getDict()
    """this class is dead for the moment"""

    def processLin(self, readLine):
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
        """maybe create an instruction object"""
        constInstruction = False
        super().__init__()

    def _breakCodeLine(self, readLine):
        instructionLine = readLine.lower()
        splitLine = instructionLine.split(' ',1)
        return splitLine

    """Ensure operands are appropriate for instruction
    ex: there are no constants present in an instruction which
    only uses registers

    """
    def _validateOperands(self, operandList):

        """Check if an instruction exists in a resource file

        If it does, return a tuple containing the instruction and the binary opcode
        If it does not, return false and get mad
        """
    def _checkForInstruction(self, instructionString):
        resourceLine = self.resourceFile.readline().strip()
        if instructionString in resourceLine:
            breakLine = resourceLine.partition(' ')
            if '_c' in breakLine[0]:
                self.constInstruction = True
            else:
                self.constInstruction = False
            return breakLine
        elif resourceLine == 0:
            return breakLine == 0
        else:

            """Ensures that all operands are appropriate

            As of 1.0, only checks for $(decimal constant)
            """
        
    def _hasSpecialFormatting(self, operandTuple):
        if '$' in operandTuple[0]:
            return -1
        if '$' in operandTuple[1]:
            return -1
        if '$' in operandTuple[2]:
            return 1
        return 0
    
    def processLine(self, readLine):
        sys.stderr.write('Program sector obj processing line\n')
        programLine = self._breakCodeLine(readLine)
        if programLine[0] == 0 or programLine[1] == 0:
            sys.stderr.write('Instruction has no instruction or destination register\n')
            return False  
        instruction = programLine[0]
        operands = programLine[1]
        
        """try to open resource file"""
        if not self.resourceFile:
             if not self.resourceFile.open(self.resourceFilename):
                 sys.stderr.write('Resource file ' + self.resourceFile + ' is not available\n')
                 return False
             
        """check if instruction allows constants"""
        conditionedInstruction = self._checkForInstruction(instruction)
        if not conditionedInstruction:
            sys.stderr.write('Attempted to pass constant operand when instruction'\
            'does not allow constants\n')
            return False
        
        """check if any of the operands on constants"""
        hasFormatting = self._hasSpecialFormatting(operands)
        if hasFormatting < 0:
            """cannot have constant in dest or source a field"""
            sys.stderr.write('Constant not allowed in destination or Source A field')
            return False
        elif hasFormatting != self.constInstruction:
            """search for the constant or non-constant instruction"""
            """reordering this with the assignment above would be smart"""
            if '_c' in instruction:
                instruction = instruction.removesuffix("_c")
                conditionedInstruction = self._checkForInstruction(instruction)
                if not conditionedInstruction:
                    """no constant form of instruction"""
                    sys.stderr.write('Instruction does not support constant operands.')
                    return False
            elif '_c'not in instruction:
                instruction = instruction + "_c"
                conditionedInstruction = self._checkForInstruction(instruction)
                if not conditionedInstruction:
                    """no non-constant form of instruction"""
                    sys.stderr.write('Instruction only supports constant operands')
                    return False
            else:
                """something went wrong"""
                sys.stderr.write('Unknown error occurred')
                return False
        else:
            """do nothing"""

        sys.stderr.write('Generating binary...\n')
        binaryGenerator = BinaryGenerator(False)
        out = binaryGenerator.generateLineBinary\
            (conditionedInstruction, operands, self.constInstruction)
        
        outfile = open("instruction.mbin", 'a')
        outfile.write(out)
        outfile.close
        return True

        
    
