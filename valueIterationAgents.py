# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        
        iterationsCount = 0
        
        while iterationsCount < iterations:
            
            allStates = mdp.getStates()
            #Updating shouldn't happen before we have completely finished an iteration, has side effects. 
            V= self.values.copy()
            for state in allStates:
                #determine which action has the highest value
                actionToTake = self.computeActionFromValues(state)
                #update our V map with the best value we get
                V[state] = self.computeVOfAction(state, actionToTake)
                
            self.values = V
            iterationsCount = iterationsCount + 1


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        
        return 0
        
#         tAndRValues = self.mdp.getTransitionStatesAndProbs(state, action)
#         
#         for tAndR in tAndRValues:
#             
#         
#         sumOfWeightRewards = 0
#         
#         return sumOfWeightRewards
#         nextState = tAndRValues.getState
#             nextStateReward = self.mdp.getReward(nextState)
#             sumOfWeightRewards = sumOfWeightRewards + (tAndRValues.getProb * nextStateReward) + self.discount * self.getValue(nextState)
        
#         util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
#Seems to just call for MAX amongst available actions from state
        
        if(state == 'TERMINAL_STATE'):
            return None

        bestAction = ''
        bestActionValue = -float("inf")
                
        availableActions = self.mdp.getPossibleActions(state)
        
        for action in availableActions:

            actionValue = self.computeVOfAction(state,action)           

            if (actionValue >= bestActionValue):
                bestActionValue = actionValue
                bestAction = action 
        
        return bestAction 
        
#         util.raiseNotDefined()

    def computeVOfAction (self, state, action ):
        
        if(state=='TERMINAL_STATE'):
            return 0
        
        transitionStateAndProbs = self.mdp.getTransitionStatesAndProbs(state, action)
            
        actionValueStar = 0

        for tStateAndProb in transitionStateAndProbs:
            nextState, nextStateProbability = tStateAndProb
                
            nextStateDiscountedValue = self.discount * self.values[nextState]
            nextStateReward = self.mdp.getReward(state, action, nextState)
             
            actionValueStar = actionValueStar + nextStateProbability * (nextStateReward +  nextStateDiscountedValue)
            
        return actionValueStar    
        
    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
