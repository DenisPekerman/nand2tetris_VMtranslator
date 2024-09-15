
import sys 

class Parser:
    input_file = None
    line = None

    def __init__(self, filename):
        self.input_file = open(filename, "r")

    def _hasMoreLines(self):
        self.line = self.input_file.readline()
        if not self.line:
            return False
        else:
            self.line = self.line.strip()
            return True

    
    '''cleaning white space and comments'''
    def advance(self):
        while self._hasMoreLines():
            if self.line.startswith("//"): 
                continue
            if self.line.strip() == '': 
                continue
            return True
        
    def commandType(self):
        return 'COMMAND'
    
    def arg1(self):
        return 'ARG1'
    
    def arg2(self):
        return 0


  
    
