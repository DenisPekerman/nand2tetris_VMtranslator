import unittest
from CodeWriter import CodeWriter 

class TestCodeWriter(unittest.TestCase):
    codeWriter = None
    
    def setUp(self) -> None:
        self.codeWriter = CodeWriter("Foo")
        return super().setUp()

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
        self.assertListEqual(self.codeWriter.hack_RAM, expectedResult)

    def testPushTemp(self):
        self.codeWriter.writePushPop("C_PUSH", "temp", 2)
        expectedResult = [
            "@2",
            "D=A",
            "@5",
            "A=D+A",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.assertListEqual(self.codeWriter.hack_RAM, expectedResult)

    def testPushLocal(self):
        self.codeWriter.writePushPop("C_PUSH", "local", 2)
        expectedResult = [
            "@2",
            "D=A",
            "@LCL",
            "A=D+M",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.assertListEqual(self.codeWriter.hack_RAM, expectedResult)

    def testPushArg(self):
        self.codeWriter.writePushPop("C_PUSH", "argument", 2)
        expectedResult = [
            "@2",
            "D=A",
            "@ARG",
            "A=D+M",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.assertListEqual(self.codeWriter.hack_RAM, expectedResult)

    def testPushThat(self):
        self.codeWriter.writePushPop("C_PUSH", "that", 2)
        expectedResult = [
            "@2",
            "D=A",
            "@THAT",
            "A=D+M",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.assertListEqual(self.codeWriter.hack_RAM, expectedResult)

    def testPushThis(self):
        self.codeWriter.writePushPop("C_PUSH", "this", 2)
        expectedResult = [
            "@2",
            "D=A",
            "@THIS",
            "A=D+M",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]
        self.assertListEqual(self.codeWriter.hack_RAM, expectedResult)

    def testPushPointer1(self):
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
        self.assertListEqual(self.codeWriter.hack_RAM, expectedResult)

    def testPushPointer0(self):
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
        self.assertListEqual(self.codeWriter.hack_RAM, expectedResult)

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
        self.assertListEqual(self.codeWriter.hack_RAM, expectedResult)


    


if __name__ == '__main__':
    unittest.main()