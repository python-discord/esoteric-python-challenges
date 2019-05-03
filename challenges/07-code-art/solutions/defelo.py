# Usage: python3 defelo.py <size>


n=int(__import__("sys").argv[1:][0
                                ])
for(i)in[*range(n)]:p=print;c=  (i
+(                          1-  n%
2)  *(n/2<=i))%2;a,b=[[(n-  i)  //
2]  *2                  ,[  -1  +c
+i  //  2,i//2+c]][i*2  <n  ];  h\
=(  2*  7)          *(  14  +1  )\
//  2;  h=  int(h/  (2  *(  2+  1)
/2  ))  ;L  =[      1]  *(  (3  -2
)*  h)  ;(  r)=sum(L)*  (1  +1  -1
*1  /1  **              11  );  (x
)=  r;  h=chr(int(r));f=(2  +3  *2
*5  )+                      0;  (s
)=  chr(f);X=h+h+s+s;p(X*a++2*  (h
+s                              )[
c]*(n-2*[0,a][a>0]-2*b)+X[::-1]*b)

# This one has size 17
