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
        slot_1='{"pokemon": "golem", "pokemonType": [{"slot": 1, "type": {"name": "rock", "url": "https://pokeapi.co/api/v2/type/6/"}}, {"slot": 2, "type": {"name": "ground", "url": "https://pokeapi.co/api/v2/type/5/"}}], "pokemonStats": [{"base_stat": 80, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 120, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 130, "effort": 3, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 55, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 65, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 45, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "defense-curl", "power": null, "pp": 40, "accuracy": null, "damage_class": "status", "type": "normal", "stat_changes": [{"change": 1, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}], "priority": 0, "effect_chance": null, "effect": "Raises user\'s Defense by one stage. After this move is used, the power of ice ball and rollout are doubled until the user leaves the fieldnull."}, "moveSlot_2": {"name": "body-slam", "power": 85, "pp": 15, "accuracy": 100, "damage_class": "physical", "type": "normal", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to paralyze the target."}, "moveSlot_3": {"name": "rock-slide", "power": 75, "pp": 10, "accuracy": 90, "damage_class": "physical", "type": "rock", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to make the target flinch."}, "moveSlot_4": {"name": "earthquake", "power": 100, "pp": 10, "accuracy": 100, "damage_class": "physical", "type": "ground", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage. If the target is in the first turn of dig, this move will hit with double powernull."}}',
        slot_2='{"pokemon": "kabutops", "pokemonType": [{"slot": 1, "type": {"name": "rock", "url": "https://pokeapi.co/api/v2/type/6/"}}, {"slot": 2, "type": {"name": "water", "url": "https://pokeapi.co/api/v2/type/11/"}}], "pokemonStats": [{"base_stat": 60, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 115, "effort": 2, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 105, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 65, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 70, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 80, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "aqua-jet", "power": 40, "pp": 20, "accuracy": 100, "damage_class": "physical", "type": "water", "stat_changes": [], "priority": 1, "effect_chance": null, "effect": "Inflicts regular damagenull."}, "moveSlot_2": {"name": "rock-slide", "power": 75, "pp": 10, "accuracy": 90, "damage_class": "physical", "type": "rock", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to make the target flinch."}, "moveSlot_3": {"name": "swords-dance", "power": null, "pp": 20, "accuracy": null, "damage_class": "status", "type": "normal", "stat_changes": [{"change": 2, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}], "priority": 0, "effect_chance": null, "effect": "Raises the user\'s Attack by two stagesnull."}, "moveSlot_4": {"name": "x-scissor", "power": 80, "pp": 15, "accuracy": 100, "damage_class": "physical", "type": "bug", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damagenull."}}',
        slot_3='{"pokemon": "rhydon", "pokemonType": [{"slot": 1, "type": {"name": "ground", "url": "https://pokeapi.co/api/v2/type/5/"}}, {"slot": 2, "type": {"name": "rock", "url": "https://pokeapi.co/api/v2/type/6/"}}], "pokemonStats": [{"base_stat": 105, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 130, "effort": 2, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 120, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 45, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 45, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 40, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "smart-strike", "power": 70, "pp": 10, "accuracy": null, "damage_class": "physical", "type": "steel", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage.  Ignores accuracy and evasion modifiersnull."}, "moveSlot_2": {"name": "rock-slide", "power": 75, "pp": 10, "accuracy": 90, "damage_class": "physical", "type": "rock", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to make the target flinch."}, "moveSlot_3": {"name": "earthquake", "power": 100, "pp": 10, "accuracy": 100, "damage_class": "physical", "type": "ground", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage. If the target is in the first turn of dig, this move will hit with double powernull."}, "moveSlot_4": {"name": "rock-polish", "power": null, "pp": 20, "accuracy": null, "damage_class": "status", "type": "rock", "stat_changes": [{"change": 2, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "priority": 0, "effect_chance": null, "effect": "Raises the user\'s Speed by two stagesnull."}}',
        slot_4='{"pokemon": "aerodactyl", "pokemonType": [{"slot": 1, "type": {"name": "rock", "url": "https://pokeapi.co/api/v2/type/6/"}}, {"slot": 2, "type": {"name": "flying", "url": "https://pokeapi.co/api/v2/type/3/"}}], "pokemonStats": [{"base_stat": 80, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 105, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 65, "effort": 0, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 60, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 75, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 130, "effort": 2, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "stone-edge", "power": 100, "pp": 5, "accuracy": 80, "damage_class": "physical", "type": "rock", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage.  User\'s critical hit rate is one level higher when using this movenull."}, "moveSlot_2": {"name": "fire-fang", "power": 65, "pp": 15, "accuracy": 95, "damage_class": "physical", "type": "fire", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to burn the target and a separate $effect_chance% chance to make the target flinch."}, "moveSlot_3": {"name": "thunder-fang", "power": 65, "pp": 15, "accuracy": 95, "damage_class": "physical", "type": "electric", "stat_changes": [], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to paralyze the target and a separate $effect_chance% chance to make the target flinch."}, "moveSlot_4": {"name": "earthquake", "power": 100, "pp": 10, "accuracy": 100, "damage_class": "physical", "type": "ground", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage. If the target is in the first turn of dig, this move will hit with double powernull."}}',
        slot_5='{"pokemon": "onix", "pokemonType": [{"slot": 1, "type": {"name": "rock", "url": "https://pokeapi.co/api/v2/type/6/"}}, {"slot": 2, "type": {"name": "ground", "url": "https://pokeapi.co/api/v2/type/5/"}}], "pokemonStats": [{"base_stat": 35, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 45, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 160, "effort": 1, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 30, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 45, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 70, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "iron-head", "power": 80, "pp": 15, "accuracy": 100, "damage_class": "physical", "type": "steel", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to make the target flinch."}, "moveSlot_2": {"name": "earthquake", "power": 100, "pp": 10, "accuracy": 100, "damage_class": "physical", "type": "ground", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage. If the target is in the first turn of dig, this move will hit with double powernull."}, "moveSlot_3": {"name": "screech", "power": null, "pp": 40, "accuracy": 85, "damage_class": "status", "type": "normal", "stat_changes": [{"change": -2, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}], "priority": 0, "effect_chance": null, "effect": "Lowers the target\'s Defense by two stagesnull."}, "moveSlot_4": {"name": "stone-edge", "power": 100, "pp": 5, "accuracy": 80, "damage_class": "physical", "type": "rock", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Inflicts regular damage.  User\'s critical hit rate is one level higher when using this movenull."}}',
        slot_6='{"pokemon": "omastar", "pokemonType": [{"slot": 1, "type": {"name": "rock", "url": "https://pokeapi.co/api/v2/type/6/"}}, {"slot": 2, "type": {"name": "water", "url": "https://pokeapi.co/api/v2/type/11/"}}], "pokemonStats": [{"base_stat": 70, "effort": 0, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"base_stat": 60, "effort": 0, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"base_stat": 125, "effort": 2, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"base_stat": 115, "effort": 0, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"base_stat": 70, "effort": 0, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"base_stat": 55, "effort": 0, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "moveSlot_1": {"name": "shell-smash", "power": null, "pp": 15, "accuracy": null, "damage_class": "status", "type": "normal", "stat_changes": [], "priority": 0, "effect_chance": null, "effect": "Raises the user\'s Attack, Special Attack, and Speed by two stages each.  Lowers the user\'s Defense and Special Defense by one stage eachnull."}, "moveSlot_2": {"name": "scald", "power": 80, "pp": 15, "accuracy": 100, "damage_class": "special", "type": "water", "stat_changes": [], "priority": 0, "effect_chance": 30, "effect": "Inflicts regular damage.  Has a 30% chance to burn the target."}, "moveSlot_3": {"name": "ancient-power", "power": 60, "pp": 5, "accuracy": 100, "damage_class": "special", "type": "rock", "stat_changes": [{"change": 1, "stat": {"name": "hp", "url": "https://pokeapi.co/api/v2/stat/1/"}}, {"change": 1, "stat": {"name": "attack", "url": "https://pokeapi.co/api/v2/stat/2/"}}, {"change": 1, "stat": {"name": "defense", "url": "https://pokeapi.co/api/v2/stat/3/"}}, {"change": 1, "stat": {"name": "special-attack", "url": "https://pokeapi.co/api/v2/stat/4/"}}, {"change": 1, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}, {"change": 1, "stat": {"name": "speed", "url": "https://pokeapi.co/api/v2/stat/6/"}}], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage. Has a 10% chance to raise all of the user\'s stats one stage."}, "moveSlot_4": {"name": "earth-power", "power": 90, "pp": 10, "accuracy": 100, "damage_class": "special", "type": "ground", "stat_changes": [{"change": -1, "stat": {"name": "special-defense", "url": "https://pokeapi.co/api/v2/stat/5/"}}], "priority": 0, "effect_chance": 10, "effect": "Inflicts regular damage.  Has a 10% chance to lower the target\'s Special Defense by one stage."}}',
        trainerClass="Gym Leader",
        bio="The Gym Leader of Pewter City who specializes in Rock-Type Pokemon.  Befitting of him because he is as hard as a rock."
    )
    db.session.add(demouser)
    db.session.add(brock)
    


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
