def has_duplicates_slow(_list):
    for i in range(len(_list)):              
        for j in range(i + 1, len(_list)):  
            if _list[i] == _list[j]:  
                return True
    return False

def get_duplicates_slow(_list):
    result = set()
    for i in range(len(_list)):              
        for j in range(i + 1, len(_list)):  
            if _list[i] == _list[j]:  
                result.add(_list[i])
    return list(result)