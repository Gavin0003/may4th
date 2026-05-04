import random


characters = [
    "Jedi Knight",
    "Padawan",
    "Rebel Pilot",
    "Mandalorian",
    "Smuggler",
    "Clone Trooper",
    "Resistance Spy"
]

planets = [
    "Tatooine",
    "Hoth",
    "Endor",
    "Naboo",
    "Coruscant",
    "Dagobah",
    "Mustafar"
]

missions = [
    "rescue a captured droid",
    "recover stolen battle plans",
    "escape an Imperial base",
    "protect a hidden Jedi temple",
    "deliver a secret message",
    "destroy a Sith weapon",
    "find a lost lightsaber"
]

enemies = [
    "Darth Vader",
    "a Sith Inquisitor",
    "stormtroopers",
    "bounty hunters",
    "a crime lord",
    "battle droids",
    "the First Order"
]

allies = [
    "R2-D2",
    "Chewbacca",
    "Ahsoka Tano",
    "Obi-Wan Kenobi",
    "BB-8",
    "a group of Ewoks",
    "a mysterious rebel informant"
]

ships = [
    "Millennium Falcon",
    "X-wing",
    "TIE fighter",
    "Naboo starfighter",
    "Razor Crest",
    "Jedi starfighter",
    "Corellian freighter"
]

def get_mission_details():
    character = random.choice(characters)
    planet = random.choice(planets)
    mission = random.choice(missions)
    enemy = random.choice(enemies)
    ally = random.choice(allies)
    ship = random.choice(ships)
    difficulty = random.randint(1, 10)
    if difficulty <= 3:
        difficulty_output = "This should be an easy mission."
    elif difficulty <= 7:
        difficulty_output = "This mission will be dangerous."
    else:
        difficulty_output = "This mission is extremely risky. I have a bad feeling about this."
    mission_details = [character, planet, mission, enemy, ally, ship, difficulty, difficulty_output]
    return mission_details

def display(info_list):
    print('==============================')    
    print('STAR WARS MISSION BRIEFING')
    print('==============================')  
    print(f'Character: {info_list[0]}')
    print(f'Planet: {info_list[1]}')
    print(f'Mission: {info_list[2]}')
    print(f'Enemy: {info_list[3]}')
    print(f'Ally: {info_list[4]}')
    print(f'Ship: {info_list[5]}')
    print(f'Difficulty: {info_list[6]}')

    print('\nBriefing:')
    print(f'A {info_list[0]} must travel to {info_list[1]} aboard the {info_list[5]}. With help from {info_list[4]}, they must {info_list[2]} before {info_list[3]} stops them. {info_list[7]} May the Force be with you.')

print("Welcome to the Star Wars Mission Generator!")

while True:
    choice = input("\nGenerate a new mission? yes/no: ").lower()

    if choice == "yes":
        display(get_mission_details())
    elif choice == "no":
        print("Goodbye, young Jedi.")
        break
    else:
        print("Please type yes or no.")
