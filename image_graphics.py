import matplotlib
import matplotlib.pyplot as plt
from LingVar import Varling
index = 1


def get_graphic(obj:Varling,plt = plt):
    global index
    fig = plt.figure(index)

    axes = fig.add_subplot(111)



    #только для термов
    diap = range(1,100+1)
    axes.grid()

    axes.set_title(obj.name_ling)
    for term in obj.terms:
        y = []
        for i in diap:
            obj.value = i
            obj.affilation_trapeze()
            y += [obj.affilation_terms[term]]


        axes.plot(diap, y,label = term,marker = "h",linewidth = 0.3)
    axes.legend()
    fig.savefig(obj.name_ling)
    index += 1




def get_result(x,y,plt = plt):
    global index
    fig = plt.figure(index)
    axes = fig.add_subplot(111)


    axes.plot(x,y)
    axes.set_title("Итог")
    fig.savefig("result")

