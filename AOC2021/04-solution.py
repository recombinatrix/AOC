import numpy as np

calls =  np.loadtxt("input/04", max_rows=1, delimiter=",").astype(complex)
cards = np.loadtxt("input/04", skiprows=2).reshape((100,5,5)).astype(complex)

# plan is that when a number is called:
# scan through every element of the cards looking for matches to the call
# if you find one, do the following:
#   1) replace all instances of that number with 0 + i
#   2) check if the numbers row or column adds up to 0 + 5i
#   3) if yes, stop searching, return the current card number, and calculate the score of the card 
#   4) the score will be the real component of the sum of the card entries multiplied by the current call.
# when the first card wins, set won to true and return that cards score
# when any card wins, calculate it's score then blank that card so it can't win again
# after finishing all calls, return the score of the final winning card

won = False
ok = True
score = 0

for call in calls:
    for card in cards:
        x = 0
        while x < 5:
            y = 0
            while y < 5:
                if card[x,y] == call:
                    card[x,y] = (0 + 1j)
                    if sum(card[x,:]) == (0 + 5j):
                        score = (int((np.sum(card) * call).real))
                        if not won: 
                            print("part1: " + str(score))
                            won = True
                        card[:,:] = (-1.+0j) # when any card wins, blank that card
                    elif sum(card[:,y]) == (0 + 5j):
                        score = (int((np.sum(card) * call).real))
                        if not won: 
                            print("part1: " + str(score))
                            won = True
                        card[:,:] = (-1.+0j) # when any card wins, blank that card

                y += 1
            x += 1

print("part2: " + str(score))