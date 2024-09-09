data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    d = 0
    for i in args:
        if isinstance(i, str):
            d += len(i)
        elif isinstance(i, int):
            d += i
        elif isinstance(i, dict):
            for kye, value in i.items():
                d += len(kye)
                d += value
        else:
            d += calculate_structure_sum(*i)
    return d


result = calculate_structure_sum(data_structure)
print(result)
