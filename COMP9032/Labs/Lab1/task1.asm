;
; lab1_task1.asm
;
; Created: 30/07/2018
; Author : Jingyun Shen
;
; This asm program executes a simple loop with branch

.include "m2560def.inc"
.def	a = r16           ; define a to be register r16
.def	b = r17           ; define b to be register r17


loop:
	cp b, a				        ; compare a with b
	breq end			        ; if a == b, end the program
	brge else             ; if b >= a, go to else
	sub a, b              ; if b < a, a = a - b
	rjmp loop

else:
	sub b, a              ; if b >= a, b = b - a
	rjmp loop

end:
	rjmp end
;;;;;;;;;;;;;;;;;;;;

loop1:
   cp b, a              ; compare b with a
   brlo else1            ; if b < a go to else1
   brne else2            ; if b > a go to else2
   rjmp end

loop2:
	 cp a, b
	 brlo  else2           ; if a < b go to else2
	 brne  else1           ; if a > b go to else1
	 breq end

else1:
   sub a, b        ; if b < a, a = a - b
	 rjmp loop1

else2:
   sub b, a        ; if b > a, b = b - a
	 rjmp loop2

end:
	 rjmp end

;;;;;;;;;

	 brge else           ; if b > a, go to else
   sub a,b              ; if b < a, a = a - b
	 rjmp loop

else:
   breq end
	 sub b, a
	 rjmp loop

end:
   rjmp end
