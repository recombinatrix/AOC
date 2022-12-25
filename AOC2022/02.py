#!/usr/bin/env python 

import numpy as np
import pandas as pd

# going to map things to dictionaries 

code = {

# opponent plays

"A" : 0, # "Rock" ,
"B" : 1, # "Paper" ,
"C" : 2, # "Scissors" ,

# my plays, score minus one so I can use it as a lookup

"X" : 0,  # "Rock"
"Y" : 1,  # "Paper" ,
"Z" : 2,  # "Scissors" ,

}

# win loss matrix:
# rows are opponent's play, columns are my plays

mx = np.array(
[[ 3 , 6 , 0 ],
 [ 0 , 3 , 6 ],
 [ 6 , 0 , 3 ]])

# what to choose matrix
# rows are opponent's play, columns are my desired outcome

choice = np.array(
[[ 2 , 0 , 1 ],
 [ 0 , 1 , 2 ],
 [ 1 , 2 , 0 ]])

# what is the score for two sets of plays

def score (p,q):
    score= [ (int(mx[x[0],x[1]]) + x[1] + 1) for x in zip(p,q) ]
    return( score)

# what is the play for a set of opponents plays and a set of desired outcomes 

def play (p,q):
    play = [ choice[x[0],x[1]] for x in zip(p,q) ]
    return(play)

# read it in

raw = pd.read_csv("input/02",delim_whitespace=True,names=["elf","me"]).replace(code)

raw["score"] = score(raw["elf"],raw["me"]) 

print(raw["score"].sum())

raw["me2"] = play(raw["elf"],raw["me"])
raw["score2"] = score(raw["elf"],raw["me2"])

print(raw["score2"].sum())