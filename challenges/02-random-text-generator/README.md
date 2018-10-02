Challenge 02 - Random Text Generator

Task: Create a function that takes in a number, and returns a randomly generated string of semi-valid English.

Goal: Program that creates the most consistently coherent phrases "wins", honourable mentions for absurdly hilarious outputs

Restrictions:
* NO STRING/CHARACTER LITERALS NOR USER DEFINED STRINGS
    * That includes fancy shmancy workarounds like storing a bunch of numbers and converting them to letters
* NO FILE/USER INPUT EXCEPT LOADING STANDARD LIBRARY MODULES
* NO NON-STANDARD LIBRARY MODULES
* NO NETWORKING - AT ALL

Yep. You read that right. You'll have to look deep *inside* for some words to jumble together.

Submission guidelines:

As always, submit your code as specified in the repository's root README file. 
Ideally, submit your code with comments including some example outputs and the random seed/state needed to recreate it.
Remember that this is not a true contest, so don't hesitate to try crazy stuff. Get creative.

Tips:
* Since you can't get lists of words from the user or from outside sources, you'll have to look somewhere else.
* The Python [random](https://docs.python.org/3.7/library/random.html) module has functions that allow you to set seeds and to get/restore states. This can be useful
to generate the same output again should you come across some good results on a particular run.

Special thanks to Lemon for the idea <3


# Licensing Information

## By contributing to this repository, you understand and agree that all code in this repository is licensed under the [GNU General Public License, Version 3 (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.html). 