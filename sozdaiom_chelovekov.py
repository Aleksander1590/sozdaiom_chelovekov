import file_operations
from faker import Faker
import random


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

population = ["Стремительный прыжок", "Электрический выстрел", "Ледяной удар", "Стремительный удар", "Кислотный взгляд", "Тайный побег", "Ледяной выстрел", "Огненный заряд"]


skills = random.sample(population, 3)
skill_1 = skills[0]
skill_2 = skills[1]
skill_3 = skills[2]

letters = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}

for key, value in letters.items():
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

files_names = ["file_1", "file_2", "file_3", "file_4", "file_5", "file_6", "file_7", "file_8", "file_9", "file_10"]


for i in range(10):
    file_operations.render_template("template.svg", f'{files_names[i]}.svg', context)
