"""This file generates the binary/hex output to be saved to vivado memory file

A better implementation is to read a whole line of the file and break it into
several strings to be parsed instead

functions:



"""

import math


"""The register Binary class objects
recieve a string (or hash or register number) of an
operand register and converts it to binary if it is appropriate

inputs : REGFILE_SIZE from HEADER
"""
class BinaryConverter:

"""Construtor (self, bitlength, hexmode)"""
    
    def __init__(self, regWidth, dataWidth, hexmode):
        self.bitlength = math.ceil(math.log2(regWidth))
        self.dataWidth = math.ceil(math.log2(dataWidth))
        self.hexmode = hexmode
        self.binOut = ""


"""Ensure that registerNum is representable by [REGISTER_SIZE] many bits"""
    def __verifyRegNumber(registerNum):
        if(registerNum > (2**bitlength-1) or registerNum < 0):
            return False
        else:
            return True


"""Ensure that registerNumber is representable by [DATA_WIDTH] many bits"""

    def __verifyDataBitWidth(data):
        if(data > (2**dataWidth - 1)):
            return False
        else:
            return True

"""Converts a number into a binary string
If not in hex mode, convert to binary
"""
    def __convertToBinary(data):
        tempbin = bin(temp)
        return tempbin

"""Convert numbers in hex or binary and return them to be written
generateBinary produces a string of hex values (if in hex mode) or 
normal binary
 In hex mode, if the number of nybbles is not even
then the leading nybble must be culled

In binary mode, the number is converted to a byte object and 
the bits are read from MSB to LSB
"""
    def __generateRegisterBinary(self, data):
        if self.__verifyRegNumber(data) == False:
            return False
        else:
            self.binOut.append(self.__convertBinary(data))
            break
        return True
    
"""Generates constant binary
if isConst = 0, make sure that register num adheres to register address restriction
if isConst = 1, make sure const adheres to max allowable constant size (DATA_WIDTH)
"""
    def __generateConstBinary(self, data, isConst):
        if isConst == 0:
            if not self.__verifyRegNumber(data):
                return False
        else:
            if not self.__verifyBitWidth(data):
                return False
        binRep = self.__convertToBinary(data)
        self.binOut.append(binRep)
        return


"""Turn an arbitrary sized list of strings to integers
Its gotten really annoying converting strings all over the place,
lets just solve that problem now instead of later
"""
    def __conditionLineToInt(stringList):
        for k in stringList:
            intList[k] = int(stringList[k])
        return intList

        

"""Convert an opcode to binary by reading opcode resource file
This function will look for the instruction keyword in a resource 
text file and grab the associated binary

Must use a predefined path to resource directory

It would be nice to have an index indicating which line to start searching
from just to avoid looping over stuff
"""
    def __generateOpcodeBinary(self, opcode):
        read = ""
        isOpcode = 0
        with open(PATH_TO_RES_DIR + "/resources/opcode.txt", "rt")\
             as opcodeFile:
            for read in opcodeFile:
                read = opcodeFile.readline()
                isOpcode = read.find(opcode, 0)
                if isOpcode == -1:
                    continue """next line"""
                elif not read:
                    opcodeFile.close()
                    return False """reached eof but not found"""
                else:
                    """found"""
                    lineTuple = read.partition('=')
                    break
                break
            self.binOut.append(lineTuple[2])
        return True


    def generateLineBinary(self, lineList, isConst):
        ints = tuple(self.__conditionLineToInts(lineList[1:3]))
        self.__generateOpcodeBinary(self, lineList[0])
        self.__generateRegisterBinary(self, ints[0])
        self.__generateConstBinary(self, ints[1], isConst)
        self.__generateRegisterBinary(self, ints[2])
        return self.binOut
