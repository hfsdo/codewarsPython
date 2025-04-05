def same_structure_as(original,other):
    print(f"ori: {original}")
    print(f"new: {other}")

    ori_lst = False
    oth_lst = False
    
    if isinstance(original, list):
        ori_lst = True
    
    if isinstance(other, list):
        oth_lst = True

    if ori_lst != oth_lst:
        return False
    
    if not ori_lst:
        return True

    if len(original) != len(other): 
        return False
    
    result = True
    for i in range(0, len(original)):
        if not same_structure_as(original[i], other[i]):
            result = False
    return result
    