'''Perform a weaker Vigenère cypher, mod 256 instead of mod 26, on the bytes of the input.
   Shift key is the bytecode of inner function (lambda self,b64,iters,quine:), which is passed itself by a combinator of sorts.
   Combinator is for anonymous introspection rather than anonymous recursion.
   Output consists of the encoder function's source code, called on an encoded string, in decode mode rather than encode mode.
   When run, that source code will decode the internal string using itself, to get the original input.
   If you change the parameters in the output source code, you can switch it back into encode mode, if you want.
   Compressed into one-liner for ease of reading.'''
f=(lambda data,encode=True:(lambda f,*args:f(f,*args))((lambda self,b64,iters,quine:(bytes.decode,lambda string:f"{quine}{ascii(quine)}))(\'{b64.b64encode(string).decode()}\',False)")[encode](bytes(map(lambda base,key:(base+(encode or~encode)*key)%256,(b64.b64decode,str.encode)[encode](data),iters.cycle(self.__code__.co_code))))),*map(__import__,('base64','itertools')),'(lambda data,encode=True:(lambda f,*args:f(f,*args))((lambda self,b64,iters,quine:(bytes.decode,lambda string:f"{quine}{ascii(quine)}))(\\\'{b64.b64encode(string).decode()}\\\',False)")[encode](bytes(map(lambda base,key:(base+(encode or~encode)*key)%256,(b64.b64decode,str.encode)[encode](data),iters.cycle(self.__code__.co_code))))),*map(__import__,(\'base64\',\'itertools\')),'))

if __name__ == '__main__':
    print("Execute the following code to decode:",f(input('What would you like to encode?\n')),sep='\n')

#code by IFcoltransG
