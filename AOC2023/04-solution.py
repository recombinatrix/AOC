points = 0
cards = {}

with open("input/04") as f:
    for line in f:
        c = int(line.split(':')[0].split()[1]) # get card number
        cards[c] = cards.get(c,0) + 1 # add a copy of the card we won, initialising the dictionary entry if this is the first time
        copies = cards[c] # how many copies of this card do we have
        k = set([int(x) for x in line.split('|')[0].split(":")[1].strip().split()])     # get winning numbers   
        n = set([int(x) for x in line.split('|')[1].strip().split()])                   # get numbers you have 
        v = len(n.intersection(k)) # how many matches are there?
        
        if v > 0: # are there any matches? 

            # for part one
            points += int(2 ** (v-1)) # value is 2 to the power of (number of matches - 1)

            # for part two
            for i in range(v): # for each win
                for j in range(copies): # how many copies of this card do we have?
                     cards[c+ i + 1] = cards.get(c+ i + 1,0) + 1 # add a copy of the card we won, initialising the dictionary entry if this is the first time

print(points)
print(sum(cards.values()))