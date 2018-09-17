"""
Submission by Joseph

Notes:
Solution only works on certain environments and requires the 'bc' package to be installed
"""

next(c for c in object.__subclasses__()if'ModuleLock'in str(c)).acquire.__globals__['sys'].modules['os'].execvp("dc",("dc","-e",input()+"p"))
