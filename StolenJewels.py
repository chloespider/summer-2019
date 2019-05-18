# My Stolen Jewel Mission by Chloe Inman
import random

def msg(room):
    if room['msg'] == '':
        return "You have entered the " + room['name'] + '. '
    else:
        return room['msg']

def get_choice(room,dir):
    if dir=='N':
        choice = 0
    elif dir=='E':
        choice = 1
    elif dir=='S':
        choice = 2
    elif dir=='W':
        choice = 3
    else:
        return -1
        
    if room['directions'][choice] == 0:
        return 4
    else:
        return choice
        
def main():
    dirs = (0,0,0,0)
    
    entrance = {'name':'Entrance Way','directions':dirs,'msg':''}
    livingroom = {'name':'Livingroom','directions':dirs,'msg':''}
    hallway = {'name':'Hallway','directions':dirs,'msg':''}
    kitchen = {'name':'Kitchen','directions':dirs,'msg':''}
    diningroom = {'name':'Dining Room','directions':dirs,'msg':''}
    family_room = {'name':'Family Room','directions':dirs,'msg':''}
    
    entrance['directions'] = (kitchen,livingroom,0,0)
    livingroom['directions'] = (diningroom,0,0,entrance)
    hallway['directions'] = (0,kitchen,0,family_room)
    kitchen['directions'] = (0,diningroom,entrance,hallway)
    diningroom['directions'] = (0,0,livingroom,kitchen)
    family_room['directions'] = (0,hallway,0,0)
    
    rooms = [livingroom,hallway,kitchen,diningroom,family_room]
    room_with_jewels = random.choice(rooms)
    jewels_delivered = False
    room = entrance
    
    name=raw_input('Hello. What is your name? ')
    print 'Welcome,' ,name+'. ', 'Can you find the stolen pouch of jewels?'
    
    while True:
        if jewels_delivered and room['name'] == 'Entrance Way':
            print('You have secured the stolen jewels and returned to the entrance. ' +
            'Congratulations on accomplishing the mission!')
            break;
        elif not jewels_delivered and room['name'] == room_with_jewels['name']:
            jewels_delivered = True
            print(msg(room) + 'There is the pouch of stolen jewels and our thief is taking a nap ' +
                  'right next to it! Collect the jewels. ' +
                  'Now back out quickly using the smae path you came in - but in reverse!')
            room['msg'] = ('You are back in the ' +room['name'] +
                           '! You already have the jewels. ' +
                        'Remember, you should escape through the rooms that you came!')
        else:
            print(msg(room))
            room['msg'] = 'You are back in the ' +room['name']
            
        stuck = True
        while stuck:
            dir = raw_input("Which direction do you want to go: N, E, S, or W? ")
            choice = get_choice(room,dir)
            if choice == -1:
                print("Please enter N, E, S, or W ")
            elif choice == 4:
                print('You cannot go in the direction. There is a wall there.')
            else:
                room = room['directions'][choice]
                stuck = False
main()