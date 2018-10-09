section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame
	mov rax, rdi  ;rax=str
	mov r8, rsi ;r8=val
	mov r11, rdx ;r11=strl
	mov rcx, 0          ;i=0
	cmp rcx, r11        ;i-=strl
	jge .END
	
.LOOP:
	mov rbx, rax ;rbx=str
	add rbx, rcx ;str[i]
	mov [rbx], r8 ;str[i]=val
	add rcx, 1   ;i+=1
	cmp rcx, r11  ;i-=strl
	jl  .LOOP
.END:
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov rax, rdi  ;rax=dst
        mov r8, rsi ;r8=src
        mov r11, rdx ;r11=len
        mov rcx, 0         ;i=0
        cmp rcx, r11       ;i-=len
        jge .EN
        
.LO:
	mov rbx, rax ;ebx=dst
	add rbx, rcx ;dst[i]
	mov r9, rbx ;r9=dest[i]
	xor rbx, rbx
	mov rbx, [r8+rcx] ;ebx=src[i]
	mov [r9], rbx ;dst[i]=src[i]
	add rcx, 1   ;i+=1
	cmp rcx, r11 ;i-=len
	jl .LO
.EN:
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
