import math

def cakes(recipe, available):
    posCakes = -1
    for item in recipe:
        if item in available:
            itemCount = math.floor(available[item] / recipe[item])
        else:
            return 0
        if posCakes > itemCount or posCakes == -1:
            posCakes = itemCount


    return posCakes