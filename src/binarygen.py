"""This file generates the binary/hex output to be saved to vivado memory file

A better implementation is to read a whole line of the file and break it into
several strings to be parsed instead

functions:



"""

import sys
import math
from keywords import GlobalDict
from instruction import Instruction


"""The register Binary class objects
recieve a string (or hash or register number) of an
operand register and converts it to binary if it is appropriate

inputs : REGFILE_SIZE from HEADER
"""
class BinaryGenerator:

    """Construtor (self, bitlength, hexmode)"""
    
    def __init__(self, hexmode):
        self.regAddrWidth = math.ceil(math.log2(int(GlobalDict.getValue('REGFILE_SIZE'))))
        self.dataWidth = int(GlobalDict.getValue('DATA_WIDTH'))
        self.hexmode = hexmode
        self.binOut = ""


    """Ensure that registerNum is representable by [REGISTER_SIZE] many bits"""
    def _verifyRegNumber(self, registerNum):
        if(registerNum > ((2**self.regAddrWidth)-1) or registerNum < 0):
            return False
        else:
            return True


    """Ensure that registerNumber is representable by [DATA_WIDTH] many bits"""

    def _verifyDataBitWidth(self, data):
        if(data > (2**self.dataWidth - 1) or data < 0):
            return False
        else:
            return True
    """Converts a number into a binary string
    If not in hex mode, convert to binary

    Yes, im aware the tempbin assignments could be one line
    """
    def _convertConstToBinary(self, data):
        bindata = bin(data)
        tempbin = str(bindata)[2:]
        tempbin = tempbin.zfill(self.dataWidth)
        return tempbin

    def _convertRegisterToBinary(self, data):
        bindata = bin(data)
        tempbin = str(bindata)[2:]
        tempbin = tempbin.zfill(self.regAddrWidth)
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
            self.binOut += self._convertRegisterToBinary(data)
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
            if not self._verifyDataBitWidth(data):
                return False
        binRep = self._convertConstToBinary(data)
        self.binOut += binRep
        return

    def generateLineBinary_test(self, instruction):
        regValues = []
        for string in instruction.getOperands():
            regValues.append(int(string.strip('reg$xb ')))
        self.binOut += instruction.getOpcode()
        self._generateRegisterBinary(regValues[1])
        self._generateConstBinary(regValues[2], instruction.getIsConst())
        self._generateRegisterBinary(regValues[0])
        return self.binOut
