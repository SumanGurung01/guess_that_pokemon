import random

pokemon = ["Aipom" , "Mew" , "Haunter" , "Primeape" , "Sandslash" , "Ekans" , "Alakazam" , "Ninetales" , "Onix" , "Cubone" , "Kabutops" , "Tauros" , "Zapdos"]
POKEMON_LIST =  ["Aipom" , "Mew" , "Haunter" , "Primeape" , "Sandslash" , "Ekans" , "Alakazam" , "Ninetales" , "Onix" , "Cubone" , "Kabutops" , "Tauros" , "Zapdos"]

pokemon_images = {
    "Aipom":{"reveal":"aipom" , "shadow":"aipom1"} , 
    "Mew" :{"reveal":"mew" , "shadow":"mew1"} , 
    "Haunter":{"reveal":"haunter" , "shadow":"haunter1"},
    "Primeape":{"reveal":"primeape" , "shadow":"primeape1"} ,
    "Sandslash":{"reveal":"sandslash" , "shadow":"sandslash1"},
    "Ekans" : {"reveal":"ekans" , "shadow":"ekans1"},
    "Alakazam" : {"reveal":"alakazam" , "shadow":"alakazam1"},
    "Ninetales" : {"reveal":"ninetales" , "shadow":"ninetales1"},
    "Onix" : {"reveal":"onix" , "shadow":"onix1"},
    "Cubone" : {"reveal":"cubone" , "shadow":"cubone1"},
    "Kabutops" : {"reveal":"kabutops" , "shadow":"kabutops1"},
    "Tauros" : {"reveal":"tauros" , "shadow":"tauros1"},
    "Zapdos" : {"reveal":"zapdos" , "shadow":"zapdos1"},
}

pokemon_details = {}

def generate_options(chosen_pokemon):
    option = []
    option.append(chosen_pokemon)
    while len(option)!=4:
        random_pokemon = random.choice(POKEMON_LIST)
        if random_pokemon not in option and random_pokemon not in option:
            option.append(random_pokemon)
    random.shuffle(option)
    return option


def get_random_pokemon():
    chosen_pokemon = random.choice(pokemon)
    pokemon.remove(chosen_pokemon)

    option = generate_options(chosen_pokemon)

    index = 0

    for i , curr_pokemon in enumerate(option , start=0):
        if curr_pokemon == chosen_pokemon:  
            index = i 

    pokemon_details["answer_index"] = index 
    pokemon_details["pokemon"] = chosen_pokemon
    pokemon_details["options"] = option
    pokemon_details["image"] = pokemon_images[chosen_pokemon]
    pokemon_details["total"] = len(pokemon)
    
    return pokemon_details

