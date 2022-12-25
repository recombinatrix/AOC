#!/usr/bin/env python 


with open("input/01") as f:
    # f.read().rstrip("\n") : read in the file as a single list, removing the the trailing "/n" because it breaks the later list comprehensions
    # thing.split("\n\n") : split by blank lines 
    # [list(map(int,x.split("\n"))) for x in thing ]     : use list comprehension to split the sub-elements of the big list by newlines
    # then use map the sublists to a list of ints, and then convert those mappings back to a list
    # [ sum(x) for x in thing ] : second list comprehension to get the sum of each sublist
    # sorted(thing) : sort the list comprehension string; list.sort() will modify the list in place and would require it's own line
    
    l = sorted([ sum(x) for x in [list(map(int,x.split("\n"))) for x in f.read().rstrip("\n").split("\n\n") ] ],reverse=True)
    
print(max(l)) # part one
print(sum(l[:3])) # part two

# this seems like an adequate solution but I'd like to see what people are doing with numpy and pandas, rather than just processing the data as raw text
# processing as raw text is fine for this solution, but figuring out how to chunk pandas by vell values could be useful for my actual work 