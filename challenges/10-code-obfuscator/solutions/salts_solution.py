#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:27:08 2019
@author: salt

This obfuscation isn't too esoteric, but it's fun nonetheless:
    We convert our string into an image with imagemagick.
    We convert the image into a numpy array.
    We use the numpy array as an adjacency matrix to make a graph.
    The edge list for our graph is our obfuscated string.

The obfuscated string can be quite long. For instance, the input "testing"
gives len(obfuscated_string) == 9526. A piece of it looks like:

>>>obfuscated_string[1000:1020]

[(11, 58), (11, 59), (11, 60), (11, 61), (11, 62), (11, 65), (11, 66),
 (11, 67), (11, 68), (11, 69), (11, 70), (11, 71), (11, 72), (11, 73),
 (11, 76), (11, 77), (11, 78), (11, 79), (11, 82), (11, 83)]

We can work backwards to get our original string :
    Make a graph with our edge list.
    Save graph's adjacency matrix as numpy array.
    Convert numpy array into an image.
    Use OCR to read the image as a string.

There's a catch, of course.  OCR isn't perfect: You may end up with missing or
wrong characters.  I also doubt this qualifies as "keeping functionality
intact", but I enjoyed it.
"""
import networkx as nx
import pytesseract
import subprocess
from PIL import Image
import numpy as np

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
    string_as_array[string_as_array > 0] = 1  #We just need an array of 1's and 0's

    #Turn our array into a graph by treating it as an adjacency matrix
    string_as_graph = nx.from_numpy_array(string_as_array,
                                          create_using=nx.DiGraph)

    #Obfuscated string is just a list of the edges in this graph:
    return list(string_as_graph.edges())

def deobfuscator(list_of_tuples):
    #====Work backwards====
    #Build graph from edge list:
    graph_from_edges = nx.DiGraph()
    #Add nodes in order or the image will be scrambled
    graph_from_edges.add_nodes_from(range(graph_order_and_image_dim))
    graph_from_edges.add_edges_from(list_of_tuples)

    #Get adjacency matrix of graph
    graph_array = nx.to_numpy_array(graph_from_edges)

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
