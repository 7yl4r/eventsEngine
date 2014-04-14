''' 
Simple text-based "game" to demonstrate use of EventsEngine. 
'''

from EventsEngine.EventsEngine import EventsEngine, Event, Trigger, Action, Story
from random import choice
from sys import maxint

# some globals for my convenience:
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
        self.event_manager = EventsEngine([
            Event(Trigger('True'),
                Action('''print "\tBAM! That's an event... next one is at t=3"''')),
                
            Event(Trigger('o.game_time > 3',self),
                Action('print "\tSee? Told you."'))
            ])
        
        # ...oh wait... add one more event... 
        self.event_manager.addEvent(Event(Trigger('o.game_time > 15', self),Action('print "\tFIN."')))
        
        # add one of my stories to our event list:
        myStory = getRandomStory(self,maxTime=15,minTime=4)
        self.event_manager.addEvent(myStory)
        
    def update(self):
        self.event_manager.checkEvents()
        print 'game time = ',self.game_time
        self.game_time+=1

def getRandomStory(game,minTime=0,maxTime=maxint):
    ''' returns a random story occurring between minTime & maxTime '''
    StoryTexts = [
        ["Yesterday's blob of cells made mistakes.",
         "Today's blob sleeps uneasily. ",
         "Perhaps tomorrow's blob will be better arranged."
        ],
        ["Two possibilities exist: ",
         "Either we are alone in the Universe..."
         "...or we are not.",
         "Both are equally terrifying."
         " ~ Arthur C. Clark"
        ],
        ["What a boring morning...",
        "Don't you wish you could break out of the daily grind?"
        ]
    ]
    story = choice(StoryTexts)
    storytime = choice(range(minTime,maxTime-len(story)))
    event_list = list()
    for line in story:
        event_list.append(Event(Trigger('o.game_time > '+str(storytime),game),
                                Action('print "\t'+line+'"' )))
        storytime+=1
    return Story(event_list)
        
if __name__ == '__main__':
    main()