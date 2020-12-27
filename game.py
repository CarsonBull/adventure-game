
# These are global setup
board_size = 10
key_loc = [1,0]
exit_loc = [1,-1]
wall_locs = [[2,0],[7,1]]
directions = ["north", "south", "east", "west"]

def move(direction, distance, player_position):
    # What direction does the user want to move
    if direction == "north":
        new_cords = [player_position[0] + distance, player_position[1]]
        if isValidMove(new_cords):
            return new_cords
    elif direction == "south":
        new_cords = [player_position[0] - distance, player_position[1]]
        if isValidMove(new_cords):
            return new_cords
    elif direction == "east":
        new_cords = [player_position[0], player_position[1] + distance] 
        if isValidMove(new_cords):
            return new_cords
    elif direction == "west":
        new_cords = [player_position[0], player_position[1] - distance] 
        if isValidMove(new_cords):
            return new_cords
    
    print(f"Unable to move {direction}. It seems there is something in your way.")
    return player_position

def getPlayerMove():
    move_direction = input("Which direction would you like to move?").lower()

    while move_direction not in directions:
        # This is called an f string. It's just a formatted string
        print(f"Please enter a valid move direction. Valid input: {directions}")
        move_direction = input("Which direction would you like to move?").lower()
    
    return move_direction

def isValidMove(future_cords):
    # Make sure the user isn't trying to move into a wall
    if future_cords in wall_locs:
        return False
    # Check that the user is not off the map in the x direction
    elif future_cords[0] > board_size or future_cords[0] < -1*board_size:
        return False
    # Check that the user is not off the map in the y direction
    elif future_cords[1] > board_size or future_cords[1] < -1*board_size:
        return False
    
    # If the user doesn't match any of the agbove constraints then it is a valid move
    return True

def adventureGame():
    player_pos = [0,0]
    has_key = False
    exited = False

    while not exited:
        print(f"Your current position is {player_pos}")
        player_move_dir = getPlayerMove()

        # TODO: Implement a move distance later. For now we are just going to hardcode it to move 1
        player_pos = move(player_move_dir, 1, player_pos) 


        if player_pos == key_loc and not key_loc:
            print("You found the key. Make your way to the exit.")
            has_key = True
        elif player_pos == exit_loc and has_key:
            print("You successfully found the key and made your way to the exit! Congrats")
            # When the player reaches the exit we want to allow them to leave
            exited = True
        elif player_pos == exit_loc:
            print(f"You found the exit at {exit_loc} but you don't have the key. Find the key then return young traveler")


if __name__ == "__main__":
    adventureGame()



