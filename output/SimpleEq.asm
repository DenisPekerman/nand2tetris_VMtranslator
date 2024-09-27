//C_PUSH constant 7
@7
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 7
@7
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
M=M-1
D=M
@SP
M=M-1
A=M
D=M-D
@COMP_0
D;JEQ
@SP
A=M
M=0
@END_0
0;JMP
(COMP_0)
@SP
A=M
M=-1
(END_0)
M=M+1
