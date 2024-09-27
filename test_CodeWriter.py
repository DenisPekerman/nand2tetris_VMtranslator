import unittest
from CodeWriter import CodeWriter 

class MockFile:
    def __init__(self, filename):
        self.filename = filename
        self.content = []

    def write(self, string):
        self.content.append(string.strip())

    def read(self):
        return self.content[1:]

class TestCodeWriter(unittest.TestCase):
    codeWriter = None
    
    def setUp(self) -> None:
        self.mockFile = MockFile('Banana.asm')
        self.codeWriter = CodeWriter("Foo", self.mockFile)
        return super().setUp()
    
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""ARITHMETIC TEST""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 

    def testWrongArith(self):
        self.codeWriter.writerArithmetic("what")
        expectedResult = []
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testAdd(self):
        self.codeWriter.writerArithmetic("add")
        expectedResult = [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "A=A-1",
            "D=D+M",
            "M=D",
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testSub(self):
        self.codeWriter.writerArithmetic("sub")
        expectedResult = [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "A=A-1",
            "D=D-M",
            "M=D",
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testNegation(self):
        self.codeWriter.writerArithmetic("neg")
        expectedResult = [
            "@SP",
            "A=M-1",
            "M=-M",
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testEqual(self):
        self.codeWriter.line_number = 17
        self.codeWriter.writerArithmetic("eq")
        expectedResult = [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "A=A-1",
            "D=M-D",
            "@COMP_17",
            "D;JEQ",
            "@SP",
            "A=M-1",
            "M=0",
            "@END_17",
            "0;JMP",
            "(COMP_17)",
            "@SP",
            "A=M-1",
            "M=-1",
            "(END_17)",
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testGreaterThan(self):
        self.codeWriter.line_number = 17
        self.codeWriter.writerArithmetic("gt")
        expectedResult = [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "A=A-1",
            "D=M-D",
            "@COMP_17",
            "D;JGT",
            "@SP",
            "A=M-1",
            "M=0",
            "@END_17",
            "0;JMP",
            "(COMP_17)",
            "@SP",
            "A=M-1",
            "M=-1",
            "(END_17)",
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testLesserThan(self):
        self.codeWriter.line_number = 17
        self.codeWriter.writerArithmetic("lt")
        expectedResult = [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "A=A-1",
            "D=M-D",
            "@COMP_17",
            "D;JLT",
            "@SP",
            "A=M-1",
            "M=0",
            "@END_17",
            "0;JMP",
            "(COMP_17)",
            "@SP",
            "A=M-1",
            "M=-1",
            "(END_17)",
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testAnd(self):
        self.codeWriter.writerArithmetic("and")
        expectedResult = [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "A=A-1",
            "M=D&M",
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testOr(self):
        self.codeWriter.writerArithmetic("or")
        expectedResult = [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "A=A-1",
            "M=D|M",
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testNot(self):
        self.codeWriter.writerArithmetic("not")
        expectedResult = [
            "@SP",
            "A=M-1",
            "M=!M",
            
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""PUSH TESTS"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def testWrongPushPop(self):
        self.codeWriter.writePushPop("C_PUSH", "bomba", 3)
        expectedResult = []
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testWrongPushPop2(self):
        self.codeWriter.writePushPop("C_PUSH", "static", 'walla')
        expectedResult = []
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testPushStatic(self):
        self.codeWriter.writePushPop("C_PUSH", "static", 3)
        expectedResult = [
            "@Foo.3",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)
    
    def testPushTemp(self):
        self.codeWriter.writePushPop("C_PUSH", "temp", 2)
        expectedResult = [
            "@5",
            "D=A",
            "@2",
            "D=D+A",
            "A=D",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testPushLocal(self):
        self.codeWriter.writePushPop("C_PUSH", "local", 2)
        expectedResult = [
            "@LCL",
            "D=M",
            "@2",
            "D=D+A",
            "A=D",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testPushArg(self):
        self.codeWriter.writePushPop("C_PUSH", "argument", 2)
        expectedResult = [
            "@ARG",
            "D=M",
            "@2",
            "D=D+A",
            "A=D",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testPushThat(self):
        self.codeWriter.writePushPop("C_PUSH", "that", 2)
        expectedResult = [
            "@THAT",
            "D=M",
            "@2",
            "D=D+A",
            "A=D",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testPushThis(self):
        self.codeWriter.writePushPop("C_PUSH", "this", 2)
        expectedResult = [
            "@THIS",
            "D=M",
            "@2",
            "D=D+A",
            "A=D",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testPushPointer_1(self):
        self.codeWriter.writePushPop("C_PUSH", "pointer", 1)
        expectedResult = [
            "@THAT",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testPushPointer_0(self):
        self.codeWriter.writePushPop("C_PUSH", "pointer", 0)
        expectedResult = [
            "@THIS",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testPushConst(self):
        self.codeWriter.writePushPop("C_PUSH", "constant", 2)
        expectedResult = [
            "@2",
            "D=A",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)  


    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""POP TESTS""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""

    def testPopStatic(self):
        self.codeWriter.writePushPop("C_POP", "static", 3)
        expectedResult = [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "@Foo.3",
            "M=D",
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testPopTemp(self):
        self.codeWriter.line_number = 17
        self.codeWriter.writePushPop("C_POP", "temp", 2)
        expectedResult = [
            "@5",
            "D=A",
            "@2",
            "D=D+A",
            "@addr_17",
            "M=D",
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "@addr_17",
            "A=M",
            "M=D",
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)  

    def testPopLocal(self):
        self.codeWriter.line_number = 17
        self.codeWriter.writePushPop("C_POP", "local", 2)
        expectedResult = [
            "@LCL",
            "D=M",
            "@2",
            "D=D+A",
            "@addr_17",
            "M=D",
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "@addr_17",
            "A=M",
            "M=D",
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testPopArgument(self):
        self.codeWriter.line_number = 17
        self.codeWriter.writePushPop("C_POP", "argument", 2)
        expectedResult = [
            "@ARG",
            "D=M",
            "@2",
            "D=D+A",
            "@addr_17",
            "M=D",
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "@addr_17",
            "A=M",
            "M=D",
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testPopThat(self):
        self.codeWriter.line_number = 17
        self.codeWriter.writePushPop("C_POP", "that", 2)
        expectedResult = [
            "@THAT",
            "D=M",
            "@2",
            "D=D+A",
            "@addr_17",
            "M=D",
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "@addr_17",
            "A=M",
            "M=D",
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testPopThis(self):
        self.codeWriter.line_number = 17
        self.codeWriter.writePushPop("C_POP", "this", 2)
        expectedResult = [
            "@THIS",
            "D=M",
            "@2",
            "D=D+A",
            "@addr_17",
            "M=D",
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "@addr_17",
            "A=M",
            "M=D",
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testPopPointer_1(self):
        self.codeWriter.writePushPop("C_POP", "pointer", 1)
        expectedResult = [
            "@SP",
            "M=M-1",
            "@THAT",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    def testPopPointer_0(self):
        self.codeWriter.writePushPop("C_POP", "pointer", 0)
        expectedResult = [
            "@SP",
            "M=M-1",
            "@THIS",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
        ]
        self.assertListEqual(self.mockFile.read(), expectedResult)

    
    
    


    


if __name__ == '__main__':
    unittest.main()