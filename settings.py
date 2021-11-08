import json
import os

settings_file = os.path.dirname(__file__) + '/settings.json'
clear_file = os.path.dirname(__file__) + '/settings(clear).json'

budget = ''
day = 1
money = ''
waste = ''
wastes = []
moneys = 0
days = 0
budgets = []

def save_data():
    data = {
        'days': days,
        'moneys': moneys,
        'budgets': budgets,
        'money': money,
        'wastes': wastes
    }
    with open(settings_file, 'w',  encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def use_data():
    with open(settings_file, 'r', encoding='utf-8') as file:
        global moneys
        global budgets
        global money
        global wastes
        data = json.load(file)
        moneys = data['moneys']
        budgets = data['budgets']
        money = data['money']
        wastes = data['wastes']


def clear_all():
    with open(clear_file, 'r', encoding='utf-8') as file:
        global moneys
        global budgets
        global money
        global wastes
        data = json.load(file)
        moneys = data['moneys']
        budgets = data['budgets']
        money = data['money']
        wastes = data['wastes']


def clear_moneys_and_budgets():
    with open(clear_file, 'r', encoding='utf-8') as file:
        global moneys
        global budgets
        data = json.load(file)
        moneys = data['moneys']
        budgets = data['budgets']














































# hobbits = {
#     "Имя": "Бильбо",
#     "Фамилия": "Бэггинс",
#     "Хобби": ["Путешествия", "Писательство"],
#     "Возраст": 111,
#     "Семья": [
#         {
#             "Имя": "Фродо"
#         },
#         {
#             "Имя": "Банго Бэггинс",
#         }
#     ]
# }

# with open('./slozna/slozna/hobbits.json', 'w', encoding='utf-8') as file:
#     json.dump(hobbits, file, ensure_ascii=False)
#     # json_str = json.dumps(file, ensure_ascii=False, indent=2)
#     # print(json_str)

# with open('./slozna/slozna/hobbits.json', 'r', encoding='utf-8') as file:
#     hobbits = json.load(file)
#     print(type(hobbits))