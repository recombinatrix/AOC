#!/usr/bin/env python 

import pandas as pd
import numpy as np

raw = pd.read_csv("input/04",sep=',|-',names=["min1","max1","min2","max2"],engine="python")

# check if one is completely contained within the other
raw["p1"] = raw.apply(lambda x : ( (x["min1"] >= x["min2"]) and (x["max1"] <= x["max2"]) ) or ((x["min1"] <= x["min2"]) and (x["max1"] >= x["max2"]))    ,axis=1)
print(raw["p1"].sum())

# if they overlap in anay way, one elf's minima will fall within the other elf's range

raw["p2"] = raw.apply(lambda x : ( (x["min1"] in (range( x["min2"],x["max2"]+1))) or (x["min2"] in (range( x["min1"],x["max1"]+1))) ) ,axis=1)
print(raw["p2"].sum())

