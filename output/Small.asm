//C_PUSH constant 42
@42
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_PUSH constant 45
@45
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_POP that 5
@THAT
D=M
@5
D=D+A
@addr_0
M=D
@SP
M=M-1
A=M
D=M
@addr_0
A=M
M=D
//C_POP that 2
@THAT
D=M
@2
D=D+A
@addr_1
M=D
@SP
M=M-1
A=M
D=M
@addr_1
A=M
M=D
