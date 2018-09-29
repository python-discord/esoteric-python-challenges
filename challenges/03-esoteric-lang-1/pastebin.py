"""
An esoteric bytecode-ish language.
Eevery operator has one operand except for 5 which has two
0 outputs the operand as an ascii character
1 jumps to the operand (starting from 0)
2 does nothing
3 deletes the first 128 bytes of the program and is the only way to jump to parts of the program more than 255 bytes
4 takes input (one character) and writes it to the program at the operand (starting from 0)
5 writes the second operand to the first (starting from 0)
The program's only memory is the program itself, with only 256 addressable bytes.

b'\1\4\0\0\4\3\1\2' is a cat program that writes the input character to an output instruction.
0: jump to 4
2: output 3
4: write input to 3
6: jump to 2

Now try writing a language that compiles to this :]
"""

execute = lambda b,i=0,line='':(execute(b,b[i+1],line) if b[i]==1 else execute(b,i+2,line)if b[i]==2 else execute(b[128:],i+2,line)if b[i]==3 else(lambda l:execute(b[:b[i+1]]+l[0].encode()+b[b[i+1]+1:],i+2,l[1:]))(line if line else input()+'\n')if b[i]==4 else execute(b[:b[i+1]]+bytes([b[i+2]])+b[b[i+1]+1:],i+3,line)if b[i]==5 else 1/0 if b[i]else(print(chr(b[i+1]),end=''),execute(b,i+2,line))