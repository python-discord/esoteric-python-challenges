# Stack-Based Esolang Based On NANDs
# Documentation and Examples at github.com/EdgyNerd/Nandy


from textwrap import wrap

def NANDy(prog, inp=''):
    inp = ''.join(format(ord(x), 'b').zfill(8) for x in inp)
    stack = [0]
    progPos=0
    loops = []
    output=''
    while True:
        i = prog[progPos]
        if i==':':
            stack+=[stack[-1]]
        elif i=='#':
            stack+=[(stack.pop()&stack.pop())^1]
        elif i=='>':
            stack.insert(0,stack.pop())
        elif i=='<':
            stack+=[stack[0]]
            del stack[0]
        elif i=='(':
            if stack[-1]>0:
                loops+=[progPos]
            else:
                while True:
                    a=1
                    progPos+=1
                    if prog[progPos]=='(':
                        a+=1
                    elif prog[progPos]==')':
                        a-=1
                        if a==0:
                            break
        elif i==')':
            if stack[-1]>0:
                progPos=loops[-1]
            else:
                loops.pop()
        elif i=='i':
            if inp=='':
                stack+=[0]
            else:
                stack+=[inp[0]]
                inp=inp[1:]
        elif i=='o':
            output+=str(stack[-1])
        if progPos==len(prog)-1:
            break
        progPos+=1
    output = wrap(output, 8)
    for i in output:
        print(chr(int(i,2)), end='')

NANDy('ioioioioioioioio', 'a')
