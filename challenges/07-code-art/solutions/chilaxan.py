print(['No '    +  'One'    ,'X','O'    ] [  (  lambda     x=
 (    lambda    f:[   f(   )      for   _   in     range(9)]
 )(   lambda    b  =  [*  range    (9)  ],  u=       [' ']\
 *9,f=[0,1]:    [(lambda    p:[p(u),    p  (b)    ])(     lambda
                a,    p=                print
 :[p('_' * 7),[p('\x1b[4m',*a[x: x + 3] ,'\x1b[0m', sep='|')for
                x in   [                0,3, 6
                ] ] ]),(                lambda     i:[u.pop(i),
                u.insert                (i,'XO'  [f[1]      -1])
                ] ) (  (                lambda   c=[0]:   [c.pop(
                ),[_ for                _   in     iter(lambda:(
                lambda i                =input(
 'XO'[f[1]-1]+': '):0if[any([0if x in map(chr,range(48,58))else
                1    for                x in i]
  )if    len(i  )else 1]  [0]else   [c  .append     (int     (i)),
    1][1]if     int(i)>=    0and  int   (i) <=8       and    ' '
     == u[      int(i) ]     else 0     )( ),1)         ],c[0]]
      [2]       )() ), (      lambda    :[f.pop           (0),
   ['/'  ],f    .insert(    0,f    [0]  )   ]if        1in[  all(
 [u[      int(  x)]=='XO'  [f       [1] -1 ]for     x in       str([


 *map(ord,'ÒřʦɶơĂ͈ö')    ][y])])for y in    range(8)] else 0)
        (),f.               append        ([0,
        2,1][               f.pop(        1)])
        ]if 0               ==f[0]        else
        f[0])               :0if x         [-1]not in[1,2]else 
                       x[-1])()],'Wins')
