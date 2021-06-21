

def get_book_cook():
    cook_book = {}
    with open("recipes.txt", encoding="utf-8") as file:
        for line in file:
            key = line.strip()
            my_list = []
            for i in range(int(file.readline().strip())):
                value = file.readline().strip()
                split_value = value.split(' | ')
                my_dict = {'ingridient_name': split_value[0],'quantity': int(split_value[1]), 'measure': split_value[2]}
                my_list.append(my_dict)
            file.readline()
            cook_book[key] = my_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, dishes_dict):
    shop_list = {}
    cook_book = dishes_dict
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list = dict(ingridient)
            new_shop_list['quantity'] *= person_count
            if new_shop_list['ingridient_name'] not in shop_list:
                shop_list[new_shop_list['ingridient_name']] = new_shop_list
            else:
                shop_list[new_shop_list['ingridient_name']]['quantity'] += new_shop_list['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print(f"{shop_list_item['ingridient_name']} {shop_list_item['quantity']} {shop_list_item['measure']}")


def person_count():
    return int(input('Введите кол-во человек: '))


def user_input():
    dishes = input('Введите список блюд через запятую: ').split(', ')
    return [dish.capitalize() for dish in dishes]


print_shop_list(get_shop_list_by_dishes(user_input(), person_count(), get_book_cook()))

