#!/usr/bin/env python

count = 0
truecount = 0

d = { # add digits for numbers shown as words, while keeping the numbers present so we can deal eith overlapping situations eg eightwo should resolve as an 8 followed by a 2
    'zero'    : 'zero0zero',
    'one'     : 'one1one',
    'two'     : 'two2two',
    'three'   : 'three3three',
    'four'    : 'four4four',
    'five'    : 'five5five',
    'six'     : 'six6six',
    'seven'   : 'seven7seven',
    'eight'   : 'eight8eight',
    'nine'    : 'nine9nine',
} 



with open("input/01") as f:
    for line in f:
        parse = [int(i) for i in str(line) if i.isdigit()]
        count += parse[0] * 10 + parse[-1]

        trueline=str(line)
        for k,v in d.items():
            trueline = trueline.replace(k,v)
        trueparse = [int(i) for i in trueline if i.isdigit()]
        trueval = trueparse[0] * 10 + trueparse[-1] 
        truecount += trueval
        print(line,trueline,trueparse,trueval,'\n')

print(count)    

print(truecount)    
