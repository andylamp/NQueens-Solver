'''
Created on Apr 12, 2013

@author: agrammenos
'''
from random import randint, random
from chessBoard import chessBoard
from copy import deepcopy
import math
from collections import namedtuple
import time

class simulatedAnnealing(object):

    global size
    global alpha
    global maxIterations
    global t0
    
    global tryBoard
    global mainboard
    
    global verbose

    def __init__(self, verbose):
        '''
        Constructor
        '''    
        self.verbose = verbose
    
    
    '''
        This basically exchanges the available columns
        by just using a random position
    '''
    def heuristicExchange(self):
        
        '''
            Get the random positions for exchange
        '''
        pos1 = randint(0,self.size-1)
        pos2 = randint(0,self.size-1)
        
        '''
            Deep-Copy the objects
        '''
        tryBoard = deepcopy(self.mainboard)
        
        '''
            Now exchange the columns
        '''
        
        tryBoard.qCols[pos1] = self.mainboard.qCols[pos2];
        tryBoard.qCols[pos2] = self.mainboard.qCols[pos1];
        tryBoard.updateBoard()
        
        tryBoard.evalThreat()
        
        #print(self.mainboard.qCols)
        #print(tryBoard.qCols)
        
        return tryBoard
        
        
        
        
        
    '''
        This functions creates the main board for us (in silent mode)
    '''
    def createSolutionBoard(self):
        self.mainboard = chessBoard(self.size, True)
        self.mainboard.createAndEvalBoard(False) 
    
    
    '''
        This function is responsible for finding a solution
    '''
    def searchSolution(self):
        self.createSolutionBoard()
        
        iterations = 0
        T = self.t0
        
        while (iterations < self.maxIterations and self.mainboard.totalCols != 0):
            
            self.tryBoard = self.heuristicExchange()
            
            '''
                Check if we found a better solution
            '''
            if(self.tryBoard.totalCols < self.mainboard.totalCols):
                '''
                    copy tryBoard to mainboard
                '''
                self.mainboard = self.tryBoard
            
            else:
                '''
                    This is Simulated Annealing property, based on a random value r
                    and the exponential difference of total differences of each of the
                    two boards divided by the current temperature gives us the probability
                    of exchanging the 'false' solution with the 'good'
                '''
                r = random()
                
                try:
                    
                    
                    p = float((self.mainboard.totalCols - self.tryBoard.totalCols ) / T)
                    power =  math.pow(math.e, p)
                    #print(self.tryBoard.totalCols, self.mainboard.totalCols)
                    #print(p, power)
                    #print(r)
                    #print(power)
                    if(r < power):
                        self.mainboard = deepcopy(self.tryBoard)
                except OverflowError:
                    print()
                    #print('Overflow occurred, cannot decrease temperature any more')
            
            iterations += 1
            T *= self.alpha
            

        if(self.verbose is True):
            print('\nSA Stats:\n\tIterations: ' + str(iterations) + " out of: " + str(self.maxIterations) + "\n\tCurrent Temperature: " + str(T))
            print('\n\tTotal Collisions (so far): ' + str(self.mainboard.totalCols) + '\n\t' + str(('We did not find a solution','We found a solution')[self.mainboard.totalCols == 0]))
        
        return (iterations, (0,1)[self.mainboard.totalCols == 0])
        
    '''
        This is a N-Queen solver function that uses the Simulated Annealing 
        probabilistic algorithm in order to find a solution to the problem.
    '''
    def simulatedAnnealing(self, bsize, alpha, maxIter, t0):

        '''
            Parameter Initialization
        '''
        
        self.size = bsize
        self.alpha = alpha
        self.maxIterations = maxIter
        self.t0 = t0
        
        '''
            Print our parameters
        '''
        
        if(self.verbose is True):
            print('\nStarting SA with parameters: ')
            print('\tsize: ' + str(bsize))
            print('\talpha: ' + str(alpha))
            print('\tmaxIterations: ' + str(maxIter))
            print('\tt0: ' + str(t0))
        
        t0 = time.time()
        (iterations, solution) = self.searchSolution()
        t1 = time.time()
        totalT = t1-t0
        
        '''
            Print solution
        '''
        if(self.verbose is True):
            self.mainboard.printBoard()
        
        return (iterations, solution, totalT)
        
                
        