from room import Room
from character import Enemy

kitchen = Room('Kitchen')
kitchen.set_description('a place to cook food')

dining_hall = Room('Dining Hall')
dining_hall.set_description('a place where people eat')

ball_room = Room('Ballroom')
ball_room.set_description('a place where people dance')

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ball_room, 'west')
ball_room.link_room(dining_hall, 'east')

dave = Enemy("dave", "a smelly zombie")
dave.set_conversation('ill eat your brains!')
dave.set_weakness('cheese')
dining_hall.set_character(dave)

current_room = kitchen

dead = False
while dead == False:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")

    if command in ['north', 'east', 'south', 'west']:
        current_room = current_room.move(command)
    elif command == 'talk':
        inhabitant.talk()
    elif command == 'fight':
        print('what combat item will you use?')
        combat_item = input("> ")
        if inhabitant.fight(combat_item) == True:
            continue
        else:
            dead = True
