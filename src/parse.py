"""This file contains the parser class which distributes 
read data to the appropriate handlers for processing

"""
"""fnmatch for wildcard"""
import fnmatch
import re
from typedict import *
from sectors import *
        
        
"""A class to parse and distribute read information to appropriate handler classes

The purpose of the parser is simply to iterate over the .mias file
and give information to the proper handlers, such as a syntax manager,
keyword manager, meta data manager

"""
class Parser:

    def __init__(self):
        self.heldLine = ""
        self.currentSectorObj = SectorObj()

        """Hand the line to the appropriate sector object
        If there is no sector object, then return

        """
        """Generate the objects to parse each sector
        The sectors will be dynamically created
        and given to the parsers sectorObject which is a parent class
        of each sector object
        """
    def _generateSectorObj(self, objType):
        self.currentSectorObj = getattr(sys.modules['sectors'], \
                                        TypeDict.getObjectType(objType))()
        
        """Begin parsing the .mias file
        Read a line of the file and hand the read lines to the appropriate sector 
        manager

        The file should be completely read by the end. Return true if complete
        """
    def beginParse(self, miasFileName):
        miasFile = open(miasFileName)
        if not miasFileName.endswith(".mias") or not miasFile:
            return False
        for readLine in miasFile:
           self.heldLine = readLine.strip()
           if(self.heldLine.find('[') >= 0 and self.heldLine.find(']') >= 0):
               self._generateSectorObj(self.heldLine.strip('[]\n'))
           elif not self.heldLine:
               continue
           else:
               self.currentSectorObj.processLine(self.heldLine)
        return True


