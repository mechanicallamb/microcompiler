"""The global D*I*C*T contains all global variables
This allows global variables to be added, removed, get and set
through a single interface

Singleton class
"""


class GlobalDict:


    _globalDictionary = {

        "REGFILE_SIZE" :int(0),
        "DATA_WIDTH" : int(0),
        "OPCODE_WIDTH" : int(0),
        "INSTRUC_EXTEN" : '0'

    }
    
    def __init__(self):
        
        """empty because compiler complains if this comment isnt here"""
        
    @staticmethod
    def setValue(entryKey, value):
        if not entryKey in GlobalDict._globalDictionary:
            return False
        GlobalDict._globalDictionary[entryKey] = value 
        return True

    @staticmethod
    def getValue(entryKey):
        return GlobalDict._globalDictionary[entryKey]

    @staticmethod
    def getKeys():
        return GlobalDict._globalDictionary.keys()

    @staticmethod
    def getValues():
        return GlobalDict._globalDictionary.values()

    @staticmethod
    def getItems():
        return GlobalDict._globalDictionary.items()

    @staticmethod
    def getDict():
        return GlobalDict._globalDictionary
