
def parse(s):
    if not isinstance(s, str):
        return -1

    if len(s.strip()) == 0:
        return -1

    return 0