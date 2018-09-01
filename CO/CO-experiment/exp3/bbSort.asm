DATAS SEGMENT
	TIPS DB "Please input numbers and split them with the blamk", 0DH, 0AH, 24H
	ARRAY DW 10 DUP(0)
	ENTER DB 0DH, 0AH, 24H
	N DW 0
DATAS ENDS

STACKS SEGMENT STACK
	DW 30 DUP(?)
	TOP LABEL WORD
STACKS ENDS

CODES SEGMENT
	ASSUME SS:STACKS, DS:DATAS, CS: CODES, ES: DATAS
START:
	;段连接和赋初值
	MOV AX, STACKS
	MOV SS, AX
	LEA SP, TOP
	
	MOV AX, DATAS
	MOV DS, AX
	
	MOV AX, DATAS
	MOV ES, AX
	
	LEA DX, TIPS
	MOV AH, 9
	INT 21H
	
	LEA SI, ARRAY
	
	MOV DX, 0
	MOV BL, 10
	MOV CX, 10
	
INPUT:
	;输入函数
	MOV AH, 1
	INT 21H
	CMP AL, 20H	;与空格比较
	JZ SAVE
	
	MOV DL, AL
	MOV AX, [SI]
	MUL BL		;将al与bl相乘并存放至ax中	
	SUB DL, 30H	;将ascii码转换为10进制证书
	ADD AL, DL
	MOV [SI], AX
	JMP INPUT

SAVE:
	;将输入的数储存
	ADD SI, 2
	LOOP INPUT
	; 数据输入完毕
	
	LEA SI, ARRAY
	MOV DI, SI
	ADD DI, 2	;从第二个元素开始
	
	MOV CL, 9
	MOV CH, 9
	
CMPO:
	;每一轮两个元素之间的比较
	MOV BX, [DI]
	CMP BX, [DI-2]
	JA NEXT
	; 交换两个元素
	MOV DX, [DI-2]
	PUSH DX
	MOV [DI-2], BX
	POP DX
	MOV [DI], DX

NEXT:
	;一轮迭代
	;CH控制内层循环，CL控制外层循环
	ADD DI, 2
	DEC CH
	CMP CH, 0
	JNZ CMPO
	MOV DI, SI
	ADD DI, 2
	DEC CL
	MOV CH, CL
	CMP CL, 0
	JNZ CMPO
	; 此时已经排序完成
	
	LEA SI, ARRAY
	MOV CL, 10
	;输出回车换行
	LEA DX, ENTER
	MOV AH, 9
	INT 21H
	
	
	MOV CX, 10
	LEA SI, ARRAY
	
PRINT:
	;输出所有数字
	PUSH CX	;必须要放入堆栈，因为下面的输出函数要修改cx
	MOV AX, [SI]
    MOV BX, 10 ;10进制
	MOV CX, 0 ;初始的压栈数字为0个
	
L1:
	;初始的被除数是AX
	XOR DX, DX
    DIV BX	;除数是16位，AX储存商，DX储存余数
    PUSH DX
	INC CX ;存储压入堆栈的数字个数
    CMP AX, 0 ;如果商是0则进入L2输出
    JNE L1 ;否则继续压栈

L2:
	;依次弹出各个数字并输出
	POP DX
    ADD DX, 30H
    MOV AH, 2
    INT 21H
    LOOP L2
	
	POP CX ;弹出真正的CX值以控制循环
	ADD SI, 2
	MOV DL, 20H
	MOV AH, 2
	INT 21H
	DEC CL
	CMP CL, 0
	JNZ PRINT

;只能输出10以内的数字
;MOV DL, [SI]
;ADD DL, 30H
;MOV AH, 2
;INT 21H
;ADD SI, 2
;
;MOV DL, 20H
;MOV AH, 2
;INT 21H
;;LOOP PRINT
;DEC CL
;CMP CL, 0
;JNZ PRINT
	
EXIT:
	MOV AH, 4CH
	INT 21H
CODES ENDS
	END START
 	
	
	