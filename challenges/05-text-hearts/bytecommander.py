"""
You said the focus isn't on golf... but I'll do it anyway.
235 bytes including imports, input, line breaks (single byte each, no trailing) and whitespace in between

The following implementation takes a single float number as parameter on STDIN, which is a size factor.
Factor 1 will produce a heart about 34 characters tall and wide, the scale is linear.
Minimum recommended factor is 0.2, below that it gets ugly.

Example: $ python3 bytecommander.py <<< .3
          
###     ###
# ### ### #
#   ###   #
#         #
##       ##
 #       # 
 ##     ## 
  ##   ##  
   #####   

This is a maths-based solution, inspired by the sixth curve on http://mathworld.wolfram.com/HeartCurve.html
  x = 16 sin³ t
  y = 13 cos t - 5 cos (2t) - 2 cos (3t) - cos (4t)
with t in [0; 2 pi]

It basically precalculates a set of up to 628 point coordinates (20*pi), rasterized to whole terminal characters according to
the entered scale factor. Then it does a simple print loop and outputs a "#" if this coordinate is in the set of points or 
else a space.
"""

# Golfed code (235 bytes):

from math import sin,cos as C
s=float(input())
P={(round(16*sin(t*.01)*s),round((C(t*.04)+2*C(t*.03)+5*C(t*.02)-13*C(t*.01)-2)*s))for t in range(628)}
R=range(min(P)[0],max(P)[0]+1)
for y in R:print("".join(" #"[(x,y)in P]for x in R))

# Ungolfed code (commented out):

"""
from math import sin, cos
scale = float(input())

points = {
    (
        # x formula:
        round(16 * sin(t * .01) * scale),
        # y formula:
        round(
            (
                cos(t * .04) + 2 * cos(t * .03) + 
                5 * cos(t * .02) - 13 * cos(t * .01) - 2
            ) * scale)
        )
    for t in range(628)  # 200 * pi
}
viewrange = range(min(points)[0], max(points)[0] + 1)

for y in viewrange:
    print("".join(" #"[(x,y) in points] for x in viewrange))
"""
