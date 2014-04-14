eventsEngine
============

Event engine package for python games. 

Create action/trigger (cause/effect) pairs, linked events (quests, stories) easily. Just drop this into your game-in-progress.

### Usage ###
1. initialize EventsEngine
2. add your events using built-in constructors
3. call EventsEngine.checkEvents in your game update() method. 

Want more details? Check out [__example__.py](https://github.com/7yl4r/eventsEngine/blob/master/__example__.py).

### Concepts ###
* Action  = any arbitrary code
* Trigger = a conditional that causes an action
* Event = a trigger->action pair
* Story = a linear series of Events that happen chronologically
* Node = an event with multiple triggers which lead to different actions
* Tree = a Story made up of Nodes
