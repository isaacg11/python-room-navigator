from room import Room
from character import Enemy
from item import Item
backpack = []

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

cheese = Item('cheese')
dave = Enemy("dave", "a smelly zombie")
dave.set_conversation('ill eat your brains!')
dave.set_weakness('cheese')
dining_hall.set_character(dave)
dining_hall.set_item(cheese)
cheese.set_description('a big smelly block of cheese')
current_room = kitchen

dead = False
while dead == False:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ['north', 'east', 'south', 'west']:
        current_room = current_room.move(command)
    elif command == 'talk':
        inhabitant.talk()
    elif command == 'fight':
        print('what combat item will you use?')
        combat_item = input("> ")
        if combat_item in backpack:
            if inhabitant.fight(combat_item) == True:
                current_room.character = None
            else:
                dead = True
        else:
            print('you do not have that combat item, please choose another')

    elif command == 'take':
        backpack.append(current_room.get_item().name)
        current_room.item = None