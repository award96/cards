from Cards import hand
import numpy as np 
import matplotlib.pyplot as plt
print('\n\n#################Start of prob_all4.py#################')

def runHand(numCards,numPlayers):

    x = hand(numCards,numPlayers)
    hands = x.dealHand()    
    counter = []

    for player in hands:
        temp = np.zeros(13)
        for card in player:
            i = card.getCardNum()
            temp[i-1] += 1

        for r in range(len(temp)):
            if temp[r] == 4:
                counter.append(r+1)
    
    return counter


def runSimul(numCards,numPlayers,numHands):
    results = []
    num4s = 0
    for i in range(numHands):
        result = runHand(numCards,numPlayers)
        if len(result) > 0:
            results.append(result)
            num4s += len(result)
    return results,num4s


def processSimul(numCards,numPlayers,numHands):
    results, num4s = runSimul(numCards,numPlayers,numHands)
    print("\nHere are the results of the simulation")
    print("\nThe number of hands in which a player had 4 of one card is ",len(results))
    print("\nThe total number of players who had 4 of one card is ",num4s)
    print("\nCalculated difference is ",num4s - len(results))

    multi = np.zeros(numPlayers)
    for result in results:
        if len(result) > 1:
            multi[len(result) - 1] += 1
        else:
            multi[0] += 1
    print("\nThe number of 4s in a hand was ",multi)

    return None


def largeSimul(numPlayers,numHands,numTests):
    xdat = []
    ydat = []
    yave = []
    for players in numPlayers:
        xdat.append(players)
        ytemp = []
        for i in range(numTests):
            results, num4s = runSimul(52//players,players,numHands)
            ytemp.append(len(results)/numHands)
        ydat.append(ytemp)
        yave.append(np.average(ytemp))

    return xdat,ydat,yave


def plot_results(xdat,ydat,yave):
    figw = 14
    figh = 8
    fig = plt.figure(1,[figw,figh])
    ax = fig.gca()
    ax.grid(True)
    fig.suptitle("Probability of Four Cards in Any Players Hand", fontsize = 30)
    ax.set_xlabel("Number of Players", size = 15)
    ax.set_ylabel("Probability", size = 15)
    ax.set_xlim(0,10)
    ax.set_ylim(0,1)
    ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
    ax.scatter(xdat,yave,color = 'k')

    for x,y in zip(xdat,yave):
        label = "{:.2f}".format(y)
        ax.annotate(label,(x,y),textcoords = 'offset points',xytext = (0,10),ha = 'center')


    ax.spines['left'].set_position('zero')


    plt.show()












numPlayers = [2,3,4,5,6,7,8,9]
numHands = 10
numTests = 100
data = largeSimul(numPlayers,numHands,numTests)
plot_results(data[0],data[1],data[2])