from Parser import Parser
from CodeWriter import CodeWriter
import sys




class Main:
    
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
                
    def translation(self):
        file_name = self.input_file.split('.')[0]
        parser = Parser(self.input_file)

        if not self.output_file:
            return 
        
        with open(self.output_file, 'w') as f:
            code = CodeWriter(file_name, f)
        
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
    output_file = sys.argv[2]
    x = Main(input_file, output_file)
    x.translation()
    
    
