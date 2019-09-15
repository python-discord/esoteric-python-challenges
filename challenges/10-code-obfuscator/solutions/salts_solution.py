#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:27:08 2019
@author: salt

This obfuscation isn't too esoteric, but it's fun nonetheless:
    We convert our string into an image with imagemagick.
    We convert the image into a numpy array.
    We use the numpy array as an adjacency matrix to make a graph.
    The dictionary (of dictionaries) of the graph is our obfuscated string.

For the input "testing" we have:


>>> obfuscated_string[10]

{0: 1, 1: 1, 2: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 14: 1, 15: 1,
 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1,
 31: 1, 32: 1, 33: 1, 34: 1, 35: 1, 36: 1, 37: 1, 38: 1, 41: 1, 42: 1, 43: 1,
 44: 1, 45: 1, 46: 1, 49: 1, 50: 1, 51: 1, 52: 1, 53: 1, 54: 1, 55: 1, 57: 1,
 58: 1, 59: 1, 60: 1, 61: 1, 62: 1, 66: 1, 67: 1, 68: 1, 69: 1, 70: 1, 71: 1,
 72: 1, 73: 1, 75: 1, 76: 1, 77: 1, 78: 1, 79: 1, 80: 1, 83: 1, 84: 1, 85: 1,
 86: 1, 87: 1, 88: 1, 89: 1, 90: 1, 94: 1, 95: 1, 96: 1, 97: 1, 98: 1, 99: 1}


We can work backwards to get our original string :
    Make a graph with our dictionary.
    Save graph's adjacency matrix as numpy array.
    Convert numpy array into an image.
    Use OCR to read the image as a string.

There's a catch, of course.  OCR isn't perfect: You may end up with missing or
wrong characters.  I also doubt this qualifies as "keeping functionality
intact", but I enjoyed it.
"""

import subprocess
import numpy as np
from PIL import Image
import networkx as nx
import pytesseract

graph_order_and_image_dim = 100 #Increase for long strings

def obfuscator(a_string):
    filename = a_string.replace(" ", "_") + ".png"

    #Create an image of our string using Imagemagick -- image must be square
    subprocess.run(["convert", "-background","white", "-fill", "black",
                    "-size",
                    f"{graph_order_and_image_dim}x{graph_order_and_image_dim}",
                    "caption:" + a_string, filename])

    #Turn our image into a numpy array
    string_as_image = Image.open(filename)
    string_as_array = np.array(string_as_image)
    #We just need an array of 1's and 0's
    string_as_array[string_as_array > 0] = 1

    #Turn our array into a graph by treating it as an adjacency matrix
    string_as_graph = nx.from_numpy_array(string_as_array,
                                          create_using=nx.DiGraph)

    #Obfuscated string is a dictionary of dictionaries of this graph:
    return nx.to_dict_of_dicts(string_as_graph, edge_data=1)

def deobfuscator(dict_of_dicts):
    #====Work backwards====
    #Build graph from dict_of_dicts:
    graph_from_dict = nx.DiGraph(dict_of_dicts)

    #Get adjacency matrix of graph
    graph_array = nx.to_numpy_array(graph_from_dict)

    #Change 1's to 255's to save as an image
    graph_array[graph_array == 1] = 255
    image_from_array = Image.fromarray(graph_array).convert("L")
    #We can send the array directly to OCR, but I like to see the image it has.
    image_from_array.save("obfuscated.png")

    #OCR our image into a string
    return pytesseract.image_to_string("obfuscated.png")

if __name__ == "__main__":
    our_string = input("Enter string to obfuscate: ")
    obfuscated_string = obfuscator(our_string)
    deobfuscated_string = deobfuscator(obfuscated_string)
    print(deobfuscated_string)
