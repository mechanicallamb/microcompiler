"""The global dict contains all global variables
This allows global variables to be added, removed, get and set
through a single interface

Perhaps have the dictionary read from a file and filled on initialization

Singleton class
"""


class GlobalDict:


    __globalDictionary = {

        "REGFILE_SIZE" : 0,
        "DATA_WIDTH" : 0,
        "OPCODE_WIDTH" : 0,
        "INSTRUC_EXTEN" : A

    }
    
    def __init__(self):
        
        """empty because compiler complains if this comment isnt here"""
        
    def setValue(self, entryKey, value):
        if not entryKey in self.globalDictionary:
            return False
        self.globalDictionary[entryKey] = value 
        return True
    
    def getValue(self, entryKey):
        return self.globalDictionary[entryKey]
    
    def getKeys(self):
        return self.globalDictionary.keys()

    def getValues(self):
        return self.globalDictionary.values()

    def getItems(self):
        return self.globalDictionary.items()

    def getDict(self):
        return self.__globalDictionary
