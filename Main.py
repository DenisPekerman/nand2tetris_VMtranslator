from Parser import Parser
from CodeWriter import CodeWriter
import sys



class Main:
    
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.asm_out = []
                
    def translation(self):
        parser = Parser(self.input_file)
        while parser.advance():
            command = parser.commandType()
            arg1 = parser.arg1()
            arg2 = parser.arg2()
            if arg1 == 'C_ARITHMETIC':
                self.asm_out.append(arg1)
            elif arg1 != 'C_ARITHMETIC':
                self.asm_out.append('{} {}'.format(arg1, arg2))
            
    def out_file(self):
        with open(output_file, 'w') as out_file:
            joined_output = '\n'.join(self.asm_out)
            out_file.write(joined_output)



if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    x = Main(input_file, output_file)
    x.translation()
    x.out_file()
    
