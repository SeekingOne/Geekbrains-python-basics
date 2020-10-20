"""
6) *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
элемента — номер товара и словарь с параметрами (характеристиками товара: название,
цена, количество, единица измерения). Структуру нужно сформировать программно, т.е.
запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
характеристика товара, например название, а значение — список значений-характеристик,
например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

dict_stock_analysis = {
    "Название": set({}),
    "Цена": set({}),
    "Кол-во": set({}),
    "Ед.": set({})
}

idx = 1
stock_list = []
stock_enum_list = []
while True:
    stock_name = input("Введите название товара: ")
    stock_price = float(input("Введите цену товара: "))
    stock_qty = int(input("Введите количество: "))
    stock_uom = input("Введите единицы измерения: ")
    stock_list.append((idx, {
        "Название": stock_name,
        "Цена": stock_price,
        "Кол-во": stock_qty,
        "Ед.": stock_uom
    }))
    choice = input("Прервать ввод? (Y): ")
    if choice == "Y":
        break
    else:
        idx += 1

print("Введены данные:\n", stock_list)

name_set = set({})
price_set = set({})
qty_set = set({})
uom_set = set({})

iterator = 0
while iterator < idx:
    stock_item = stock_list[iterator][1]
    dict_stock_analysis["Название"].add(stock_item["Название"])
    dict_stock_analysis["Цена"].add(stock_item["Цена"])
    dict_stock_analysis["Кол-во"].add(stock_item["Кол-во"])
    dict_stock_analysis["Ед."].add(stock_item["Ед."])
    iterator +=1

print("Аналитика:\n", dict_stock_analysis)
