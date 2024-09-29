import re

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
        
    """Command clasification"""
    def commandType(self):
        arg_pattern = r'^(label|goto|if|push|pop|function|call)\b'
        arithmetic_pattern = r'^(add|sub|neg|eq|gt|lt|and|or|not)\b$'

        arg_match = re.match(arg_pattern, self.line)
        arith_match = re.match(arithmetic_pattern, self.line)
       
        if arith_match:
            return 'C_ARITHMETIC'
        elif arg_match:
            return 'C_{}'.format(arg_match.group(1).upper())        
            
    """if not arithmetic return the segment part of a command. if arithmetic return the command"""
    def arg1(self):
        command_type = self.commandType()
        if command_type not in ('C_RETURN', 'C_ARITHMETIC'):
            arg = self.line.split()
            return arg[1]
        elif command_type == 'C_ARITHMETIC':
            return self.line[:]

    """return the index part of a command"""
    def arg2(self):
        commamnd_type = self.commandType()
        if commamnd_type in ('C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL'):
            arg = self.line.split()
            return arg[2]

       


  
    
