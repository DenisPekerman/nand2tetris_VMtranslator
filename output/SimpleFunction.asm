@256
D=A
@SP
M=D
// function SimpleFunction.test 2
(SimpleFunction.test)
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
@SP
M=M+1
//C_PUSH local 0
@LCL
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH local 1
@LCL
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
M=M-1
A=M
D=M
A=A-1
D=D+M
M=D
// not
@SP
A=M-1
M=!M
//C_PUSH argument 0
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
M=M-1
A=M
D=M
A=A-1
D=D+M
M=D
//C_PUSH argument 1
@ARG
D=M
@1
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=D
// RETURN
// FRAME = LCL
@LCL
D=M
@frame
M=D
// RET = *(FRAME-5)
@5
D=D-A
A=D
D=M
@return_address
M=D
// ARG = pop()
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// SP=ARG+1
@ARG
D=M+1
@SP
M=D
// THAT = *(FRAME-1)
@frame
D=M-1
A=D
D=M
@THAT
M=D
// THIS = *(FRAME-2)
@2
D=A
@frame
D=M-D
A=D
D=M
@THIS
M=D
// ARG = *(FRAME-3)
@3
D=A
@frame
D=M-D
A=D
D=M
@ARG
M=D
// LCL = *(FRAME-4)
@4
D=A
@frame
D=M-D
A=D
D=M
@LCL
M=D
// goto Ret
@return_address
A=M
0;JMP
