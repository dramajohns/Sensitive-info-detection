# -*- coding: utf-8 -*-
# simple function for reading txt files
def readtext(filepath) :
    with open(filepath) as f:
      text = f.read()
    return(text)