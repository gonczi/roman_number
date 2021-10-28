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

    units = {'IX': 9, 'VIII': 8, 'VII': 7, 'VI': 6, 'IV': 4, 'V': 5, 'III': 3, 'II': 2, 'I': 1}
    for unit in units.keys():
        tail = s[-1 * len(unit):]
        if tail == unit:
            s = s[:-1 * len(unit)]
            res = units[unit]

    units = {'XC': 90, 'LXXX': 80, 'LXX': 70, 'LX': 60, 'XL': 40, 'L': 50, 'XXX': 30, 'XX': 20, 'X': 10}
    for unit in units.keys():
        tail = s[-1 * len(unit):]
        if tail == unit:
            s = s[:-1 * len(unit)]
            res = res + units[unit]

    return res
