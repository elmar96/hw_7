
def binary_search(list_number, search_number):
    first = 0
    last = len(list_number) - 1
    resultN = False

    while first <= last and not resultN:
        middle = (first + last) // 2
        val = list_number[middle]
        if val == search_number:
            resultN = True
            return resultN
        if val > search_number:
            last = middle - 1
        else:
            last = middle + 1
    return resultN


lst_number = [4485, 3662, 3156, 4443, 3882, 4254, 4048, 4028, 3060, 3685]
value = 3882
result = binary_search(lst_number, value)
if result:
    print(f"Элемент найден!")
else:
    print(f"Элемент не найден!")
