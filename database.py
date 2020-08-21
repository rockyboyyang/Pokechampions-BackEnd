from faker import Faker
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
load_dotenv()

fake = Faker()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import User, Trainer


with app.app_context():
    db.drop_all()
    db.create_all()
        
    demouser = User(username='satoshi', 
                    hashed_password=generate_password_hash('password'), 
                    rank='Novice',
                    boulderbadge=False,
                    cascadebadge=False,
                    thunderbadge=False,
                    rainbowbadge=False,
                    soulbadge=False,
                    marshbadge=False,
                    volcanobadge=False,
                    earthbadge=False,
                    beatElite4_1=False,
                    beatElite4_2=False,
                    beatElite4_3=False,
                    beatElite4_4=False,
                    beatChampion=False,
                    )
    
    brock = Trainer(
        name='brock',
        slot_1='{"pokemon": "golem", "pokemonType": [{"slot": 1, "type": {"name": "rock", "url": "https://pokeapi.co/api/v2/type/6/"}}, {"slot": 2, "type": {"name": "ground", "url": "https://pokeapi.co/api/v2/type/5/"}}], "pokemonStats": [{"base_stat": 80, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 120, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 130, "effort": 3, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 55, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 65, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 45, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "rock-slide", "power": 75, "pp": 10, "accuracy": 90, "damage_class": "physical", "type": "rock", "typeURL": "https://pokeapi.co/api/v2/type/6/", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to make the target flinch."}, "moveSlot_2": {"name": "body-slam", "power": 85, "pp": 15, "accuracy": 100, "damage_class": "physical", "type": "normal", "typeURL": "https://pokeapi.co/api/v2/type/1/", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to paralyze the target."}, "moveSlot_3": {"name": "thunder-punch", "power": 75, "pp": 15, "accuracy": 100, "damage_class": "physical", "type": "electric", "typeURL": "https://pokeapi.co/api/v2/type/13/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to paralyze the target."}, "moveSlot_4": {"name": "earthquake", "power": 100, "pp": 10, "accuracy": 100, "damage_class": "physical", "type": "ground", "typeURL": "https://pokeapi.co/api/v2/type/5/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage. If the target is in the first turn of dig, this move will hit with double powernull."}}',
        slot_2='{"pokemon": "kabutops", "pokemonType": [{"slot": 1, "type": {"name": "rock", "url": "https://pokeapi.co/api/v2/type/6/"}}, {"slot": 2, "type": {"name": "water", "url": "https://pokeapi.co/api/v2/type/11/"}}], "pokemonStats": [{"base_stat": 60, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 115, "effort": 2, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 105, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 65, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 70, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 80, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "x-scissor", "power": 80, "pp": 15, "accuracy": 100, "damage_class": "physical", "type": "bug", "typeURL": "https://pokeapi.co/api/v2/type/7/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damagenull."}, "moveSlot_2": {"name": "aqua-jet", "power": 40, "pp": 20, "accuracy": 100, "damage_class": "physical", "type": "water", "typeURL": "https://pokeapi.co/api/v2/type/11/", "stat_changes": [], "priority": 1, "effect_chance": null, "effect": "Inflicts regular damagenull."}, "moveSlot_3": {"name": "rock-slide", "power": 75, "pp": 10, "accuracy": 90, "damage_class": "physical", "type": "rock", "typeURL": "https://pokeapi.co/api/v2/type/6/", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to make the target flinch."}, "moveSlot_4": {"name": "aqua-tail", "power": 90, "pp": 10, "accuracy": 90, "damage_class": "physical", "type": "water", "typeURL": "https://pokeapi.co/api/v2/type/11/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damagenull."}}',
        slot_3='{"pokemon": "rhydon", "pokemonType": [{"slot": 1, "type": {"name": "ground", "url": "https://pokeapi.co/api/v2/type/5/"}}, {"slot": 2, "type": {"name": "rock", "url": "https://pokeapi.co/api/v2/type/6/"}}], "pokemonStats": [{"base_stat": 105, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 130, "effort": 2, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 120, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 45, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 45, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 40, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "stone-edge", "power": 100, "pp": 5, "accuracy": 80, "damage_class": "physical", "type": "rock", "typeURL": "https://pokeapi.co/api/v2/type/6/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage.  User\'s critical hit rate is one level higher when using this movenull."}, "moveSlot_2": {"name": "smart-strike", "power": 70, "pp": 10, "accuracy": null, "damage_class": "physical", "type": "steel", "typeURL": "https://pokeapi.co/api/v2/type/9/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage.  Ignores accuracy and evasion modifiersnull."}, "moveSlot_3": {"name": "superpower", "power": 120, "pp": 5, "accuracy": 100, "damage_class": "physical", "type": "fighting", "typeURL": "https://pokeapi.co/api/v2/type/2/", "stat_changes": [{"change": -1, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"change": -1, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}], "priority": 0, "effect_chance": 100, "effect": "Inflicts regular damage, then lowers the user\'s Attack and Defense by one stage each100."}, "moveSlot_4": {"name": "drill-run", "power": 80, "pp": 10, "accuracy": 95, "damage_class": "physical", "type": "ground", "typeURL": "https://pokeapi.co/api/v2/type/5/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage.  User\'s critical hit rate is one level higher when using this movenull."}}',
        slot_4='{"pokemon": "aerodactyl", "pokemonType": [{"slot": 1, "type": {"name": "rock", "url": "https://pokeapi.co/api/v2/type/6/"}}, {"slot": 2, "type": {"name": "flying", "url": "https://pokeapi.co/api/v2/type/3/"}}], "pokemonStats": [{"base_stat": 80, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 105, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 65, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 60, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 75, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 130, "effort": 2, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "ice-fang", "power": 65, "pp": 15, "accuracy": 95, "damage_class": "physical", "type": "ice", "typeURL": "https://pokeapi.co/api/v2/type/15/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to freeze the target and a separate $effect_chance% chance to make the target flinch."}, "moveSlot_2": {"name": "stone-edge", "power": 100, "pp": 5, "accuracy": 80, "damage_class": "physical", "type": "rock", "typeURL": "https://pokeapi.co/api/v2/type/6/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage.  User\'s critical hit rate is one level higher when using this movenull."}, "moveSlot_3": {"name": "steel-wing", "power": 70, "pp": 25, "accuracy": 90, "damage_class": "physical", "type": "steel", "typeURL": "https://pokeapi.co/api/v2/type/9/", "stat_changes": [{"change": 1, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage. Has a 10% chance to raise the user\'s Defense one stage."}, "moveSlot_4": {"name": "air-cutter", "power": 60, "pp": 25, "accuracy": 95, "damage_class": "special", "type": "flying", "typeURL": "https://pokeapi.co/api/v2/type/3/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage.  User\'s critical hit rate is one level higher when using this movenull."}}',
        slot_5='{"pokemon": "omastar", "pokemonType": [{"slot": 1, "type": {"name": "rock", "url": "https://pokeapi.co/api/v2/type/6/"}}, {"slot": 2, "type": {"name": "water", "url": "https://pokeapi.co/api/v2/type/11/"}}], "pokemonStats": [{"base_stat": 70, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 60, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 125, "effort": 2, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 115, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 70, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 55, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "earth-power", "power": 90, "pp": 10, "accuracy": 100, "damage_class": "special", "type": "ground", "typeURL": "https://pokeapi.co/api/v2/type/5/", "stat_changes": [{"change": -1, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to lower the target\'s Special Defense by one stage."}, "moveSlot_2": {"name": "hydro-pump", "power": 110, "pp": 5, "accuracy": 80, "damage_class": "special", "type": "water", "typeURL": "https://pokeapi.co/api/v2/type/11/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damagenull."}, "moveSlot_3": {"name": "ice-beam", "power": 90, "pp": 10, "accuracy": 100, "damage_class": "special", "type": "ice", "typeURL": "https://pokeapi.co/api/v2/type/15/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to freeze the target."}, "moveSlot_4": {"name": "ancient-power", "power": 60, "pp": 5, "accuracy": 100, "damage_class": "special", "type": "rock", "typeURL": "https://pokeapi.co/api/v2/type/6/", "stat_changes": [{"change": 1, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"change": 1, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"change": 1, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"change": 1, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"change": 1, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"change": 1, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage. Has a 10% chance to raise all of the user\'s stats one stage."}}',
        slot_6='{"pokemon": "onix", "pokemonType": [{"slot": 1, "type": {"name": "rock", "url": "https://pokeapi.co/api/v2/type/6/"}}, {"slot": 2, "type": {"name": "ground", "url": "https://pokeapi.co/api/v2/type/5/"}}], "pokemonStats": [{"base_stat": 35, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 45, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 160, "effort": 1, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 30, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 45, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 70, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "rock-slide", "power": 75, "pp": 10, "accuracy": 90, "damage_class": "physical", "type": "rock", "typeURL": "https://pokeapi.co/api/v2/type/6/", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to make the target flinch."}, "moveSlot_2": {"name": "earthquake", "power": 100, "pp": 10, "accuracy": 100, "damage_class": "physical", "type": "ground", "typeURL": "https://pokeapi.co/api/v2/type/5/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage. If the target is in the first turn of dig, this move will hit with double powernull."}, "moveSlot_3": {"name": "body-slam", "power": 85, "pp": 15, "accuracy": 100, "damage_class": "physical", "type": "normal", "typeURL": "https://pokeapi.co/api/v2/type/1/", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to paralyze the target."}, "moveSlot_4": {"name": "iron-head", "power": 80, "pp": 15, "accuracy": 100, "damage_class": "physical", "type": "steel", "typeURL": "https://pokeapi.co/api/v2/type/9/", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to make the target flinch."}}',
        trainerClass="Gym Leader",
        bio="The Gym Leader of Pewter City who specializes in Rock-Type Pokemon.  Befitting of him because he is as hard as a rock.",
        pre_battle_quote="So, you're here. I'm Brock. I'm Pewter's Gym Leader. My rock-hard willpower is evident even in my Pokémon. My Pokémon are all rock hard, and have true-grit determination. That's right - my Pokémon are all Rock type! Fuhaha! You're going to challenge me knowing that you'll lose? That's the Trainer's honor that compels you to challenge me. Fine, then! Show me your best!",
        post_battle_quote="I took you for granted, and so I lost. As proof of your victory, I confer on you this...the official Pokémon League BoulderBadge.",
    )

    misty = Trainer(
        name='misty',
        slot_1='{"pokemon": "golduck", "pokemonType": [{"slot": 1, "type": {"name": "water", "url": "https://pokeapi.co/api/v2/type/11/"}}], "pokemonStats": [{"base_stat": 80, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 82, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 78, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 95, "effort": 2, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 80, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 85, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "psychic", "power": 90, "pp": 10, "accuracy": 100, "damage_class": "special", "type": "psychic", "typeURL": "https://pokeapi.co/api/v2/type/14/", "stat_changes": [{"change": -1, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to lower the target\'s Special Defense by one stage."}, "moveSlot_2": {"name": "blizzard", "power": 110, "pp": 5, "accuracy": 70, "damage_class": "special", "type": "ice", "typeURL": "https://pokeapi.co/api/v2/type/15/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to freeze the target. During hail, this move has 100% accuracy.  It also has a (100 - accuracy)% chance to break through the protection of protect and detect."}, "moveSlot_3": {"name": "signal-beam", "power": 75, "pp": 15, "accuracy": 100, "damage_class": "special", "type": "bug", "typeURL": "https://pokeapi.co/api/v2/type/7/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to confuse the target."}, "moveSlot_4": {"name": "hydro-pump", "power": 110, "pp": 5, "accuracy": 80, "damage_class": "special", "type": "water", "typeURL": "https://pokeapi.co/api/v2/type/11/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damagenull."}}',
        slot_2='{"pokemon": "seadra", "pokemonType": [{"slot": 1, "type": {"name": "water", "url": "https://pokeapi.co/api/v2/type/11/"}}], "pokemonStats": [{"base_stat": 55, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 65, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 95, "effort": 1, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 95, "effort": 1, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 45, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 85, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "dragon-pulse", "power": 85, "pp": 10, "accuracy": 100, "damage_class": "special", "type": "dragon", "typeURL": "https://pokeapi.co/api/v2/type/16/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damagenull."}, "moveSlot_2": {"name": "blizzard", "power": 110, "pp": 5, "accuracy": 70, "damage_class": "special", "type": "ice", "typeURL": "https://pokeapi.co/api/v2/type/15/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to freeze the target. During hail, this move has 100% accuracy.  It also has a (100 - accuracy)% chance to break through the protection of protect and detect."}, "moveSlot_3": {"name": "signal-beam", "power": 75, "pp": 15, "accuracy": 100, "damage_class": "special", "type": "bug", "typeURL": "https://pokeapi.co/api/v2/type/7/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to confuse the target."}, "moveSlot_4": {"name": "hydro-pump", "power": 110, "pp": 5, "accuracy": 80, "damage_class": "special", "type": "water", "typeURL": "https://pokeapi.co/api/v2/type/11/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damagenull."}}',
        slot_3='{"pokemon": "dewgong", "pokemonType": [{"slot": 1, "type": {"name": "water", "url": "https://pokeapi.co/api/v2/type/11/"}}, {"slot": 2, "type": {"name": "ice", "url": "https://pokeapi.co/api/v2/type/15/"}}], "pokemonStats": [{"base_stat": 90, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 70, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 80, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 70, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 95, "effort": 2, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 70, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "surf", "power": 90, "pp": 15, "accuracy": 100, "damage_class": "special", "type": "water", "typeURL": "https://pokeapi.co/api/v2/type/11/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage. If the target is in the first turn of dive, this move will hit with double powernull."}, "moveSlot_2": {"name": "ice-beam", "power": 90, "pp": 10, "accuracy": 100, "damage_class": "special", "type": "ice", "typeURL": "https://pokeapi.co/api/v2/type/15/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to freeze the target."}, "moveSlot_3": {"name": "ice-shard", "power": 40, "pp": 30, "accuracy": 100, "damage_class": "physical", "type": "ice", "typeURL": "https://pokeapi.co/api/v2/type/15/", "stat_changes": [], "priority": 1, "effect_chance": null, "effect": "Inflicts regular damagenull."}, "moveSlot_4": {"name": "aqua-jet", "power": 40, "pp": 20, "accuracy": 100, "damage_class": "physical", "type": "water", "typeURL": "https://pokeapi.co/api/v2/type/11/", "stat_changes": [], "priority": 1, "effect_chance": null, "effect": "Inflicts regular damagenull."}}',
        slot_4='{"pokemon": "gyarados", "pokemonType": [{"slot": 1, "type": {"name": "water", "url": "https://pokeapi.co/api/v2/type/11/"}}, {"slot": 2, "type": {"name": "flying", "url": "https://pokeapi.co/api/v2/type/3/"}}], "pokemonStats": [{"base_stat": 95, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 125, "effort": 2, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 79, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 60, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 100, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 81, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "waterfall", "power": 80, "pp": 15, "accuracy": 100, "damage_class": "physical", "type": "water", "typeURL": "https://pokeapi.co/api/v2/type/11/", "stat_changes": [], "priority": 0, "effect_chance": 20, "effect": "Inflicts regular damage.  Has a 20% chance to make the target flinch."}, "moveSlot_2": {"name": "earthquake", "power": 100, "pp": 10, "accuracy": 100, "damage_class": "physical", "type": "ground", "typeURL": "https://pokeapi.co/api/v2/type/5/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage. If the target is in the first turn of dig, this move will hit with double powernull."}, "moveSlot_3": {"name": "stone-edge", "power": 100, "pp": 5, "accuracy": 80, "damage_class": "physical", "type": "rock", "typeURL": "https://pokeapi.co/api/v2/type/6/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage.  User\'s critical hit rate is one level higher when using this movenull."}, "moveSlot_4": {"name": "ice-fang", "power": 65, "pp": 15, "accuracy": 95, "damage_class": "physical", "type": "ice", "typeURL": "https://pokeapi.co/api/v2/type/15/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to freeze the target and a separate $effect_chance% chance to make the target flinch."}}',
        slot_5='{"pokemon": "vaporeon", "pokemonType": [{"slot": 1, "type": {"name": "water", "url": "https://pokeapi.co/api/v2/type/11/"}}], "pokemonStats": [{"base_stat": 130, "effort": 2, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 65, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 60, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 110, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 95, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 65, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "shadow-ball", "power": 80, "pp": 15, "accuracy": 100, "damage_class": "special", "type": "ghost", "typeURL": "https://pokeapi.co/api/v2/type/8/", "stat_changes": [{"change": -1, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}], "priority": 0, "effect_chance": 20, "effect": "Inflicts regular damage.  Has a 20% chance to lower the target\'s Special Defense by one stage."}, "moveSlot_2": {"name": "hydro-pump", "power": 110, "pp": 5, "accuracy": 80, "damage_class": "special", "type": "water", "typeURL": "https://pokeapi.co/api/v2/type/11/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damagenull."}, "moveSlot_3": {"name": "signal-beam", "power": 75, "pp": 15, "accuracy": 100, "damage_class": "special", "type": "bug", "typeURL": "https://pokeapi.co/api/v2/type/7/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to confuse the target."}, "moveSlot_4": {"name": "ice-beam", "power": 90, "pp": 10, "accuracy": 100, "damage_class": "special", "type": "ice", "typeURL": "https://pokeapi.co/api/v2/type/15/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to freeze the target."}}',
        slot_6='{"pokemon": "starmie", "pokemonType": [{"slot": 1, "type": {"name": "water", "url": "https://pokeapi.co/api/v2/type/11/"}}, {"slot": 2, "type": {"name": "psychic", "url": "https://pokeapi.co/api/v2/type/14/"}}], "pokemonStats": [{"base_stat": 60, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 75, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 85, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 100, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 85, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 115, "effort": 2, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "hydro-pump", "power": 110, "pp": 5, "accuracy": 80, "damage_class": "special", "type": "water", "typeURL": "https://pokeapi.co/api/v2/type/11/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damagenull."}, "moveSlot_2": {"name": "thunderbolt", "power": 90, "pp": 15, "accuracy": 100, "damage_class": "special", "type": "electric", "typeURL": "https://pokeapi.co/api/v2/type/13/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to paralyze the target."}, "moveSlot_3": {"name": "psychic", "power": 90, "pp": 10, "accuracy": 100, "damage_class": "special", "type": "psychic", "typeURL": "https://pokeapi.co/api/v2/type/14/", "stat_changes": [{"change": -1, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to lower the target\'s Special Defense by one stage."}, "moveSlot_4": {"name": "blizzard", "power": 110, "pp": 5, "accuracy": 70, "damage_class": "special", "type": "ice", "typeURL": "https://pokeapi.co/api/v2/type/15/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to freeze the target. During hail, this move has 100% accuracy.  It also has a (100 - accuracy)% chance to break through the protection of protect and detect."}}',
        trainerClass="Gym Leader",
        bio="The Gym Leader of Cerulean City who specializes in Water-Type Pokemon.  Misty is a trainer who's going to keep improving.  She won't lose to someone like you!",
        pre_battle_quote="Hi, you're a new face! Only those Trainers who have a policy about Pokémon can turn pro. What is your approach when you catch and train Pokémon? My policy is an all out offensive with Water-type Pokémon!",
        post_battle_quote="Wow! You're too much, all right! You can have the CascadeBadge to show that you beat me.",
    )

    ltsurge = Trainer(
        name='ltsurge',
        slot_1='{"pokemon": "electrode", "pokemonType": [{"slot": 1, "type": {"name": "electric", "url": "https://pokeapi.co/api/v2/type/13/"}}], "pokemonStats": [{"base_stat": 60, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 50, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 70, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 80, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 80, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 150, "effort": 2, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "signal-beam", "power": 75, "pp": 15, "accuracy": 100, "damage_class": "special", "type": "bug", "typeURL": "https://pokeapi.co/api/v2/type/7/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to confuse the target."}, "moveSlot_2": {"name": "thunder", "power": 110, "pp": 10, "accuracy": 70, "damage_class": "special", "type": "electric", "typeURL": "https://pokeapi.co/api/v2/type/13/", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to paralyze the target. During rain dance, this move has 100% accuracy.  It also has a (100 - accuracy)% chance to break through the protection of protect and detect. During sunny day, this move has 50% accuracy."}, "moveSlot_3": {"name": "swift", "power": 60, "pp": 20, "accuracy": null, "damage_class": "special", "type": "normal", "typeURL": "https://pokeapi.co/api/v2/type/1/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage.  Ignores accuracy and evasion modifiersnull."}, "moveSlot_4": {"name": "foul-play", "power": 95, "pp": 15, "accuracy": 100, "damage_class": "physical", "type": "dark", "typeURL": "https://pokeapi.co/api/v2/type/17/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage.  Damage is calculated using the target\'s attacking stat rather than the user\'s."}}',
        slot_2='{"pokemon": "electrode", "pokemonType": [{"slot": 1, "type": {"name": "electric", "url": "https://pokeapi.co/api/v2/type/13/"}}], "pokemonStats": [{"base_stat": 60, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 50, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 70, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 80, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 80, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 150, "effort": 2, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "signal-beam", "power": 75, "pp": 15, "accuracy": 100, "damage_class": "special", "type": "bug", "typeURL": "https://pokeapi.co/api/v2/type/7/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to confuse the target."}, "moveSlot_2": {"name": "thunder", "power": 110, "pp": 10, "accuracy": 70, "damage_class": "special", "type": "electric", "typeURL": "https://pokeapi.co/api/v2/type/13/", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to paralyze the target. During rain dance, this move has 100% accuracy.  It also has a (100 - accuracy)% chance to break through the protection of protect and detect. During sunny day, this move has 50% accuracy."}, "moveSlot_3": {"name": "swift", "power": 60, "pp": 20, "accuracy": null, "damage_class": "special", "type": "normal", "typeURL": "https://pokeapi.co/api/v2/type/1/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage.  Ignores accuracy and evasion modifiersnull."}, "moveSlot_4": {"name": "foul-play", "power": 95, "pp": 15, "accuracy": 100, "damage_class": "physical", "type": "dark", "typeURL": "https://pokeapi.co/api/v2/type/17/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage.  Damage is calculated using the target\'s attacking stat rather than the user\'s."}}',
        slot_3='{"pokemon": "electabuzz", "pokemonType": [{"slot": 1, "type": {"name": "electric", "url": "https://pokeapi.co/api/v2/type/13/"}}], "pokemonStats": [{"base_stat": 65, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 83, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 57, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 95, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 85, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 105, "effort": 2, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "signal-beam", "power": 75, "pp": 15, "accuracy": 100, "damage_class": "special", "type": "bug", "typeURL": "https://pokeapi.co/api/v2/type/7/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to confuse the target."}, "moveSlot_2": {"name": "thunder", "power": 110, "pp": 10, "accuracy": 70, "damage_class": "special", "type": "electric", "typeURL": "https://pokeapi.co/api/v2/type/13/", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to paralyze the target. During rain dance, this move has 100% accuracy.  It also has a (100 - accuracy)% chance to break through the protection of protect and detect. During sunny day, this move has 50% accuracy."}, "moveSlot_3": {"name": "ice-punch", "power": 75, "pp": 15, "accuracy": 100, "damage_class": "physical", "type": "ice", "typeURL": "https://pokeapi.co/api/v2/type/15/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to freeze the target."}, "moveSlot_4": {"name": "focus-blast", "power": 120, "pp": 5, "accuracy": 70, "damage_class": "special", "type": "fighting", "typeURL": "https://pokeapi.co/api/v2/type/2/", "stat_changes": [{"change": -1, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to lower the target\'s Special Defense by one stage."}}',
        slot_4='{"pokemon": "magneton", "pokemonType": [{"slot": 1, "type": {"name": "electric", "url": "https://pokeapi.co/api/v2/type/13/"}}, {"slot": 2, "type": {"name": "steel", "url": "https://pokeapi.co/api/v2/type/9/"}}], "pokemonStats": [{"base_stat": 50, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 60, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 95, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 120, "effort": 2, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 70, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 70, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "tri-attack", "power": 80, "pp": 10, "accuracy": 100, "damage_class": "special", "type": "normal", "typeURL": "https://pokeapi.co/api/v2/type/1/", "stat_changes": [], "priority": 0, "effect_chance": 20, "effect": "Inflicts regular damage.  Has a 20% chance to burn, freeze, or paralyze the target.  One of these effects is selected at random; they do not each have independent chances to occur."}, "moveSlot_2": {"name": "thunder", "power": 110, "pp": 10, "accuracy": 70, "damage_class": "special", "type": "electric", "typeURL": "https://pokeapi.co/api/v2/type/13/", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to paralyze the target. During rain dance, this move has 100% accuracy.  It also has a (100 - accuracy)% chance to break through the protection of protect and detect. During sunny day, this move has 50% accuracy."}, "moveSlot_3": {"name": "signal-beam", "power": 75, "pp": 15, "accuracy": 100, "damage_class": "special", "type": "bug", "typeURL": "https://pokeapi.co/api/v2/type/7/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to confuse the target."}, "moveSlot_4": {"name": "flash-cannon", "power": 80, "pp": 10, "accuracy": 100, "damage_class": "special", "type": "steel", "typeURL": "https://pokeapi.co/api/v2/type/9/", "stat_changes": [{"change": -1, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to lower the target\'s Special Defense by one stage."}}',
        slot_5='{"pokemon": "jolteon", "pokemonType": [{"slot": 1, "type": {"name": "electric", "url": "https://pokeapi.co/api/v2/type/13/"}}], "pokemonStats": [{"base_stat": 65, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 65, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 60, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 110, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 95, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 130, "effort": 2, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "signal-beam", "power": 75, "pp": 15, "accuracy": 100, "damage_class": "special", "type": "bug", "typeURL": "https://pokeapi.co/api/v2/type/7/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to confuse the target."}, "moveSlot_2": {"name": "thunder", "power": 110, "pp": 10, "accuracy": 70, "damage_class": "special", "type": "electric", "typeURL": "https://pokeapi.co/api/v2/type/13/", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to paralyze the target. During rain dance, this move has 100% accuracy.  It also has a (100 - accuracy)% chance to break through the protection of protect and detect. During sunny day, this move has 50% accuracy."}, "moveSlot_3": {"name": "hyper-voice", "power": 90, "pp": 10, "accuracy": 100, "damage_class": "special", "type": "normal", "typeURL": "https://pokeapi.co/api/v2/type/1/", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damagenull."}, "moveSlot_4": {"name": "shadow-ball", "power": 80, "pp": 15, "accuracy": 100, "damage_class": "special", "type": "ghost", "typeURL": "https://pokeapi.co/api/v2/type/8/", "stat_changes": [{"change": -1, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}], "priority": 0, "effect_chance": 20, "effect": "Inflicts regular damage.  Has a 20% chance to lower the target\'s Special Defense by one stage."}}',
        slot_6='{"pokemon": "raichu", "pokemonType": [{"slot": 1, "type": {"name": "electric", "url": "https://pokeapi.co/api/v2/type/13/"}}], "pokemonStats": [{"base_stat": 60, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 90, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 55, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 90, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 80, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 110, "effort": 3, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "signal-beam", "power": 75, "pp": 15, "accuracy": 100, "damage_class": "special", "type": "bug", "typeURL": "https://pokeapi.co/api/v2/type/7/", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to confuse the target."}, "moveSlot_2": {"name": "thunder", "power": 110, "pp": 10, "accuracy": 70, "damage_class": "special", "type": "electric", "typeURL": "https://pokeapi.co/api/v2/type/13/", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to paralyze the target. During rain dance, this move has 100% accuracy.  It also has a (100 - accuracy)% chance to break through the protection of protect and detect. During sunny day, this move has 50% accuracy."}, "moveSlot_3": {"name": "iron-tail", "power": 100, "pp": 15, "accuracy": 75, "damage_class": "physical", "type": "steel", "typeURL": "https://pokeapi.co/api/v2/type/9/", "stat_changes": [{"change": -1, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to lower the target\'s Defense by one stage."}, "moveSlot_4": {"name": "focus-blast", "power": 120, "pp": 5, "accuracy": 70, "damage_class": "special", "type": "fighting", "typeURL": "https://pokeapi.co/api/v2/type/2/", "stat_changes": [{"change": -1, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to lower the target\'s Special Defense by one stage."}}',
        trainerClass="Gym Leader",
        bio='Also known as the Lightning Liutenant.  He was a soldier who fought in a war, during which Electric-type Pokemon saved his life!',
        pre_battle_quote="Hey, kid! What do you think you're doing here? You won't live long in combat! Not with your puny power! I tell you, kid, electric Pokémon saved me during the war! They zapped my enemies into paralysis! The same as I'll do to you!",
        post_battle_quote="Now that's a shocker! You're the real deal, kid! Fine, then, take the ThunderBadge!",
    )

    erika = Trainer(
        name='erika'
        slot_1='',
        slot_2='',
        slot_3='',
        slot_4='',
        slot_5='',
        slot_6='',
        trainerClass="Gym Leader",
        bio='',
        pre_battle_quote='',
        post_battle_quote='',
    )

    koga = Trainer(
        name='koga'
        slot_1='',
        slot_2='',
        slot_3='',
        slot_4='',
        slot_5='',
        slot_6='',
        trainerClass="Gym Leader",
        bio='',
        pre_battle_quote='',
        post_battle_quote='',
    )

    sabrina = Trainer(
        name='sabrina'
        slot_1='',
        slot_2='',
        slot_3='',
        slot_4='',
        slot_5='',
        slot_6='',
        trainerClass="Gym Leader",
        bio='',
        pre_battle_quote='',
        post_battle_quote='',
    )

    blaine = Trainer(
        name='blaine'
        slot_1='',
        slot_2='',
        slot_3='',
        slot_4='',
        slot_5='',
        slot_6='',
        trainerClass="Gym Leader",
        bio='',
        pre_battle_quote='',
        post_battle_quote='',
    )

    giovanni = Trainer(
        name='giovanni'
        slot_1='',
        slot_2='',
        slot_3='',
        slot_4='',
        slot_5='',
        slot_6='',
        trainerClass="Gym Leader",
        bio='',
        pre_battle_quote='',
        post_battle_quote='',
    )

    lorelei = Trainer(
        name='lorelei'
        slot_1='',
        slot_2='',
        slot_3='',
        slot_4='',
        slot_5='',
        slot_6='',
        trainerClass="Elite Four",
        bio='',
        pre_battle_quote='',
        post_battle_quote='',
    )

    bruno = Trainer(
        name='bruno'
        slot_1='',
        slot_2='',
        slot_3='',
        slot_4='',
        slot_5='',
        slot_6='',
        trainerClass="Elite Four",
        bio='',
        pre_battle_quote='',
        post_battle_quote='',
    )

    agatha = Trainer(
        name='agatha'
        slot_1='',
        slot_2='',
        slot_3='',
        slot_4='',
        slot_5='',
        slot_6='',
        trainerClass="Elite Four",
        bio='',
        pre_battle_quote='',
        post_battle_quote='',
    )

    lance = Trainer(
        name='lance'
        slot_1='',
        slot_2='',
        slot_3='',
        slot_4='',
        slot_5='',
        slot_6='',
        trainerClass="Elite Four",
        bio='',
        pre_battle_quote='',
        post_battle_quote='',
    )

    rocky = Trainer(
        name='rocky'
        slot_1='',
        slot_2='',
        slot_3='',
        slot_4='',
        slot_5='',
        slot_6='',
        trainerClass="Pokemon Champion",
        bio='',
        pre_battle_quote='',
        post_battle_quote='',
    )

    db.session.add(demouser)
    db.session.add(brock)
    db.session.add(misty)
    


    # db.session.add(Chat(jobseekers_id=1, companies_id=1))
    # db.session.add(Chat(jobseekers_id=1, companies_id=3))
    # db.session.add(Chat(jobseekers_id=2, companies_id=1))
    # db.session.add(Chat(jobseekers_id=2, companies_id=3))
    # db.session.add(Chat(jobseekers_id=3, companies_id=3))
    # db.session.add(Chat(jobseekers_id=3, companies_id=4))
    # db.session.add(Chat(jobseekers_id=4, companies_id=2))
    # db.session.add(Chat(jobseekers_id=4, companies_id=4))
    # db.session.add(Chat(jobseekers_id=5, companies_id=2))
    # db.session.add(Chat(jobseekers_id=5, companies_id=5))

    # jobs = [fake.job(), fake.job(), fake.job(), fake.job(), fake.job()]
    # db.session.add(Experience(title=jobs[0], jobseekers_id=1, date_start='now', date_end='now', description=fake.text()))
    # db.session.add(Experience(title=jobs[1], jobseekers_id=2, date_start='now', date_end='now', description=fake.text()))
    # db.session.add(Experience(title=jobs[2], jobseekers_id=3, date_start='now', date_end='now', description=fake.text()))
    # db.session.add(Experience(title=jobs[3], jobseekers_id=4, date_start='now', date_end='now', description=fake.text()))
    # db.session.add(Experience(title=jobs[4], jobseekers_id=5, date_start='now', date_end='now', description=fake.text()))

    # db.session.add(Opening(companies_id=1, title=jobs[0], description=fake.text(), created_at='now'))
    # db.session.add(Opening(companies_id=1, title=jobs[1], description=fake.text(), created_at='now'))
    # db.session.add(Opening(companies_id=2, title=jobs[3], description=fake.text(), created_at='now'))
    # db.session.add(Opening(companies_id=2, title=jobs[4], description=fake.text(), created_at='now'))
    # db.session.add(Opening(companies_id=3, title=jobs[0], description=fake.text(), created_at='now'))
    # db.session.add(Opening(companies_id=3, title=jobs[1], description=fake.text(), created_at='now'))
    # db.session.add(Opening(companies_id=3, title=jobs[2], description=fake.text(), created_at='now'))
    # db.session.add(Opening(companies_id=4, title=jobs[3], description=fake.text(), created_at='now'))
    # db.session.add(Opening(companies_id=5, title=jobs[4], description=fake.text(), created_at='now'))

    # companies = Company.query.all()
    # jobseekers = Jobseeker.query.all()
    # openings = []
    # _ = [openings.extend(c.openings) for c in companies]
    # for opening in openings:
    #     for jobseeker in jobseekers:
    #         db.session.add(Swipe(jobseekers_id=jobseeker.id, openings_id=opening.id, created_at='now', swiped_right=True, super_swipe=True, role='company'))

    db.session.commit()
