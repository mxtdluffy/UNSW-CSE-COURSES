
; AssemblerApplication1.asm
;
; Created: 11/09/2018 11:08:26 AM
; Author : Comp9032
;

; Replace with your application code
;
; AssemblerApplication1.asm
;
; Created: 2018/9/10 20:57:29
; Author : Jingyun Shen & Lu Yin
;
; This program is written for COMP9032 lab3 task2
; Run three different patterns on the LED of the board consecutively.
; When the button PB0 is pressed, the pattern is hold.
; Implemented by external interrupt
.include "m2560def.inc"
.equ loop_count = 0xFFFF       ; loop_count = 65535
.equ PATTERN = 0b01010101
.def temp = r23
.def iH = r25                  ; i = r25: r24
.def iL = r24
.def countH = r17              ; count = r17:r16
.def countL = r16
                               ; set up interrupt vectors
jmp RESET
.org INT0addr                  ; defined in m2560def.inc
jmp EXT_INT0
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
.macro oneDelay                    ;delay the execution for 8 cyc
     ldi countL, low(loop_count)   ;set count=loop_count
     ldi countH, high(loop_count)
     clr iH                        ;clear i
     clr iL
loop:
     cp iL, countL   ;1 cyc     ;compare i with count
     cpc iH, countH  ;1 cyc
     brsh done       ;1-2 cyc   ;if i>= count,done
     adiw iH:iL, 1   ;2 cyc     ;if i<count, i+=1
     nop             ;1 cyc
     rjmp loop       ;2 cyc
done:
.endmacro
.macro oneSecondDelay   ; loop the oneDelay 30 times in order to achieve one-second-delay
 clr r21                ; clear r21
loop1:
 cpi r21, 30         ; compare r21 to 30
 breq done1          ; if r21 == 30, done
 oneDelay            ; else do oneDelay
 inc r21             ; r21 ++
 rjmp loop1
done1:
.endmacro
;;;;;;;;;;;;;;;;;;;;;;;;;;;;
RESET:
cbi DDRD, 1        ;clear bit 1 of port D
clr temp
out DDRD, temp     ;set PORTD for input
ser temp           ; set Port C as output
out DDRC, temp
out PORTC, temp
ldi temp, (2 << ISC00)            ; set INT0 as falling edge triggered interrupt
sts EICRA, temp
in temp, EIMSK                    ; enable INT0
ori temp, (1 << INT0)
out EIMSK, temp
sei                               ; enable Global Interrupt
jmp main

;;;;;;;;;;;;;;;;;;;;;;;;;;
EXT_INT0:
in temp, SREG          ; save SREG
push temp
sbic PIND, 0      ;if bit 1 of PORTD is not pressed, skip the next instruction
rjmp continue
waiting:
  sbic PIND, 1
     rjmp waiting      ;else keep waiting
continue:
out SREG, temp
pop temp
reti
;;;;;;;;;;;;;;;;;;;;;;;;;
main:
ldi r20, 0xAA     ;write the pattern1 of 10101010
out PORTC, r20
oneSecondDelay    ;delay 1 second before next pattern

ldi r20, 0x55     ;write the pattern2 of 01010101
out PORTC, r20
oneSecondDelay    ;delay 1 second before next pattern
ldi r20, 0xDD     ;write the pattern3 of 11011101
out PORTC, r20
oneSecondDelay    ;delay 1 second before next pattern
rjmp main
;;;;;;;;;;;;;;;;;;;;;;;
