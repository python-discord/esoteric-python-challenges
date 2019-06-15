# `raincat.py` by ByteCommander

This script acts similar to `lolcat` as it prints its input to the terminal in a rainbow-colored way. 
As the challenge includes code-golf, it is written as concise as possible, though surely further optimizations
could still be made.

It contains a HSV (Hue-Saturation-Value) to RGB (Red-Green-Blue) color conversion function inspired by 
https://www.rapidtables.com/convert/color/hsv-to-rgb.html so that we can easily cycle through the hue degrees
for a nice rainbow gradient.

For coloring the output, we use ANSI escape codes to display 24-bit RGB colors,
as described e.g. on https://stackoverflow.com/a/33206814/4464570.

- The first version [`raincat1.py`](/challenges/09-lolcat/solutions/bytecommander/raincat1.py) 
  only produced a plain vertical gradient and required exactly one input file path as command-line argument.
  It contains the full color conversion formula that would accept varying Saturation and Value parameters,
  but these are constantly 1 anyway.

  ![raincat1.png](/challenges/09-lolcat/solutions/bytecommander/raincat1.png)

- The second version [`raincat2.py`](/challenges/09-lolcat/solutions/bytecommander/raincat2.py)
  creates a much finer, diagonal gradient by coloring each letter individually,
  with a small hue delta per character and a slightly larger starting offset per line.
  It also takes either one single file path as command-line argument (more arguments will be ignored)
  or alternatively reads from stdin if none are given.
  The conversion function has been simplified by removing the Saturation and Value parameters.

  ![raincat2.png](/challenges/09-lolcat/solutions/bytecommander/raincat2.png)

Tested and compatible with at least Python 3.5+ on Ubuntu, using gnome-terminal.
