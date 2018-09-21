import calendar
import collections
import re
import readline
import math
import random
import copy
import os
import sys

def h(s,o,n=0):
	try:
		if (type(o.__doc__)==str and not o.__doc__ in s):
			s.append(o.__doc__)
		else:
			return
	except:
		pass
	for v in dir(o):
		try:
			h(s,getattr(o,v),n)
		except:
			pass

def chunker(s):
	acc = str()
	for c in s:
		if (c.isalpha()):
			acc=acc+c
		else:
			if (acc!=str()):
				yield acc
				acc = str()
	if (acc != str()):
		yield acc


def trie(t,s):
	s = list(chunker(s))
	for w in range(1,len(s)):
		try:
			t[s[w-1]].add(s[w])
		except:
			t[s[w-1]] = set()
			t[s[w-1]].add(s[w])

def generate(start,trie,seed,n=150):
	r = random.Random()
	r.seed(seed)
	s = r.sample(start,1)[0]
	acc = []
	try:
		for x in range(n):
			acc.append(s)
			s = r.sample(trie[s],1)[0]
	except:
		pass
	return acc

s=[]
v = copy.copy(globals())
for x in v.values():
	h(s,x)
s = [str().join([c for c in x.lower() if c.isspace() or c.isalpha()]) for x in s]
t = {}
for x in s:
	trie(t,x)
start = {list(chunker(x))[0] for x in s}


for x in range(100):
	print()
	print(*generate(start,t,x))
	print()













