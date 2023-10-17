import random
#Sierra's <3 game of cludeo 
# 21 5 22 15 12 9
# Define the characters, rooms, and weapons in the game
characters = ["Miss Scarlet", "Colonel Mustard", "Mrs. White", "Mr. Green", "Mrs. Peacock", "Professor Plum"]
rooms = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Cellar", "Billiard Room", "Library", "Lounge", "Hall", "Study"]
weapons = ["Candlestick", "Knife", "Lead Pipe", "Revolver", "Rope", "Wrench"]




# Create the confidential case file with a random solution
confidential_file = {
    "character": random.choice(characters),
    "room": random.choice(rooms),
    "weapon": random.choice(weapons)
}
# Removing the selected characters from possible playing cards 
for i in confidential_file.values():
    if i in characters:
        characters.remove(i)
    if i in rooms:
        rooms.remove(i)
    if i in weapons:
        weapons.remove(i)
players = []
num_players = int(input("Enter the number of players (2 to 6): "))
if num_players < 2 or num_players > 6:
    print("Invalid number of players. You can only play with 2 to 6 players.")
    exit()
for i in range(1, num_players + 1):
    player_name = input(f"Enter the name of Player {i}: ")
    players.append({"name": player_name, "cards": []})

all_cards = characters + rooms + weapons
random.shuffle(all_cards)

for i, card in enumerate(all_cards):
    player_index = i % num_players
    players[player_index]["cards"].append(card)
    file_name=str(players[player_index]["name"])+".txt"
    f=open(file_name,'w+')
    for k in players[player_index]["cards"]:
        adjusted=f"\n {k}"
        f.write(adjusted)
    f.close()

def make_suggestion(player, room):
    print(f"{player['name']}, you are in the {room}. Make a suggestion.")
    character = input("Suggest a character: ")
    weapon = input("Suggest a weapon: ")
    
    return {"character": character, "room": room, "weapon": weapon}
# Main game loop
running=True
while running:
    for player in players:
        print(f"\n{player['name']}'s turn:")
        current_room = random.choice(rooms)
        suggestion = make_suggestion(player, current_room)
        print(f"{player['name']} suggests that the murder was committed by {suggestion['character']} in the {suggestion['room']} with the {suggestion['weapon']}.")
        
        for other_player in players:
            if other_player != player:
                response = input(f"{other_player['name']}, do you have a card to disprove this suggestion? (Enter the card's name or 'no'): ")
                if response != 'no' and response in other_player['cards']:
                    print(f"{other_player['name']} shows a card to {player['name']}.")
        accusation_check=str(input(f"Do you {player['name']} want to make an accusation? y/n"))
        if accusation_check=='y' or accusation_check=="Y":
             accusation = {
             "character": input("Make an accusation. Who do you accuse? "),
             "room": input("Where do you accuse the murder took place? "),
             "weapon": input("Which weapon do you think was used? ")}
             if accusation == confidential_file:
                 print(f"Congratulations, {player['name']}! You've solved the case and won the game!")
                 break
             else:
                 print(f"Sorry, {player['name']}. Your accusation is incorrect. You are out of the game.")
                 num_players-1
                 response = input(f"Press Enter to end {player['name']}'s turn...")
                 if num_players==0:
                     running=False
                     

print("Game over!")

