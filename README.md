# cards
Class to simulate cards and dealing, functions to simulate card games

During a 3 person game of Presidents, one of my friends lamented that with 3 players the chance a single hand has 4 of the\
same card is too high. The rule is that if you play 4 of a kind, the lowest card now wins the pile, as opposed to the highest\
If the incidence of 4 of a kind is too high in Presidents, the entire strategy of the game is different, and a once rare\
and exciting event becomes a common part of the game.

To test the probability of a 4 of a kind appearing, I created these two files...

cards.py
  contains card class
     store and retrieve the kind and suit of a card
     
  contains hand class
    create the ordered deck
    deal out a random card from the deck until there are fewer cards than players
    
    
prob_all4.py
  function run_hand()
    using the hand class simulates a single hand
    returns an list of all 4 of a kinds in that hand (ie [] = no 4 of a kinds, [1,13] = 4 of a kind Ace, 4 of a kind King)
    does not differentiate between who gets the 4 of a kind
    
  function runSimul()
    calls run_hand() a specified number of times.
    returns a list of len(number of hands at least one 4 of a kind appeared) where each item in the array is a list\
    of which card(s) it was that appeared (ie 1 = Ace, 13 = King).
    
  function processSimul()
    calls runSimul once and prints out statements about what happened
    useful to understand what exactly is happening, but not called in the prob_all4.py file
   
   function largeSimul()
    calls runSimul() a specified number of times for a list of the number of players to test.
    returns x: the list of the number of players tested
    returns yDat: a list of len(x) in which each index is a list of len(number of tests) that shows the results of each test
    returns yAve: a list of len(x) in which each index is the average number of 4 of a kinds divided by the number of tests
   function plotResults():
     plots the results (x vs yAve)
     the x axis is the number of players, the y axis is the probabilty anyone gets a four of a kind in a given hand.
    
  
     
   
