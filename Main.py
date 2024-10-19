from Parser import Parser
from CodeWriter import CodeWriter
import sys
import os


class Main:
    
    def __init__(self, input_file, output_file, sys_init=True):
        self.input_file = input_file
        self.output_file = output_file
        self.sys_init = sys_init

        # empty the file if it's a new run
        if sys_init:
            with open(self.output_file, 'w'):
                pass


    @staticmethod
    def getOutputPath(input_files):
        if os.path.isfile(input_files):      
            output_path = os.path.dirname(input_files)
        elif os.path.isdir(input_files):
            output_path = input_files    
        return output_path
    

    @staticmethod
    def getOutputFileName(input):
        isFile = os.path.isfile(input)
        output_file_name = os.path.basename(input)
        if isFile:
            output_file_name = output_file_name.replace('.vm', '.asm') 

        else:
            output_file_name = output_file_name + '.asm'
        return output_file_name


    @staticmethod
    def prioritizeSys(files):   
        for file in files:
            if os.path.basename(file) == 'Sys.vm':
                files.remove(file)
                files.insert(0, file)
                break
        return files


    @staticmethod
    def getAllVMfiles(fileOrFolder):
        isFile = os.path.isfile(fileOrFolder)
        if isFile:
            if fileOrFolder.endswith('.vm'):
                return [fileOrFolder]

        else: 
            files = os.listdir(fileOrFolder) 
            files = [file for file in files if file.endswith('.vm')]
            files = [os.path.join(fileOrFolder, file ) for file in files]
            files = Main.prioritizeSys(files)
            return files
                
                
    def translation(self):
        file_label = os.path.basename(self.input_file)
        file_label = file_label.split('.')[0]
        parser = Parser(self.input_file)

        if not self.output_file:
            return 
        
        with open(self.output_file, 'a') as f:
            code = CodeWriter(file_label, f, sys_init=self.sys_init)
        
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

        
    input = sys.argv[1]
    input_files = Main.getAllVMfiles(input)
    output_path = Main.getOutputPath(input)
    output_file_name = Main.getOutputFileName(input)
    output_file = os.path.join(output_path, output_file_name)
    should_init = True

    for file in input_files:
        print(f'proccesing {file}')
        main = Main(file, output_file, sys_init=should_init)
        if should_init:
            should_init = False
        main.translation()
        


