"""This file generates the binary/hex output to be saved to vivado memory file

A better implementation is to read a whole line of the file and break it into
several strings to be parsed instead

functions:



"""

import sys
import math
from keywords import GlobalDict


"""The register Binary class objects
recieve a string (or hash or register number) of an
operand register and converts it to binary if it is appropriate

inputs : REGFILE_SIZE from HEADER
"""
class BinaryGenerator:

    """Construtor (self, bitlength, hexmode)"""
    
    def __init__(self, hexmode):
        self.bitlength = math.ceil(math.log2(int(GlobalDict.getValue('REGFILE_SIZE'))))
        self.dataWidth = math.ceil(math.log2(int(GlobalDict.getValue('DATA_WIDTH'))))
        self.hexmode = hexmode
        self.binOut = ""


    """Ensure that registerNum is representable by [REGISTER_SIZE] many bits"""
    def _verifyRegNumber(self, registerNum):
        if(registerNum > (2**self.bitlength-1) or registerNum < 0):
            return False
        else:
            return True


    """Ensure that registerNumber is representable by [DATA_WIDTH] many bits"""

    def _verifyDataBitWidth(self, data):
        if(data > (2**self.dataWidth - 1)):
            return False
        else:
            return True

    """Converts a number into a binary string
    If not in hex mode, convert to binary
    """
    def _convertToBinary(self, data):
        tempbin = bin(data)
        return tempbin

    """Convert numbers in hex or binary and return them to be written
    generateBinary produces a string of hex values (if in hex mode) or 
    normal binary
    In hex mode, if the number of nybbles is not even
    then the leading nybble must be culled

    In binary mode, the number is converted to a byte object and 
    the bits are read from MSB to LSB
    """
    def _generateRegisterBinary(self, data):
        if self._verifyRegNumber(data) == False:
            return False
        else:
            self.binOut += self._convertToBinary(data)
        return True
    
    """Generates constant binary
    if isConst = 0, make sure that register num adheres to register address restriction
    if isConst = 1, make sure const adheres to max allowable constant size (DATA_WIDTH)
    """
    def _generateConstBinary(self, data, isConst):
        if isConst == 0:
            if not self._verifyRegNumber(data):
                return False
        else:
            if not self._verifyBitWidth(data):
                return False
        binRep = self._convertToBinary(data)
        self.binOut += binRep
        return


    """Turn an arbitrary sized list of strings into integers
    Its gotten really annoying converting strings all over the place,
    lets just solve that problem now instead of later
    """
    def _conditionLineToInt(self, stringList):
        intList = []
        for k in range(len(stringList)):
            if stringList[k].find('$') >= 0:
                strippedRegister = stringList[k].lstrip('$')
            else:
                strippedRegister = stringList[k].lstrip('reg')
            intList.append(int(strippedRegister))
        return intList

        

    """Convert an opcode to binary by reading opcode resource file
    This function will look for the instruction keyword in a resource 
    text file and grab the associated binary

    Must use a predefined path to resource directory

    It would be nice to have an index indicating which line to start searching
    from just to avoid looping over stuff
    """
    def _generateOpcodeBinary(self, opcode):
        
        read = ""
        isOpcode = 0
        with open(PATH_TO_RES_DIR + "~git-repos/microcompiler/resources/opcode.txt", "rt")\
             as opcodeFile:
            for read in opcodeFile:
                isOpcode = read.find(opcode, 0)
                if isOpcode == -1:
                    """next line"""
                    continue
                elif not read:
                    """reached eof but not found"""
                    opcodeFile.close()
                    return False 
                else:
                    """found"""
                    lineTuple = read.partition('=')
            self.binOut += lineTuple[2]
        return True


    def generateLineBinary(self, opcode, lineList, isConst):
        registerList = (lineList.strip()).split(', ')
        regValues = tuple(self._conditionLineToInt(registerList))

        """append the binary portion of the opcode"""
        self.binOut += opcode[1]
        self._generateRegisterBinary(regValues[0])
        self._generateConstBinary(regValues[1], isConst)
        self._generateRegisterBinary(regValues[2])
        return self.binOut
