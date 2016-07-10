''' 
Trigger class for events. 

Triggers are evaluated in order to determine if it is appropriate to activate the action of an event.
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
        try:
            return eval(self.criteria)
        except AttributeError as E: # (problems with o in criteria)
            print '\n\nERR: trigger cannot resolve your reference. Did you pass the right o object?'\
                 +'\n\tyour evalStr syntax:'\
                 +'\n\t'+self.criteria\
                 +'\n\to = '+str(o)\
                 +'\n\n'
            raise E
