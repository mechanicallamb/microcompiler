"""This file contains the defintion of sector objects

This file needs an InstructionClass to hold the information
about an instruction

"""

"""Parent Class, left empty"""
class SectorObj:

    def __init__(self):

        """do nothing"""

    def processLine(self, readLine):

        """overridden"""
        
import globaldict

"""This object processes statements in the header sector

"""
class HeaderSectorObj(SectorObj):

    def __init__(self, globalDictRef):
        super().__init__(self)
        self.globalDictRef = globalDictRef

    
    def __getHeaderFieldValue(self, readLine):
        fieldList = readLine.strip('#')
        return fieldList

    def processLine(self, readLine):
        fieldKV = self.__getHeaderFieldValue(readLine)
        """delimit with white space"""
        fieldKV = fieldKV.split(' ')
        if not self.globalDictRef.setValue(fieldKV[0], fieldKV[1]):
            """better to throw error but whatever"""
            return False
        return True
        
        

        
    """This object processes statements in the data sector"""
class DataSectorObj(SectorObj):

    def __init__(self):
        super().__init__(self)

    """this class is dead for the moment"""


import binarygen

"""This object processes statements in the data sector

As of 1.0, there will be no checking for hex or binary
Everything will be assumed base 10 and will be cast to lower case

1.0 does not support routines, or branching

"""
class ProgramSectorObj(SectorObj):
    
    def __init__(self, fileConstructor, resourceFile):
        self.resourceFilename = resourceFile
        self.resourceFile = file()
        self.outfileConstrutor = fileConstructor
        """maybe create an instruction object"""
        constInstruction = False
        super().__init__()

    def __breakCodeLine(self, readLine):
        instructionLine = readLine.lower()
        instructionLine = instructionLine.split(' ')
        return instructionLine

    """Ensure operands are appropriate for instruction
    ex: there are no constants present in an instruction which
    only uses registers

    """
    def __validateOperands(operandList):

        """Check if an instruction exists in a resource file

        If it does, return a tuple containing the instruction and the binary opcode
        If it does not, return false and get mad
        """
    def __checkForInstruction(self, instructionString):
        resourceLine = self.resourceFile.readLine()
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
        
    def __hasSpecialFormatting(self, operandTuple):
        if '$' in operandTuple[0]:
            return -1
        if '$' in operandTuple[1]:
            return -1
        if '$' in operandTuple[2]:
            return 1
        return 0
    
    def processLine(self, readLine):
        
        programLine = self.__breakCodeLine(readLine)
        if programLine[0] == 0 or programLine[1] == 0:
            """eventually error"""
            return False   
        instruction = programLine[0]
        operands = programLine[1].split(',')
        
        """try to open resource file"""
        if not self.resourceFile:
             if not self.resourceFile.open(self.resourceFilename):
                 return False
             
        """check if instruction allows constants"""
        conditionedInstruction = self.__checkForInstruction(self, instruction)
        if not conditionedInstruction:
            return False
        
        """check if any of the operands on constants"""
        hasFormatting = self.__hasSpecialFormatting(operands)
        if formatting < 0:
            """cannot have constant in dest or source a field"""
            return False
        elif hasFormatting != self.constantInstruction:
            """search for the constant or non-constant instruction"""
            """reordering this with the assignment above would be smart"""
            if '_c' in instruction:
                instruction = instruction.removesuffix("_c")
                conditionedInstruction = self.__checkForInstruction(self, instruction)
                if not conditionedInstruction:
                    """no constant form of instruction"""
                    return False
            elif '_c'not in instruction:
                instruction = instruction + "_c"
                conditionedInstruction = self.__checkForInstruction(self, instruction)
                if not conditionedInstruction:
                    """no non-constant form of instruction"""
                    return False
            else:
                """something went wrong"""
                return False
        else:
            """do nothing"""
        
        binaryGenerator = BinaryGenerator(False, GlobalDict.getDict())
        out = binaryGenerator.generateLineBinary\
            (conditionedInstruction, operands, self.constInstruction)
        
        outfile = open("instruction.mbin", 'a')
        outfile.write(out)
        outfile.close
        return True

        
    
