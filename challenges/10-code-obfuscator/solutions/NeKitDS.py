"""Weird encoder/obfuscator that came up to my mind.
The method is, for every character in a string,
convert it to two random characters like that,
so sum of ord() calls is equal to ord() of the plain character.
"""

# one-lined function for both encoding and decoding.
# compressed for more readability.
# huge thanks to chilaxan for helping with it.

string = '(lambda s,d=0:''.join([chr(sum(map(ord,c)))for c in[s[i:i+2]for i in range(0,len(s),2)]]if d else[(lambda x:chr(x)+chr(ord(c)-x))(__import__('random').randrange(0,ord(c))if ord(c)else 0)for c in s]))'

encode, decoder = eval(string), string + '({!r},1)'

if __name__ == '__main__':
    print('Evaluate the following code to get the source:', decoder.format(encode(input('Enter the code to obfuscate: '))), sep='\n')
