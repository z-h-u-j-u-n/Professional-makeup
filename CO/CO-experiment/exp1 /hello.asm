DATAS SEGMENT
	STRING  DB 1,10,"Hello World!",13,10,'$'
    ;此处输入数据段代码  
DATAS ENDS



CODES SEGMENT
    ASSUME CS:CODES,DS:DATAS
START:
    MOV AX,DATAS
    MOV DS,AX
    LEA DX,STRING
    MOV AH,9
    INT 21H
    MOV AH,4CH
    INT 21H
CODES ENDS
    END START

