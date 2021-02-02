"""
Author: Ugur Taysi
Program Name: Uno Game
Used Terms: 
~~~~~~~
Closed Deck: The deck in the middle which players blindly draw from
Open Deck: The deck in the middle which players put the cards that they play on the top visibly. Dictates which next card will be playable or not.
"""

import random

class UnoCard:

    def __init__(self, color, num):
        self.color = color
        self.num = num

    def __str__(self):
        return self.color + ' ' + str(self.num)
    
    #Determines if the card object is playable against the other card object
    def canPlay(self, other):
        if (self.color == other.color or self.num == other.num):
            return True
        else:
            return False


class CollectionOfCards:
    
    def __init__(self):
        self.open = []
        self.closed = []
        self.colors = ['Red','Yellow','Green','Blue']
    
    #Creates closed deck with cards of 4 colors and 9 numbers. Each color has 2 of each number. Total 72 cards. Each card is an UnoCard object.
    def createClosedDeck(self):
        self.closed = []
        for i in self.colors:
            for j in range (1, 10, 1):
                a = UnoCard(i,j)
                self.closed.append(a)
                self.closed.append(a)
    
    #Creates an empty open deck
    def createOpenDeck(self):
        self.open = []
    
    #Shuffles the closed deck
    def shuffleClosedDeck(self):
        random.shuffle(self.closed)

        
class UnoGame: 
    decks = CollectionOfCards()
    
    def __init__(self,players):
        self.players = players
        self.hands = []
        self.finished = 0
        self.winner = 404
        self.turn = 0
    
    #Starts the game
    def startGame(self):
        for i in range (0, self.players, 1):
            #Each empty list in self.hands is a player's hand
            self.hands.append([])
        #Create closed and open decks and shuffle the closed deck
        self.decks.createClosedDeck()
        self.decks.createOpenDeck()
        self.decks.shuffleClosedDeck()
        #Deal each player 7 cards
        for i in range (0,self.players,1):
            self.dealSeven(i)
        #Initiate first turn and then repeat playTurn method until the game is finished
        self.playFirstTurn()
        while (self.finished == 0):
            self.playTurn()
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nGood game! PLAYER ' + str(self.winner) + ' WINS.\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

    #Deals 7 cards to a player's hand in the beginning of the game    
    def dealSeven(self,playerID):
        #Pop the last item from closed deck and append it to the hand of the player, 7 times.
        for i in range (0,7,1):
            self.hands[playerID].append(self.decks.closed.pop(-1))
    
    #Initializes first turn
    def playFirstTurn(self):
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~\nPlayer ' + str(self.turn%self.players+1) + "'s turn to play! ")
        print('Your cards are: ')
        #Print each card in the person's hand so they can choose to play
        for i in range (0,len(self.hands[self.turn%self.players]),1):
            print('['+str(i+1)+']', end=' ')
            print(self.hands[self.turn%self.players][i])
        print('Type card number to play: ', end='')
        choice = int(input())
        #Pop the choice from player's hand and add it to the open deck in the middle
        self.decks.open.append(self.hands[self.turn%self.players].pop(choice-1))
        print('The middle card is now: ', end='')
        print(self.decks.open[-1])
        self.turn += 1 

    #Main turn method. This will keep repeating itself until the game comes to a finish.
    def playTurn(self):
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nPlayer ' + str(self.turn%self.players+1) + "'s turn to play! ")
        #First check whether the hand is playable or not
        if (self.handPlayable(self.hands[self.turn%self.players]) == True):
            print('Your cards are: ')
            #Print each card in the person's hand so they can choose to play
            for i in range (0,len(self.hands[self.turn%self.players]),1):
                print('['+str(i+1)+']', end=' ')
                print(self.hands[self.turn%self.players][i])
            print('Type card number to play: ', end='')
            choice = int(input())
            #First check if the person's choice is playable or not. If not, ask to rechoose. 
            while (self.hands[self.turn%self.players][choice-1].canPlay(self.decks.open[-1]) == False):
                print("Your choice is not playable! Middle card is: ", end='')
                print(self.decks.open[-1])
                print('Type card number to play: ', end='')
                choice = int(input()) 
            #Pop the choice from player's hand and add it to the open deck in the middle
            self.decks.open.append(self.hands[self.turn%self.players].pop(choice-1))
            print('The middle card is now: ', end='')
            print(self.decks.open[-1])
        #If the hand is not playable draw a random card from the closed deck and skip the turn
        else:
            self.hands[self.turn%self.players].append(self.decks.closed.pop(-1))
            print('Your hand is not playable! Drew ', end='')
            print(self.decks.closed[-1], end='')
            print(' and skipped turn!')
            print('The middle card is now: ', end='')
            print(self.decks.open[-1])        
        #At the end of each turn check if we've come to have a winner
        if(self.checkWinner(self.hands[self.turn%self.players]) == True):
            self.finished = 1
            self.winner = self.turn%self.players+1
        self.turn += 1

    #Determines if the hand is playable with the open card in the middle
    def handPlayable(self, hand):
        playable = False
        for i in range (0,len(hand),1):
            if (hand[i].canPlay(self.decks.open[-1]) == True):
                playable = True
        return playable
    
    #Checks if a person is the winner
    def checkWinner(self,hand):
        if (len(hand) == 0):
            return True
        else:
            return False


#Ask player count then initialize game
players = int(input('How many players will play? '))
game1 = UnoGame(players)
game1.startGame()
