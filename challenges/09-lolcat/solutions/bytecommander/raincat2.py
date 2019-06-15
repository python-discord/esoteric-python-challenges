import sys
def R(H):X=int(255*(1-abs((H/60)%2-1)));C=255;return[[[[[(C,0,X),(X,0,C)][H<300],(0,X,C)][H<240],(0,C,X)][H<180],(X,C,0)][H<120],(C,X,0)][H<60]
i=0
for l in open(*(sys.argv+[0])[1:2]):print("".join("\033[38;2;%d;%d;%dm"%R(h%360)+c for h,c in enumerate(l,i)),end="\033[0m");i+=8
