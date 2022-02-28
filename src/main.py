import sys
from parse import Parser

def main():

    sys.stdout.write('Begin')
    parser = Parser()
    success = parser.beginParse("testprogram.mias")
    if not success:
        sys.stderr.write('Compilation Failed.\n')
        return
    sys.stderr.write("MicroCompiler Completed Successfully\n")
    return
    
if __name__ == '__main__':
    main()
