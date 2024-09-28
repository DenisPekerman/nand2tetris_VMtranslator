from Parser import Parser
from CodeWriter import CodeWriter
import sys
import os


class Main:
    
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
                
    def translation(self):
        file_label = os.path.basename(self.input_file)
        file_label = file_label.split('.')[0]
        parser = Parser(self.input_file)

        if not self.output_file:
            return 
        
        with open(self.output_file, 'w') as f:
            code = CodeWriter(file_label, f)
        
            while parser.advance():
                commanType= parser.commandType()
                segment = parser.arg1()
                index = parser.arg2()
                if commanType == 'C_ARITHMETIC':
                    commanType = segment
                    code.writerArithmetic(commanType) 

                if commanType in ("C_PUSH", "C_POP"):
                    code.writePushPop(commanType, segment, index)

    
if __name__ == "__main__":
    input_file = sys.argv[1]
    try:
        output_path = sys.argv[2]
    except:
        output_path = ''
    output_file = os.path.join(output_path, input_file.replace('.vm', '.asm'))
    x = Main(input_file, output_file)
    x.translation()
    
    
