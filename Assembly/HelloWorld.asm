org 0x7c00
jmp 0x0000:start

msg db ‘Hello, World!’, 10, 0

start:

xor ax, ax
mov ds, ax

mov si, msg
mov cl, 0 

printString:
lodsb                                  
cmp cl, al                             
je done

mov ah, 0xe    
mov bl, 2        
int 10h             

jmp printString

done:

jmp $

times 510 - ($ - $$) db 0
dw 0xaa55
