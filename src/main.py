"""This is the main file for the microcompilers

"""


import parse

def main() -> int:
    parser = Parser()
    success = parser.beginParse("test.mias")
    if not success:
        return -1
    return 0
    
