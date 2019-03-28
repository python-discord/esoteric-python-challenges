#IFcoltransG's heart ASCII generator. When prompted, type a number for the size of the grid of characters. A heart will be output.
from cmath import * #for when things get complex
from math import sin, cos, sqrt #for when things go back to normal

#I like to put all my functions in one place:
function_declarations = '''
print("I'm just going to use this print as another comment.")
#the main function of the code: prints heart shapes
def heart(width=0, height=None, string=" #")->None:
    #looks terrible for heart(n) where n-10<3, so only use it on 10-n<3
    global size #so we can use it inside other functions
    width = width or heart(int(input())) #heart returns None.
    height, possibilities = height or width, string
    if width is None:
        return
        #we don't want width to be none, so we don't process it when it is.
    else:
        size = width, height
    #we now know width is not none
    for x in enumerate((possibilities,)*width):
        #loops through the columns
        for y in map(lambda n:(x[~1]+n*1j, x[-1]), range(height)):
            #loops through the rows
            print(end=y[-1][-action(y)])
            #prints the correct symbol, every time.
        else:
            print()
            #newline after each row

def action(y)->bool:
    #decides what symbol to output at a specific spot in the grid.
    width, height = size
    offset = - (0.175+0.5j)
    scale = 5
    shape = 1.7
    try:
        data = y[~1] #selects the complex number portion of y
        normalised = data.real/width+data.imag/height*1j + offset
        #scales the function domain to a 1x1 square, then translates it over a bit
        value = scale*normalised
        #rescales the domain back up, so that you can see all of it on screen at once
        r,t = abs(value)+3, phase(value)-pi/2
        #Complicated maths. Especially the three. Only certain constants work in it's place, and it was terribly difficult to find one! Basically converts the complex number into polar coordinates. r is the distance between the origin and the complex number, and t is the angle to it, except with 3 and -90° added respectively
        term = 2+2*sin(t)*(sqrt(abs(cos(t)))/(sin(t) + shape) - 1)
        #I found this little thing on Wolfram Mathworld: Heart Curve 5
        assert r <3+term
        #if we've reached this point, everything is going fine, so we return a certain symbol to the printer
        return_value = False
        return return_value
    except AssertionError:
        #this means something bad has happened and we need to return the other symbol
        return_value = True
        return return_value
    finally:
        return not return_value
        #remove this bit to invert colours

#credits display function (not implemented yet):
def code_designed_by_IFcoltransG(process=print("How many columns?"))->heart():
    #insert processing here
    #I'm probably not going to finish this, because python already has a global credits variable
    return NotImplementedError and NotImplemented
    #Obviously doesn't actually return heart() like the type annotation above says.

#okay, all out functions are declared. Now we can write our actual code...
#...


'''[62:]
print(sep=exec(function_declarations))
#the exec returns None, but through force of will, we don't print it.
