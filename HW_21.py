

def read_cook_book():
    with open('Cook_book.txt', encoding='UTF-8') as file:
        cook_book = dict()
        for line in file:
            recipe_name = line.strip().lower()
            cook_book[recipe_name] = list()
            ingredients_count = file.readline()

            for ingredient in range(int(ingredients_count)):
                ingredients = file.readline().strip()
                ingredient_list = ingredients.split(' | ')
                dict_ingredient = {
                    'ingredient_name': ingredient_list[0],
                    'quantity': int(ingredient_list[1]),
                    'measure': ingredient_list[2]
                }
                cook_book[recipe_name].append(dict_ingredient)
            file.readline()

    return cook_book


def get_shop_list_by_dishes(person_count, dishes, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    cook_book = read_cook_book()
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(person_count, dishes, cook_book)
    print_shop_list(shop_list)


create_shop_list()
