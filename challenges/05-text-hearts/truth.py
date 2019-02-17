from PIL import ImageFont
from random import randint

p=lambda a:f'\033[38;5;{range(22,227,6)[int(a/256*35)]}m{chr(12448+randint(0, 90))}\033[0m'
m=ImageFont.truetype('DejaVuSans.ttf',32).getmask('\u2665')
for y in range(m.size[1]):print(''.join([p(m.getpixel((x,y)))for x in range(m.size[0])]))