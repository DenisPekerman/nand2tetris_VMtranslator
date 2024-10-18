import unittest
from MockFile import MockFile
from CodeWriter import CodeWriter 

class TestCodeWriter(unittest.TestCase):
    codeWriter = None
    
    def setUp(self) -> None:
        self.mockFile = MockFile('Banana.asm')
        self.codeWriter = CodeWriter("Foo", self.mockFile, sys_init=False)
        return super().setUp()
    

##  tests : sys.init, label, goto, if_goto, if, function, call, return, 


    def testSysInit(self):
        self.codeWriter.writeInit()
        expectedResult = [
            '@256', 
            'D=A', 
            '@SP', 
            'M=D'
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testLabel(self):
        self.codeWriter.writeLabel("LOOP")
        expectedResult = [
            '(LOOP)'
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)
    
    def testGoto(self):
        self.codeWriter.writeGoto("LOOP")
        expectedResult = [
            '@LOOP',
            '0;JMP'
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)
    
    def testIf(self):
        self.codeWriter.writeIf("LOOP")
        expectedResult = [
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            '@LOOP',
            'D;JNE'
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testFunction(self):
        self.codeWriter.writeFunction("SquareGame.new" ,"2")
        expectedResult = [
            '(SquareGame.new)',
            '@SP',
            'A=M',
            'M=0',
            '@SP',
            'M=M+1',
            '@SP',
            'A=M',
            'M=0',
            '@SP',
            'M=M+1'
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testCall(self):
        self.codeWriter.uniq_num = 17
        self.codeWriter.writeCall("SquareGame.new" ,"2")
        expectedResult = [
            '@SquareGame.new$ret.17',
            'D=A',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1',

            '@LCL',
            'D=M',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1',

            '@ARG',
            'D=M',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1',

            '@THIS',
            'D=M',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1',

            '@THAT',
            'D=M',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1',

            '@SP',
            'D=M',
            '@2',
            'D=D-A',
            '@5',
            'D=D-A',
            '@ARG',
            'M=D',

            '@SP',
            'D=M',
            '@LCL',
            'M=D',
            
            '@SquareGame.new',
            '0;JMP',
            '(SquareGame.new$ret.17)'
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testReturn(self):
        self.codeWriter.writeReturn()
        expectedResult = [
            '@LCL',
            'D=M',
            '@frame',
            'M=D',

            '@5',
            'D=D-A',
            'A=D',
            'D=M',
            '@return_address',
            'M=D',
            
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            '@ARG',
            'A=M',
            'M=D',

            '@ARG',
            'D=M+1',
            '@SP',
            'M=D',
            
            '@frame',
            'D=M-1',
            'A=D',
            'D=M',
            '@THAT',
            'M=D',
            
            '@2',
            'D=A',
            '@frame',
            'D=M-D',
            'A=D',
            'D=M',
            '@THIS',
            'M=D',

            '@3',
            'D=A',
            '@frame',
            'D=M-D',
            'A=D',
            'D=M',
            '@ARG',
            'M=D',

            '@4',
            'D=A',
            '@frame',
            'D=M-D',
            'A=D',
            'D=M',
            '@LCL',
            'M=D',

            '@return_address',
            'A=M',
            '0;JMP'
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)






if __name__ == '__main__':
    unittest.main()