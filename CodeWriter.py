
# Register indices
RAM_SP = 0      # Stack pointer
RAM_LCL = 1     # Local segment base address
RAM_ARG = 2     # Argument segment base address
RAM_THIS = 3    # THIS segment base address
RAM_THAT = 4    # THAT segment base address

# Temp segment (addresses 5–12)
RAM_TEMP = 5

# General purpose registers (addresses 13–15)
RAM_R13 = 13
RAM_R14 = 14
RAM_R15 = 15

# Static variables start at address 16
RAM_STATIC = 16

# Stack start at address 256
RAM_STACK = 256

# End of the RAM (address 2047)
RAM_STACK_END = 2047

class CodeWriter:
    def __init__(self, input_file_name):
        #   self.output_file = output_file
        self.hack_RAM = []
        self.file_name = input_file_name
            
    def writerArithmetic(self, c_arithmetic):
        
        pass



    def writePushPop(self, command, segment, index):

#push temp, local, argument, that, this:
#@index              Load the address of the variable at 'index' into the A register
#D=A                 Store the address in the D register
#@segment            Load the address of the segment into the A register
#A=D+(value_to_add)  Set the A register to the address of `D + (A(segment-adress) + index)' OR 'D + (M(segment-content) + index')
#D=M                 Load the value at the calculated address into the D register
#@SP                 Load the address of the stack pointer into the A register
#A=M                 Dereference the stack pointer to access the top of the stack
#M=D                 Store the value from D into the top of the stack
#@SP                 Load the address of the stack pointer into the A register again
#M=M+1               Increment the stack pointer to point to the next empty position

#push: static
# @{self.file_name}{index}  Access static variable indexed by {index}, where {self.file_name} is the VM file name
# D=M                       Load the value of static[index] into register D
# @SP                       Access the stack pointer (SP)
# A=M                       Set A to the address where SP is pointing (top of the stack)
# M=D                       Store the value from D (static[index]) at the top of the stack
# @SP                       Access the stack pointer (SP) again
# M=M+1                     Increment the stack pointer to point to the next available space on the stack

#push pointer:
# @THAT/THIS     When pointer's index is 1/0 access the THAT/THIS register
# D=M            Load the value of THAT/THIS into register D
# @SP            Access the stack pointer (SP)
# A=M            Set A to the address where SP is pointing (top of the stack)
# M=D            Store the value from D (THAT/THIS) at the top of the stack
# @SP            Access the stack pointer (SP) again
# M=M+1          Increment the stack pointer to point to the next available space on the stack

#push constant:
# @index                Load the address of the variable at 'index'
# D=A                   Store the address in D
# @SP                   Load the stack pointer address
# A=M                   Set A to the value of the stack pointer (top of the stack)
# M=D                   Store the value from D(index) into the top of the stack
# @SP                   Load the stack pointer address again
# M=M+1                 Increment the stack pointer to point to the next empty slot

#pop:
#@index              Load the address of the variable at 'index' into the A register
#D=A                 Store the address in the D register
#@segment            Load the address of the segment into the A register
#A=D+(value_to_add)  Set the A register to the address of `D + (A(segment-adress) + index)' OR 'D + (M(segment-content) + index')
#D=M                 Load the value at the calculated address into the D register
#@SP                 Load the address of the stack pointer into the A register again
#M=M-1               Decrement the stack pointer to point to the previous position
#@SP                 Load the address of the stack pointer into the A register
#A=M                 Dereference the stack pointer to access the top of the stack
#M=D                 Store the value from D into the top of the stack


        if command == 'C_PUSH':
            if segment == 'static':
                self.hack_RAM.append(f'@{self.file_name}.{index}')
                self.hack_RAM.append('D=M')
                self.hack_RAM.append('@SP')
                self.hack_RAM.append('A=M')
                self.hack_RAM.append('M=D')
                self.hack_RAM.append('@SP')
                self.hack_RAM.append('M=M+1')
                        
            elif segment == 'temp':
                self._pushPopHelper(index, RAM_TEMP, "A")
                
            elif segment == 'local':
                self._pushPopHelper(index, 'LCL', "M")

            elif segment == 'argument':
                self._pushPopHelper(index, 'ARG', "M")

            elif segment == 'that':
                self._pushPopHelper(index, 'THAT', 'M')

            elif segment == 'this':
                self._pushPopHelper(index, 'THIS', 'M')

            elif segment == 'pointer':
                if index == 1:
                    self.hack_RAM.append("@THAT")
                else:
                    self.hack_RAM.append("@THIS")
                self.hack_RAM.append("D=M")
                self.hack_RAM.append("@SP")
                self.hack_RAM.append("A=M")
                self.hack_RAM.append("M=D")
                self.hack_RAM.append("@SP")
                self.hack_RAM.append("M=M+1")

            elif segment == 'constant':
                self.hack_RAM.append(f'@{index}')
                self.hack_RAM.append('D=A')
                self.hack_RAM.append('@SP')               
                self.hack_RAM.append('A=M')
                self.hack_RAM.append('M=D')
                self.hack_RAM.append('@SP')
                self.hack_RAM.append('M=M+1')

        # if command == 'C_POP':

        #     if segment == 'local':



    
    def _pushPopHelper(self, index, segment, value_to_add):
        self.hack_RAM.append(f'@{index}')
        self.hack_RAM.append('D=A')
        self.hack_RAM.append(f'@{segment}')
        self.hack_RAM.append(f'A=D+{value_to_add}')
        self.hack_RAM.append('D=M')
        self.hack_RAM.append('@SP')               
        self.hack_RAM.append('A=M')
        self.hack_RAM.append('M=D')
        self.hack_RAM.append('@SP')
        self.hack_RAM.append('M=M+1')

    
        
                    
               
               
if __name__ == "__main__":
     x = CodeWriter('test-file')
     x.writePushPop('C_PUSH', 'static', '3')
     print('\n'.join(x))
    
     


          