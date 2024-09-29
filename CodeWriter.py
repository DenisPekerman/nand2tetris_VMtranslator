from typing import TextIO


"""This module consists of two main functions.

writeArithmetic translates arithmetic operations: 
add, sub, neg, eq, gt, lt, and, or not.

writePushPop translates push and pop commands: 
push/pop local,argument,this,that,temp,static,pointer,constant.

details regarding assembly commands can be found at assemblyDetail.txt"""

class CodeWriter:
    output_file: TextIO

    def __init__(self, input_file_name: str, output_file: TextIO):
        self.hack_RAM = []
        self.input_file = input_file_name
        self.output_file = output_file
        self.line_number = 0

    def writerArithmetic(self, command):
        self._output(f'// {command}')
        if command == 'add':
            self._addSubOperator('+')

        elif command == 'sub':
            self._addSubOperator('-')

        elif command == 'neg':
            self._output("@SP")
            self._output("A=M-1")
            self._output("M=-M")
            
        elif command == 'eq':
            self._comparisonOperator('JEQ')

        elif command == 'gt':
            self._comparisonOperator('JGT')
        
        elif command == 'lt':
            self._comparisonOperator('JLT')

        elif command == 'and':
            self._andOrOperator('&')

        elif command == 'or':
            self._andOrOperator('|')

        elif command == 'not':
            self._output("@SP")
            self._output("A=M-1")
            self._output("M=!M")
    
        self.line_number += 1


    def writePushPop(self, command, segment, index):
        try:
            int(index)
        except:
            print('INDEX ERROR', index)
            return 
        self._output(f'//{command} {segment} {index}')

        if command == 'C_PUSH':
            if segment == 'static':
                self._output(f'@{self.input_file}.{index}')
                self._output('D=M')
                self._storeAndIncrement()
                
            elif segment == 'temp':
                self._pushPopHelper('5', 'A', index)
                self._output('A=D')
                self._output('D=M')
                self._storeAndIncrement()
                
            elif segment == 'local':
                self._pushPopHelper('LCL', 'M', index)
                self._output('A=D')
                self._output('D=M')
                self._storeAndIncrement()

            elif segment == 'argument':
                self._pushPopHelper("ARG", 'M', index)
                self._output('A=D')
                self._output('D=M')
                self._storeAndIncrement()

            elif segment == 'that':
                self._pushPopHelper("THAT", 'M', index)
                self._output('A=D')
                self._output('D=M')
                self._storeAndIncrement()

            elif segment == 'this':
                self._pushPopHelper("THIS", 'M', index)
                self._output('A=D')
                self._output('D=M')
                self._storeAndIncrement()

            elif segment == 'pointer':
                if index == '1':
                    self._output("@THAT")
                elif index == '0':
                    self._output("@THIS")
                self._output("D=M")
                self._storeAndIncrement()

            elif segment == 'constant':
                self._output(f'@{index}')
                self._output('D=A')
                self._storeAndIncrement()


        if command == 'C_POP':
            if segment == 'static':
                self._output('@SP')
                self._output('M=M-1')
                self._output('A=M')
                self._output('D=M')
                self._output(f'@{self.input_file}.{index}')
                self._output('M=D')

            if segment == 'temp':
                self._pushPopHelper('5', 'A', index)
                self._popHelper()

            if segment == 'local':
                self._pushPopHelper("LCL", 'M', index)
                self._popHelper()

            if segment == 'argument':
                self._pushPopHelper("ARG", 'M', index)
                self._popHelper()

            if segment == 'that':
                self._pushPopHelper('THAT', 'M', index)
                self._popHelper()

            if segment == 'this':
                self._pushPopHelper('THIS', 'M', index)
                self._popHelper()

            if segment == 'pointer':
                self._output('@SP')
                self._output('M=M-1')
                self._output('A=M')
                self._output('D=M')
                if index == '1': 
                    self._output('@THAT')
                if index == '0':
                    self._output('@THIS')
                self._output('M=D')

            self.line_number += 1


    def _pushPopHelper(self, segment, value_to_add, index):
        self._output(f'@{segment}')
        self._output(f'D={value_to_add}')
        self._output(f'@{index}')
        self._output('D=D+A')

    def _popHelper(self):
        self._output(f'@addr_{self.line_number}')
        self._output('M=D')
        self._output('@SP')
        self._output('M=M-1')
        self._output('A=M')
        self._output('D=M')
        self._output(f'@addr_{self.line_number}')
        self._output('A=M')
        self._output('M=D')

    def _storeAndIncrement(self):
        self._output('@SP')               
        self._output('A=M')
        self._output('M=D')
        self._output('@SP')
        self._output('M=M+1')

    def _comparisonOperator(self, type):
        self._output("@SP")
        self._output("M=M-1")
        self._output("A=M")
        self._output("D=M")
        self._output("A=A-1")
        self._output("D=M-D")
        self._output(f"@COMP_{self.line_number}")
        self._output(f"D;{type}")
        self._output("@SP")
        self._output("A=M-1")
        self._output("M=0")
        self._output(f"@END_{self.line_number}")
        self._output("0;JMP")
        self._output(f"(COMP_{self.line_number})")
        self._output("@SP")
        self._output("A=M-1")
        self._output("M=-1")
        self._output(f"(END_{self.line_number})")

    def _addSubOperator(self, operator):
        self._output("@SP")
        self._output("M=M-1")
        self._output("A=M")
        self._output("D=M")
        self._output("A=A-1")
        if operator == '+':
            self._output("D=D+M")
        elif operator == '-':
            self._output("D=M-D")
        self._output("M=D")
        
    def _andOrOperator(self, operator):
        self._output("@SP")
        self._output("M=M-1")
        self._output("A=M")
        self._output("D=M")
        self._output("A=A-1")
        self._output(f"M=D{operator}M")

    def _output(self, line):
        self.output_file.write(line+'\n')



    
        
                    
               
               
if __name__ == "__main__":
     x = CodeWriter('test-file')
     x.writePushPop('C_PUSH', 'static', '3')
     print('\n'.join(x))
    
     


          