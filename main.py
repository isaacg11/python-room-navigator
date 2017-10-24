from room import Room

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

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)