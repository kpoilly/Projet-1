;; FUNCTION PROTOTYPE:
;; bool validate_sequence(unsigned char message[], unsigned sequence);

;; DESCRIPTION:
;; The function generates a sequence from the message passed as parameters and checsk if it corresponds to the sequence passed as second parameter
;; The return value is stored in the eax register (0/1))

;; PARAMETERS:
;;   [ebp+8] : Address of the message array - 32 bits
;;   [ebp+12]: Hash to verify - 32 bits


;; VARIABLES: The registers have the following uses:
;;   ...

CPU     586
GLOBAL  validate_sequence
EXTERN  project
GLOBAL  check
SECTION .data
msg times 256 db 0
SECTION .text

validate_sequence:
	push ebx
	push ecx
	push edx	
	push ebp             ; Function prologue - Store value of ebp on the stack
	mov ebp, esp         ; and copy esp into ebp (since esp could change during 				       execution
        
	mov ecx, [ebp+8]     ; message
	mov edx, 0x00000000  ; c
	mov ebx, 0

	addmsg:
	  mov bl, [ecx+ebx]
	  cmp bl, 0
	  je XOR
	
	  mov [msg+ebx], bl
	  inc ebx
	  
	  jmp addmsg
	
	XOR:
	  mov ebx, 0

	loop1:
          mov ecx, [msg+ebx]     
          xor edx, ecx
	  rol edx, 8
	  add ebx, 4

	  stopcondition:
            mov ecx, [msg+ebx]
            cmp ecx, 0
            jne loop1
	    ror edx, 8

	  push edx
	  call project
	  add esp, 4

	  cmp eax, [ebp+12]
	  je true
	
	  false:
	    mov eax, 0
	    jmp end

	  true:	
	    mov eax, 1

	end:
	  mov esp, ebp     ; Function epilogue - Restore esp and ebp old values
          pop ebp
	  pop edx
	  pop ecx
	  pop ebx
	  ret

