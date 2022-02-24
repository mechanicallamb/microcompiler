"""This file contains the type D*I*C*T*I*O*N*A*R*Y for the compiler 
This file is to all for dynamic construction of classes by passing
a string of the class name to an TypeDict object which will return
the path to the class to be instantiated  


"""

import sys

class TypeDict:

    _typeList = {

        "HEADER": "HeaderSectorObj",
        "DATA": "DataSectorObj",
        "PROGRAM": "ProgramSectorObj"
    }

    def __init__(self):
        """empty so compiler doesnt complain"""

    def getObjectType(typename):
        sys.stderr.write('Reporting access of variable: ' + TypeDict._typeList[typename] + '\n')
        return TypeDict._typeList[typename]
