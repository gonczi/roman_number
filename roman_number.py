
def parse(s):
    if not isinstance(s, str):
        return -1

    if len(s.strip()) == 0:
        return -1

    for ch in list(s):
        if ch not in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
            return -1

    return 0