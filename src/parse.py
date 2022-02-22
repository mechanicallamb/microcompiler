"""This file contains the parser class which distributes 
read data to the appropriate handlers for processing

"""
"""fnmatch for wildcard"""
import fnmatch
import typedict
import sectors
        
        
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

        """Generate the objects to parse each sector
        The sectors will be dynamically created
        and given to the parsers sectorObject which is a parent class
        of each sector object
        """
    def __generateSectorObj(objType):
        currentSectorObj = TypeDict.getObjectType(objType).__init__()
        
        """Begin parsing the .mias file
        Read a line of the file and hand the read lines to the appropriate sector 
        manager

        The file should be completely read by the end. Return true if complete
        """
    def beginParse(self, miasFileName, sectorFilename):
        file = open(miasFileName)
        if not file.endswith(".mias") or not file:
            return False
        for readLine in file:
            self.heldLine = file.readLine()
            if self.heldLine.find("[*]") != -1:
               self. __generateSectorObj(self.heldLine.strip('[]'))
            elif not heldLine:
                continue
            else:
                self.currentSectorObj.processLine(self.heldLine)
        return True


