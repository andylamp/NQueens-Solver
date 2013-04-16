'''
Created on Apr 12, 2013

@author: agrammenos
'''

from __future__ import print_function
from random import randint

class chessBoard(object):

    global qCols
    global totalCols
    global verbose

    def __init__(self,nsize, verbose):
        '''
        Constructor
        '''
        
        global bsize
        global board
        
        #print('Peos ' + str(nsize))
        
        board = []
        bsize = int(nsize)
        self.verbose = verbose
            
    '''
        This creates the required board to sit our queens into.
        The board is creating by using the supplied N during program
        initiation.
    '''
    def createBoard(self):
         
        #print('creating board with N: ' + str(bsize))
        
        
        '''
            Create random Positions
        '''
        colIndex = range(0, bsize)
        i = 0
        self.qCols = []
        #print('Randomizing Queen Column Position...')
        while i < bsize and len(colIndex) > 0:
            #print(i)
            index = randint(0, len(colIndex)-1);
            #print(index)
            self.qCols.append(colIndex[index])
            colIndex.pop(index)
            #i = i + 1
        
        #print('Queen columns: ')
        #print(self.qCols)
            
        
        '''
            Initialize the board
        '''
        for i in range(bsize*bsize):
            # append values
            board.append(' _ ')
            
        '''
            Now put the queens in the board, please note
            that they are not in the same column. This is
            ensured by the randomization above.
        '''
        for i in range(bsize):
            board[i*bsize+self.qCols[i]] = ' Q '
        
        
    '''
        This function updates the board Queen locations (should they change)
    '''
    def updateBoard(self):
        
        for i in range(bsize*bsize):
            board[i] = ' _ '
        
        for i in range(bsize):
            board[i*bsize+self.qCols[i]] = ' Q '
            
    '''
        This function prints the supplied chess board based
        while aligning the columns and rows based on our N
        size parameter
    '''    
    def printBoard(self):
        
        spacer = int(bsize)
        
        #print(qCols)
        '''
            This does the required magic in order to print it
        '''
        for i in range(spacer):
            print('')
            for j in range(spacer):
                print(board[i*spacer+j], end='')
                #print('x', end='')
        
        print('\n')
    
    '''
        This function checks the chess board for any collisions
        that are present.
    '''    
    
    def evalThreat(self):
        
        
        rRange = bsize-1
        self.totalCols = 0
        
        for i in range(rRange):
            for j in range(i+1, bsize):
                if(abs(i-j) == abs(self.qCols[i] - self.qCols[j])):
                    #print('collision detected')
                    self.totalCols = self.totalCols + 1
                    
        #print('Total Collisions found: ' + str(self.totalCols) + '\n')
     
    '''
        This function creates a chess board, distributes the queens
        in it as well as prints it only if the user enables the 
        specific flag that does that
    '''   
        
    def createAndEvalBoard(self, silent):
        
        self.createBoard()
        #if(silent is False):
        #    self.printBoard()
        self.evalThreat()
        
        