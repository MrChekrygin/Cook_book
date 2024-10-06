from pprint import pprint


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    """Формирование списка покупок по блюдам и количеству персон."""
    shop_list = {}

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


# Вызов функции:
shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Макароны'], 2, cook_book)

# Вывод результата:
pprint(shop_list)
