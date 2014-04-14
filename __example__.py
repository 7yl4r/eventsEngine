''' 
a hacky way to get events working while we try to think of something
more clever.
'''

from EventsEngine.EventsEngine import EventsEngine, Event, Trigger, Action

SEP = '===================================================' # horizontal bar
YES = ['y','Y','yes','Yes','YES','affirmative'] # strings that mean yes

def main():
    print SEP\
      +"\n\t Welcome to EventManager's mock game! \
        \n\t This is just a demo... \
        \n\t         ...sorry it's not very fun. =)\
        \n"+SEP
     
    game = gameInstance()
    keep_playing = True
    
    while(keep_playing):
        game.update()
        
        ans = raw_input("do you want to quit? ")
        if ans in YES:
            keep_playing=False
            
    print 'goodbye!'

class gameInstance(object):
    def __init__(self):
        self.game_time = 0
        
        # add initial list of events to my game
        self.event_manager = EventsEngine(getEventList(self))
        
        # ...oh wait... add one more event... 
        self.event_manager.addEvent(Event(Trigger('o.game_time > 10', self),Action('print "\tFIN."')))

        
    def update(self):
        self.event_manager.checkEvents()
        print 'game time = ',self.game_time
        self.game_time+=1
        

def getEventList(game):
    ''' return list of all starting events for my game '''
    return [
        Event(Trigger('True'),
            Action('''print "\tBAM! That's an event... next one is at t=3"''')),
            
        Event(Trigger('o.game_time > 3',game),
            Action('print "\tWhat a boring morning..."')),
            
        Event(Trigger('o.game_time > 6',game),
            Action('''print "\tDon't you wish you could break out of the the daily grind?"'''))
        ]
        
if __name__ == '__main__':
    main()