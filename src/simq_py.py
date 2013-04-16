'''
Created on Apr 11, 2013

@author: agrammenos

'''

from __future__ import print_function
from simulatedAnnealing import simulatedAnnealing
from collections import namedtuple

'''
    This is the benchmarking function for the SA program
'''
def benchSA(verbose, nsize):
    
    '''
        Benchmarking variables
        Nmax = 100 Queens
        nincr = 5 Queens increment per round
    '''
    nmax = 45
    nqincr = 5
    iterations = 30
    alpha = 0.999 # very low decrease in temperature
    maxIter = 100000
    initTemp = 100000
    
    '''
        Simulation Result Structure
    '''
    simResStruct = namedtuple('simResStruct', "Queens ArchivedSolution averageIterations executionTime")    
    
    print('Benchmarking Simulated Annealing N-Queens')
    
    results = []
    sa = simulatedAnnealing(False)
    
    '''
        Run the benchmarking for loop
    '''
    #(x,y) = sa.simulatedAnnealing(steps, alpha, maxIter, initTemp)
    #s = sa.simulatedAnnealing(10, alpha, 10, initTemp)
    
    for steps in range(nqincr, nmax, nqincr):

        totalT = 0
        averageIterations = 0
        foundSolution = 0
        for i in range(iterations):
            s = sa.simulatedAnnealing(steps, alpha, maxIter, initTemp)
            
            averageIterations += s[0]
            foundSolution += s[1]
            totalT += s[2]
            
            print(s)
        # add it
        foundSolution = foundSolution / iterations
        averageIterations = averageIterations / iterations
        totalT = totalT / iterations
        results.append(simResStruct(steps, foundSolution, averageIterations, totalT))
        print(results)
    
            
            
'''
    This is the Simulated Annealing Solver Wrapper, it's main purpose
    is to instantiate the SA object and pass it the required arguments
'''   
def SASolver(nsize, iterations, verbose):
    
    sa = simulatedAnnealing(True)
    sa.simulatedAnnealing(nsize, 0.999, iterations, iterations*10)
    

'''
    Our main function
'''

def main(nsize, iterations, verbose, quiet, bench):
    
    '''
        Based on input we either benchmark the software or
        perform the n-queens problem for an arbitrary size
        specified
    '''
    if(bench):
        benchSA(1, 1)
    elif (nsize > 0 and iterations > 0):
        print('Arbitrary N-Queen Problem  with SA, passing to Solver')
        
        print('Nsize is' + str(nsize) + '\n' + 'iterations: ' + str(iterations))
        SASolver(nsize, iterations, verbose)
        

    

if __name__ == '__main__':
    
    ''' 
        library that's used for easy command line
        parameters parsing
    ''' 
    import argparse
    
    
    parser = argparse.ArgumentParser(description='Search for queens')
    parser.add_argument('--quiet', nargs='*', help='be verbose about execution')
    parser.add_argument('--verbose', nargs='*', help='quiet execution')
    parser.add_argument('-n','--nsize', help='size of the Chess Table [REQUIRED]', type=int)
    parser.add_argument('-i','--niter', help='amount of iterations [REQUIRED]', type=int)
    parser.add_argument('--bench', action='store_true', help='Benchmark the software up to n=20 for 30 iterations each with a step of 5 Queens each round')
    
    arguments = parser.parse_args()
    
    if(arguments.bench):
        main(0,0,0,0,arguments.bench)
    elif(arguments.nsize > 0 and arguments.niter > 0 and (arguments.verbose or arguments.quiet)):
        if(arguments.verbose): 
            main(arguments.nsize, arguments.niter,arguments.verbose, 0, 0)
        elif(arguments.quiet):
            main(arguments.nsize, arguments.niter, 0, arguments.quiet,0)
            
    elif(arguments.nsize > 0 and arguments.niter > 0):
        main(arguments.nsize, arguments.niter, 0, 0, 0)
            
    ''' 
        Do nothing!
    '''
        
        
        
        
        
        
    