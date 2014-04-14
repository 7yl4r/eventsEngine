''' 
Trigger class for events. 
'''
from datetime import datetime

### ========================== ###
### TRIGGER TEMPLATE FUNCTIONS ###
#         (depreciated)         #
### ========================== ###
# def alwaysTrue():
    # return True

##player stats :
# def valueAbove(value, thresh):
    # return value > thresh
    
# def valueIs(value, criteria):
    # try:
        # return value == loc
    # except AttributeError:
        # return False
    
##game stats :
# def commandCountAbove(game,number):
    # return game.commands_entered > number

# def timeElapsedSinceGameStart(game,timeDelta):
    # return (datetime.now() - game.GAME_START) > timeDelta
### ========================== ###

class Trigger(object):
    
    def __init__(self, evalStr, o=None):
        '''
        evalStr should return boolean.
        o is an object which can be referenced in the evalStr
        '''
        self.criteria = evalStr
        self.obj = o
    def __call__(self):
        o = self.obj
        return eval(self.criteria)
      
