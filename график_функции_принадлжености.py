import matplotlib.pyplot as plt
import numpy as np
import affilation as affil

def show_gragh_aff(dotes:list,terms:dict):
    ranges = np.arange(1,100,1)
    plt.ylabel("Вероятность")
    plt.xlabel("Балл")

    extremums = []

    #получаем экстремумы
    for ext in terms.values():
        print(ext[-1])
        extremums.append(ext[-1])

    affil.EPSILENT = len(ranges)//len(extremums)
    print(affil.EPSILENT)
    grapphs = [[ranges,[affil.get_affilation(extremum,x) for x in ranges]] for extremum in extremums]
    for gr in grapphs:
        plt.plot(*gr,linewidth = 2)


    colours = 'rby'
    for i,dot in enumerate(dotes):

        for term in terms:

            x = dot
            y = affil.get_affilation(terms[term][-1], dot)

            plt.plot(x,y, f"{colours[i]}o")
            plt.annotate(f"dot {i} {term}",xy=(x,y),
                         xytext = (x+2,y),
                         )



    plt.show()



