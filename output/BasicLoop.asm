@256
D=A
@SP
M=D
//C_PUSH constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//C_POP local 0
@LCL
D=M
@0
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
// label LOOP
(LOOP)
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
// add
@SP
M=M-1
A=M
D=M
A=A-1
D=D+M
M=D
//C_POP local 0
@LCL
D=M
@0
D=D+A
@addr_4
M=D
@SP
M=M-1
A=M
D=M
@addr_4
A=M
M=D
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
//C_PUSH constant 1
@1
D=A
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
//C_POP argument 0
@ARG
D=M
@0
D=D+A
@addr_6
M=D
@SP
M=M-1
A=M
D=M
@addr_6
A=M
M=D
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
// if-goto LOOP
@SP
M=M-1
A=M
D=M
@LOOP
D;JNE
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
