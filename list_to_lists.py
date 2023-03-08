"""
Дан список слов в единственном числе. Верните множество из этих слов в форме 
множественного числа, если они встречаются в списке более одного раза.

Примечание:
Здесь английский язык упрощен, поэтому сконцентрируйтесь только на том, 
добавлять или нет букву “s” к окончаниям слов.

Пример:
pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
"""


def pluralize(a: list) -> set:
    b = set(a)
    c = set()
    for i in b:
        if a.count(i) > 1:
            i += 's'
            c.add(i)
        else:
            c.add(i)
    return c


lst = pluralize(["chair", "pencil", "arm"])
print(lst)
lst = pluralize(["table", "table", "table"])
print(lst)
lst = pluralize(["cow", "pig", "cow", "cow"])
print(lst)
