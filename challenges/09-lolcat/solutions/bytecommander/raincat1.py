import sys
h,s,v=0,1,1
def R():H=h%360;C=v*s;M=v-C;X=int(255*(M+C*(1-abs((H/60)%2-1))));C=int((C+M)*255);return[[[[[(C,0,X),(X,0,C)][H<300],(0,X,C)][H<240],(0,C,X)][H<180],(X,C,0)][H<120],(C,X,0)][H<60]
f=open(sys.argv[1])
for l in f:print(end="\033[38;2;%d;%d;%dm%%s\033[0m"%R()%l);h+=10
