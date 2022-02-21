"""This file contains the type dictionary for the compiler 
This file is to all for dynamic construction of classes by passing
a string of the class name to an TypeDict object which will return
the path to the class to be instantiated  


"""

class TypeDict:

    def __init__():
        typeList = {

            'HeaderSectorObj': HeaderSectorObj,
            'DataSectorObj': DataSectorObj,
            'ProgramSectorObj': ProgramSectorObj


        }

    def getObjectType(self, typename):
        return self.typeList[typename]
    
