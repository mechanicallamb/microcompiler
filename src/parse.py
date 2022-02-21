"""This file contains the parser class which distributes 
read data to the appropriate handlers for processing

"""

import fnmatch""" for * wildcard"""
import utils.TypeDict
import sectors


class Distributer:

    def __init__():
        
        
"""A class to parse and distribute read information to appropriate handler classes

The purpose of the parser is simply to iterate over the .mias file
and give information to the proper handlers, such as a syntax manager,
keyword manager, meta data manager

"""
class Parser:

    def __init__():
        heldLine = ""
        currentSectorObj = SectorObj()

"""Hand the line to the appropriate sector object
If there is no sector object, then return
"""
    def __distribute(self):
        if not __sectorCheck(self):
            return False

    def getCurrentSector(self):
        return self.currentSectorObj

    def __checkFileType(filename):
        
    def __sectorCheck(self):


"""Generate the objects to parse each sector
The sectors will be dynamically created
and given to the parsers sectorObject which is a parent class
of each sector object
"""
    def __generateSectorObj(objType):
        
        
"""Begin parsing the .mias file
Read a line of the file and hand the read lines to the appropriate sector 
manager

The file should be completely read by the end. Return true if complete
"""
    def beginParse(self, filename):
        file = open(filename)
        if not file.endswith(".mias") or file = 0:
            return False
        for readLine in file:
            self.heldLine = file.readLine()
            if self.heldLine.find("[*]") != -1:
                __generateSectorObj(self.heldLine.strip('[]'))
            self.distribute()
        return True
