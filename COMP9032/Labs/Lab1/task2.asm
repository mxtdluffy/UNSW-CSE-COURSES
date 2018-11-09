;lab1_task2.asm
;
;Created: 30/07/2018
;Author : Jingyun Shen
;

.def 	a = r17
.def 	n = r19
.def 	i = r18
.def 	anH = r21
.def 	anL = r20
.def 	sumH = r16
.def 	sumL = r15

	;ldi a, 2
	ldi i, 1
	;ldi n, 4
	mov anL, a
	ldi anH, 0
	mov sumL, a

loop:
; in the loop, we do a^n = a * a^(n-1) and sum + = a^n
; we use r5:r20 to store a^n termporaily
	cp n, i
	breq end                 ; if n == i, go to end
	mul anL, a               ; r1:r0 = a * anL
	mov r20, r0              ; a^n_L = (a^(n - 1)_L * a)_L
	mov r5, r1
	mul anH, a               ; r1:r0 = a * anH
	add r5, r0		           ; a^n_H = (a^(n - 1)_L * a)_H + (a^(n - 1)_H * a)_L
	movw r21:r20, r5:r20     ; use r21:r20 to store a^n


	add sumL, r20
	adc sumH, r21            ; sum += a^n
	inc i                    ; i += 1
	rjmp loop

end:
	rjmp end
