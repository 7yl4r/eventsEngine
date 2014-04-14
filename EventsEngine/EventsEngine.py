'''
This class defines the object which holds all game information. 
Think of it like a giant game container in which everything goes.
'''

from event.Event import Event
from event.Action import Action
from event.Trigger import Trigger

class EventsEngine(object):
    def __init__(self, eventList=None):
        if eventList!=None:
            self.events = eventList           
        else:
            self.events = list()
        
    def checkEvents(self):
        '''
        Checks all events in the event list to see 
        if they have been triggered. If so, performs event action
        and removes event from the list.
        
        Returns true if any event was fired, else false.
        '''
        somethingHappened=False
        for event in self.events:
            if event.check():
                self.events.remove(event)
                somethingHappened=True
        return somethingHappened
        
    def addEvent(self,e):
        # adds given event
        self.events.append(e)
        
    def set(self,game):
        '''sets all attributes in this EventManager equal to those of a given manager'''
        self.events = game.events
        
