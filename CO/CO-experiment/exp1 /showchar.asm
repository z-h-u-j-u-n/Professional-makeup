DATAS SEGMENT
	;
DATAS ENDS

STACKS SEGMENT
	;
STACKS ENDS

CODES SEGMENT
	ASSUME CS:CODES, DS:DATAS, SS:STACKS
START:
	MOV ah, 1
	int 21H
	
	MOV AH, 4CH
	INT 21H
CODES ENDS
	END START