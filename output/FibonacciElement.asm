@256
D=A
@SP
M=D
// call Sys.init 0
//push return address
@Sys.init$ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP-n-5
@SP
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
// LCL=SP
@SP
D=M
@LCL
M=D
// goto f
@Sys.init
0;JMP
// (return-address)
(Sys.init$ret.1)
// function Sys.init 0
(Sys.init)
//C_PUSH constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Main.fibonacci 1
//push return address
@Main.fibonacci$ret.3
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP-n-5
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
// LCL=SP
@SP
D=M
@LCL
M=D
// goto f
@Main.fibonacci
0;JMP
// (return-address)
(Main.fibonacci$ret.3)
// label END
(END)
// goto END
@END
0;JMP
// function Main.fibonacci 0
(Main.fibonacci)
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
//C_PUSH constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@COMP_1
D;JLT
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
// if-goto N_LT_2
@SP
M=M-1
A=M
D=M
@N_LT_2
D;JNE
// goto N_GE_2
@N_GE_2
0;JMP
// label N_LT_2
(N_LT_2)
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
// label N_GE_2
(N_GE_2)
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
//C_PUSH constant 2
@2
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
// call Main.fibonacci 1
//push return address
@Main.fibonacci$ret.8
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP-n-5
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
// LCL=SP
@SP
D=M
@LCL
M=D
// goto f
@Main.fibonacci
0;JMP
// (return-address)
(Main.fibonacci$ret.8)
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
// call Main.fibonacci 1
//push return address
@Main.fibonacci$ret.10
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// ARG = SP-n-5
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
// LCL=SP
@SP
D=M
@LCL
M=D
// goto f
@Main.fibonacci
0;JMP
// (return-address)
(Main.fibonacci$ret.10)
// add
@SP
M=M-1
A=M
D=M
A=A-1
D=D+M
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
