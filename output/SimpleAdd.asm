//C_PUSH constant 7
@7
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@COMP_0
D;JEQ
@SP
A=M-1
M=0
@END_0
0;JMP
(COMP_0)
@SP
A=M-1
M=-1
(END_0)
//C_PUSH constant 9
@9
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 9
@9
D=A
@SP
A=M
M=D
@SP
M=M+1
// eq
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@COMP_1
D;JEQ
@SP
A=M-1
M=0
@END_1
0;JMP
(COMP_1)
@SP
A=M-1
M=-1
(END_1)
// and
@SP
M=M-1
A=M
D=M
A=A-1
M=D&M
