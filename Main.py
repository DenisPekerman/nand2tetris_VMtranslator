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
                arg1 = parser.arg1()
                arg2 = parser.arg2()
                if commanType == 'C_ARITHMETIC':
                    commanType = arg1
                    code.writerArithmetic(commanType) 

                elif commanType in ("C_PUSH", "C_POP"):
                    code.writePushPop(commanType, arg1, arg2)

                elif commanType == 'C_LABEL':
                    code.writeLabel(arg1)
                
                elif commanType == 'C_GOTO':
                    code.writeGoto(arg1)

                elif commanType == 'C_IF':
                    code.writeIf(arg1)

                elif commanType == 'C_FUNCTION':
                    code.writeFunction(arg1, arg2)

                elif commanType == 'C_CALL':
                    code.writeCall(arg1, arg2)
                
                elif commanType == 'C_RETURN':
                    code.writeReturn()


    
if __name__ == "__main__":

    def getAllVMfiles(fileOrFolder):
        isFile = os.path.isfile(fileOrFolder)
        if isFile:
            if fileOrFolder.endswith('.vm'):
                return [fileOrFolder]

        else: 
            files = os.listdir(fileOrFolder) 
            files = [file for file in files if file.endswith('.vm')]
            files = [os.path.join(fileOrFolder, file ) for file in files]
            return files
        
    input = sys.argv[1]
    input_files = getAllVMfiles(input)

    for file in input_files:
        print(f'proccesing {file}')
        try:
            output_path = sys.argv[2]
            input_file_name = os.path.basename(file)
        except:
            output_path = ''
            input_file_name = file

        output_file_name = input_file_name.replace('.vm', '.asm')
        output_file = os.path.join(output_path, output_file_name)

        main = Main(file, output_file)
        main.translation()
        


