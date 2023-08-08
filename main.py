# Программа для чтения книги рецептов

cook_book = {}
book = []
with open('Recipes.txt', 'r', encoding='UTF-8') as f:
    f = [line.rstrip() for line in f]
    book = list(f)
for idx, x in enumerate(book):
    if idx == 0 and x != '':
        cook_book.setdefault(book[idx], [])
        y = 2
        for n in range(int(book[idx + 1])):
            res = {'ingredient_name': "", 'quantity': "", 'measure': ''}
            res['ingredient_name'] = ((book[idx+y]).split(' | '))[0]
            res['quantity'] = ((book[idx + y]).split(' | '))[1]
            res['measure'] = ((book[idx + y]).split(' | '))[2]
            cook_book[book[idx]].append(res)
            y += 1
    if x == '':
        cook_book.setdefault(book[idx+1], [])
        y = 3
        for n in range(int(book[idx + 2])):
            res = {'ingredient_name': "", 'quantity': "", 'measure': ''}
            res['ingredient_name'] = ((book[idx + y]).split(' | '))[0]
            res['quantity'] = ((book[idx + y]).split(' | '))[1]
            res['measure'] = ((book[idx + y]).split(' | '))[2]
            cook_book[book[idx+1]].append(res)
            y += 1
print(cook_book)
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for nums in dishes:
        for idx, nams in enumerate(cook_book[nums]):
            if (((cook_book[nums])[idx])['ingredient_name'])  not in shop_list.keys():
                shop_list[((cook_book[nums])[idx])['ingredient_name']] = {}
                (shop_list[((cook_book[nums])[idx])['ingredient_name']])['quantity'] = ((int(((cook_book[nums])[idx])['quantity'])) * person_count)
                (shop_list[((cook_book[nums])[idx])['ingredient_name']])['measure'] = (((cook_book[nums])[idx])['measure'])
            else:
                x = (int(((cook_book[nums])[idx])['quantity']) * person_count)
                (shop_list[((cook_book[nums])[idx])['ingredient_name']])['quantity'] = (int((shop_list[((cook_book[nums])[idx])['ingredient_name']])['quantity']) + x)
    return shop_list
print(get_shop_list_by_dishes(['Омлет', 'Яичница', 'Утка по-пекински'], 14))


