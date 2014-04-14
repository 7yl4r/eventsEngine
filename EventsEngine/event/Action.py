''' 
Action class for events. 
'''

#from lib.colorama import Fore

### EXAMPLE ACTIONS ###
#(depreciated)#
### ========================== ###
#def printout(text,remove=True):
#    print(Fore.MAGENTA+text)
### ========================== ###
    

class Action(object):
    
    def __init__(self,evalStr,o=None):
        '''
        evalStr will be run when Action() is called
        o is an object which can be referenced in the evalStr
        '''
        self.whatToDo = evalStr
        self.obj = o
        
    def __call__(self):
        o = self.obj
        exec(self.whatToDo)
      
