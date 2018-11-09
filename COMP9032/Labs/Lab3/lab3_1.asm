;
; AssemblerApplication1.asm
;
; Created: 4/09/2018 11:21:04 AM
; Author : Jingyun Shen & Lu Yin
;

; This program is written for COMP9032 lab3 task1
; Run three different patterns on the LED of the board consecutively.
; When the button PB0 is pressed, the pattern is hold.
.include "m2560def.inc"
.equ loop_count = 0xFFFF       ; loop_count = 65535
.def iH = r25                  ; i = r25: r24
.def iL = r24
.def countH = r17              ; count = r17:r16
.def countL = r16

rjmp main

.macro oneDelay                    ;delay the execution for 8 cyc
     ldi countL, low(loop_count)   ;set count=loop_count
     ldi countH, high(loop_count)
     clr iH                        ;clear i
     clr iL
loop:
     cp iL, countL  ;1 cyc     ;compare i with count
     cpc iH, countH  ;1 cyc
     brsh done          ;1-2 cyc   ;if i>= count,done
     adiw iH:iL, 1      ;2 cyc     ;if i<count, i+=1
     nop    ;1 cyc
     rjmp loop   ;2 cyc
done:
.endmacro

.macro halfSecondDelay   ; loop the oneDelay 30 times in order 
                         ;to achieve half-second-delay
 clr r21             ; clear r21
loop1:
 cpi r21, 15         ; compare r21 to 15
 breq done1          ; if r21 == 30, done
 oneDelay            ; else do oneDelay
 inc r21             ; r21 ++
 rjmp loop1
done1:
.endmacro

main:
     cbi DDRD, 1       ;clear bit 1 of port D
     clr r19
     out DDRD, r19     ;set PORTD for input
     ser r19
     out PORTD, r19    ;activate the pull up
     out DDRC, r19     ;set PORTC for output
mainloop:
     ldi r20, 0xAA     ;write the pattern1 of 10101010
     out PORTC, r20
     oneSecondDelay    ;delay seconds before next pattern
waiting1:
     sbis PIND, 0      ;if bit 1 of PORTD is not pressed, skip the next instruction
     rjmp waiting1     ;else keep waiting

  ldi r20, 0x55     ;write the pattern2 of 01010101
     out PORTC, r20
     oneSecondDelay    ;delay seconds before next pattern
waiting2:
      sbis PIND, 0    ;if bit 1 of PORTD is not pressed, skip the next instruction
      rjmp waiting2   ;else keep waiting
     ldi r20, 0xDD    ;write the pattern3 of 11011101
     out PORTC, r20
     oneSecondDelay   ;delay seconds before next pattern

waiting3:
     sbis PIND, 0     ;if bit 1 of PORTD is not pressed, skip the next instruction
     rjmp waiting3    ;else keep waiting

     rjmp mainloop
end:
     rjmp end
