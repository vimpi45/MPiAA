def has_duplicates_fast(_list):
    list_to_set = set(_list)
    if len(list_to_set) != len(_list):
        return True
    return False

def get_duplicates_fast(_list):
    s1 = set()
    s2 = set()
    for elem in (_list):
        if elem in s1:
            s2.add(elem)
        s1.add(elem)
    return list(s2)
