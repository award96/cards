# cards
Class to simulate cards and dealing, functions to simulate card games

During a 3 person game of Presidents, one of my friends lamented taht with 3 players the chance that a single hand has 4 of a kind is too high. In Presidents, if you play a 4 of a kind, the winning card is now the lowest as opposed to the highest card. Flipping the rules of the game like that should be a rare incidence, and he believed that with 3 players it was just too likely that someone would get a 4 of a kind.

To test the probability of a 4 of a kind appearing, I created these two files...

The final output is any4.png, a graph where the x axis is the number of players and the y axis is the probability that any of those players is dealt a 4 of a kind.

##cards.py
 
###Card class
store and retrieve a card.
     
###Hand class
Create an ordered deck, retrieve cards from it randomly.
    
    
##prob_all4.py

###run_hand()
Simulate a single hand. Returns a list of all 4 of a kinds in that hand. Does not differentiate between who gets the 4 of a kind
    
###runSimul()
calls run_hand() a specified number of times. returns a list of all the times a 4 of a kind appeared. Each item in the array is a list of which card(s) it was that appeared (ie 1 = Ace, 13 = King).
    
###processSimul()
calls runSimul once and prints out statements about what happened. Useful to understand what exactly is happening, but not called in the prob_all4.py file
   
###largeSimul()
calls runSimul() n times, for each element of a list. The list corresponds to the number of players in the simulated game.
####returns
x: the list of simulations where each indice is the number of players tested
yDat: a list of len(x) in which each index is a list of len(number of tests) that shows the results of each test
yAve: a list of len(x) in which each index is the average number of 4 of a kinds divided by the number of tests

###plotResults():
plots the results of n simulations for each number of players (x vs yAve). the x axis is the number of players, the y axis is the probabilty anyone gets a four of a kind in a given hand.
    
  
     
   
