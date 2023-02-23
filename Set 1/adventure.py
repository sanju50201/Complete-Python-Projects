class Room:
    def __init__(self, name, description, choices):
        self.name = name
        self.description = description
        self.choices = choices

    def get_choices(self):
        return self.choices


class Game:
    def __init__(self, rooms):
        self.rooms = rooms
        self.current_room = self.rooms[0]

    def play(self):
        while True:
            print(self.current_room.name)
            print(self.current_room.description)

            choices = self.current_room.get_choices()

            for i, choice in enumerate(choices):
                print(f"{i+1}. {choice[0]}")
            choice = int(input("Enter your choice: ")) - 1

            if choice < 0 or choice >= len(choices):
                print("Invalid choice, please try again")
                continue
            elif choice == -1:
                break
            self.current_room = self.rooms[choices[choice][1]]


# define the rooms in the game
room_1 = Room("Room 1", "This is room 1.", [
              ("Go to room 2", 1), ("Go to room 3", 2)])
room_2 = Room("Room 2", "This is Room 2.", [("Go to room 1", 0)])
room_3 = Room("Room 3", "This is Room 3.", [("Go to room 1", 0), ("Quit", -1)])

# start the game

game = Game([room_1, room_2, room_3])
game.play()
