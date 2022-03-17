def get_cook_book(recipes_doc):
    cook_book = {}
    with open(recipes_doc, encoding="utf-8") as op:
        while True:
            dish_name = op.readline().replace("\n", "")
            cook_book[dish_name] = []
            ingredient_count = op.readline()
            for ingredient in range(int(ingredient_count)):
                ingredient_inf = op.readline()
                list_inf = ingredient_inf.split(" | ")
                cook_book[dish_name].append\
                    ({'ingredient_name': list_inf[0], 'quantity': int(list_inf[1]), 'measure': list_inf[2].replace("\n", "")})
            if op.readline() == "":
                break
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ing in cook_book[dish]:
                if ing['ingredient_name'] not in shop_list:
                    shop_list[ing['ingredient_name']] = {list(ing.keys())[2]: list(ing.values())[2].replace("\n", ""),
                                                        list(ing.keys())[1]: int(list(ing.values())[1]
                                                                                 * person_count)}
                else:
                    shop_list[ing['ingredient_name']] = {list(ing.keys())[2]: list(ing.values())[2].replace("\n", ""),
                                                        list(ing.keys())[1]: int(shop_list[ing
                                                        ['ingredient_name']]['quantity']) + (int(list(ing.values())[1]))
                                                                             * person_count}
        else:
            print(f'Блюдо - "{dish}" не найдено!\n')
    return shop_list


def merge_doc(doc1,doc2,doc3, new_doc):
    with open(doc1, encoding="utf-8") as op1:
        d1 = op1.readlines()
    with open(doc2, encoding="utf-8") as op2:
        d2 = op2.readlines()
    with open(doc3, encoding="utf-8") as op3:
        d3 = op3.readlines()
        all_d = [d1, d2, d3]
    priority_len = sorted(all_d, reverse=True)
    with open(new_doc, "w", encoding="utf-8") as wr:
        if priority_len[0] == d1:
            wr.write(doc1 + "\n")
            wr.write(str(len(d1)) + "\n")
            for line in d1:
                wr.write(line)
        elif priority_len[0] == d2:
            wr.write(doc2 + "\n")
            wr.write(str(len(d2)) + "\n")
            for line in d2:
                wr.write(line)
        elif priority_len[0] == d3:
            wr.write(doc3 + "\n")
            wr.write(str(len(d3)) + "\n")
            for line in d1:
                wr.write(line)
        if priority_len[1] == d1:
            wr.write(doc1 + "\n")
            wr.write(str(len(d1)) + "\n")
            for line in d1:
                wr.write(line)
        elif priority_len[1] == d2:
            wr.write(doc2 + "\n")
            wr.write(str(len(d2)) + "\n")
            for line in d2:
                wr.write(line)
        elif priority_len[1] == d3:
            wr.write(doc3 + "\n")
            wr.write(str(len(d3)) + "\n")
            for line in d3:
                wr.write(line)
        if priority_len[2] == d1:
            wr.write("\n" + doc1 + "\n")
            wr.write(str(len(d1)) + "\n")
            for line in d1:
                wr.write(line)
        elif priority_len[2] == d2:
            wr.write("\n" + doc2 + "\n")
            wr.write(str(len(d2)) + "\n")
            for line in d2:
                wr.write(line)
        elif priority_len[2] == d3:
            wr.write("\n" + doc3 + "\n")
            wr.write(str(len(d3)) + "\n")
            for line in d3:
                wr.write(line)


cook_book = get_cook_book('recipes.txt')
print(cook_book)
print()
shop_list1 = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Неизвестное блюдо'], 2)
print(shop_list1)
print()
merge_doc("1.txt", "2.txt", "3.txt", "4.txt")
with open("4.txt", encoding="utf-8") as op:
    for line in op.readlines():
        print(line)