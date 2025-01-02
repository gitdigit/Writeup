# Assembly Challenge Solution

## Challenge Description

Reverse-engineer the provided assembly code to determine:
1. What does the program compute?
2. What is the final result stored in `result` for the given input?

### Provided Code

```asm
section .data
    input db 5  

section .bss
    result resb 1

section .text
    global _start

_start:
    mov al, [input] 
    xor bl, bl 
    mov cl, al

loop_start:
    cmp cl, 0 
    je loop_end
    add bl, cl
    dec cl 
    jmp loop_start 

loop_end:
    mov [result], bl 

    ; Prepare to exit
    mov eax, 60   
    xor edi, edi   
    syscall

````

## Solution

It "suffices" to follow the instructions, starting with:

### _start
- Place the value of `input` (5) into `al`.
- `xor bl, bl` sets the `bl` register to `0`.
- Copy the value of `al` into `cl`. `cl` is now **5**.

### loop_start
- If `cl == 0`, jump to `loop_end`.
- Otherwise:
  - Add the value of `cl` to `bl` (which was initially 0).
  - Decrement `cl`.
  - Return to the beginning of the loop.

### loop_end
- When exiting `loop_start`, reach `loop_end` where the value of `bl` is copied into `result`.

`bl` will therefore hold the value **5 + 4 + 3 + 2 + 1**, which is **15**.

## Flag

````
StarHack{15}
````