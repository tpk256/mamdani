

EPSILENT = None #она задается автоматически


def result_affilation(extremums,number):
    result = {"low":0,"mid":0,"high":0}

    for ext,key in zip(extremums,result):
        result[key] = get_affilation(ext,number)

    return result

def check_eps(diap, number):
    #Проверка наличия в окрестности
    return abs(diap-number) <= EPSILENT

def get_affilation(diap,number):
    #здесь diap есть экстремумы

    if check_eps(diap,number):
        return (EPSILENT - abs(diap-number)) / EPSILENT,number

    return 0,number

def definition_eps(terms:dict):
    centers = []
    global EPSILENT
    for value in terms.values():
        ext = (value[0] + value[-1]) // 2
        centers.append(ext)




    EPSILENT = sum(len(ranges) for ranges in terms.values()) / len(terms)

    return centers

