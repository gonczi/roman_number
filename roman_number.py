def parse(s):
    if not isinstance(s, str):
        return -1

    s = s.strip()
    if len(s) == 0:
        return -1

    for ch in list(s):
        if ch not in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
            return -1

    res = 0

    unit_list = [
        {'IX': 9, 'VIII': 8, 'VII': 7, 'VI': 6, 'IV': 4, 'V': 5, 'III': 3, 'II': 2, 'I': 1},
        {'XC': 90, 'LXXX': 80, 'LXX': 70, 'LX': 60, 'XL': 40, 'L': 50, 'XXX': 30, 'XX': 20, 'X': 10},
        {'CM': 900, 'DCCC': 800, 'DCC': 700, 'DC': 600, 'CD': 400, 'D': 500, 'CCC': 300, 'CC': 200, 'C': 100},
        {'MMM': 3000, 'MM': 2000, 'M': 1000},
    ]
    for units in unit_list:
        for unit in units.keys():
            tail = s[-1 * len(unit):]
            if tail == unit:
                s = s[:-1 * len(unit)]
                res = res + units[unit]

    if len(s) > 0:
        return -1

    return res
