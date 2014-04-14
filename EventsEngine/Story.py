'''
A story is a series of connected events which occur in sequential order. 
The Story class defined here is much like the event class but instead is an event-list
which is iterated through as each subsequent event is completed.

Returns False if story not over, returns True is story is complete and can be deallocated.
'''

from Event import Event

class Story(object):
    def __init__(self,eventList):
        '''
        eventList = sequence of Event objects which take place sequentially from eventList[0] to eventList[n]
        '''
        self.current_event = None

        self.eventList = eventList[::-1] # reverse the list so we can pop off the end (which is now the first item)
        self._next_event()
            
        
    def getEventName(self):
        return self.current_event.get_event_name()
        
    def check(self):
        ''' checks the event for trigger condition satisfied '''
        if self.current_event.trigger():
            self.current_event.action()
            return self._next_event()
        # else do nothing
        return False
        
    ### PRIVATE METHODS ###    
        
    def _next_event(self):
        '''
        moves to the next Event in the list.
        returns true if story is over
        '''
        try:
            self.current_event   = self.eventList.pop()        
        except IndexError: # catch attempt to pop empty list
            return True # Story is over
        # if no error (still some story remaining)
            return False