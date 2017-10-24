class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def get_name(self):
        return self.name

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(room.get_name() + "\n" + "--------------" + "\n" + direction
                  + "\n")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You cant go that way")
            return self
