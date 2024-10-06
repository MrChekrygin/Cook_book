def parse_ingredient(line):
    """Парсинг строки ингредиента в словарь."""
    ingredient_name, quantity, measure = [item.strip() for item in line.split('|')]
    return {
        'ingredient_name': ingredient_name,
        'quantity': int(quantity),
        'measure': measure
    }

def parse_recipe(file):
    """Парсинг файла с рецептами и создание словаря cook_book."""
    cook_book = {}
    with open(file, 'r', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()  # Чтение названия блюда
            if not dish_name:
                break  # Выход из цикла, если достигнут конец файла
            num_ingredients = int(f.readline().strip())  # Количества ингредиентов
            ingredients = []
            for _ in range(num_ingredients):
                ingredient_line = f.readline().strip()
                ingredients.append(parse_ingredient(ingredient_line))  # Парсинг ингредиента
            cook_book[dish_name] = ingredients  # Добавление блюда и его ингредиентов в словарь
            f.readline()  # Пропускаем пустую строку между рецептами
    return cook_book

file_path = 'files/recipes.txt'
cook_book = parse_recipe(file_path)

from pprint import pprint
pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    """Формирование списка покупок по блюдам и количеству персон."""
    shop_list = {}
    file_path = 'files/recipes.txt'  # Путь к файлу с рецептами
    cook_book = parse_recipe(file_path) # Парсинг файла с рецептами и создание словаря cook_book

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count  # Умножаем на количество персон
                measure = ingredient['measure']

                if name in shop_list:
                    shop_list[name]['quantity'] += quantity  # Если ингредиент уже есть, добавляем количество
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}  # Добавляем новый ингредиент
        else:
            print(f"Блюдо '{dish}' не найдено в cook_book")

    return shop_list

