import file_operations
from faker import Faker
import random
import os
from runic_alphabet import runic_alphabet

for i in range(1, 11):

    fake = Faker("ru_RU")
    first_name = fake.first_name()
    last_name = fake.last_name()
    town = fake.city()
    job = fake.job()
    strength = random.randint(3, 18)
    agility = random.randint(3, 18)
    endurance = random.randint(3, 18)
    intelligence = random.randint(3, 18)
    luck = random.randint(3, 18)

    skills = [
    "Стремительный прыжок", 
    "Электрический выстрел", 
    "Ледяной удар", 
    "Стремительный удар", 
    "Кислотный взгляд", 
    "Тайный побег", 
    "Ледяной выстрел", 
    "Огненный заряд"
    ]

    random_skills = random.sample(skills, 3)
    skill_1 = random_skills[0]
    skill_2 = random_skills[1]
    skill_3 = random_skills[2]

    for key, value in runic_alphabet.items():
        skill_1 = skill_1.replace(key, value)
        skill_2 = skill_2.replace(key, value)
        skill_3 = skill_3.replace(key, value)

    context = {
        "first_name": first_name,
        "last_name": last_name,
        "town": town,
        "job": job,
        "strength": strength,
        "agility": agility,
        "endurance": endurance,
        "intelligence": intelligence,
        "luck": luck,
        "skill_1": skill_1,
        "skill_2": skill_2,
        "skill_3": skill_3
    }

    os.makedirs("files", exist_ok=True)
    file_operations.render_template("template.svg", f'files/card-{i}.svg', context)
