# import график_функции_принадлжености as show
import affilation
import rules_get_aff
# terms = {"low":range(1,21),"lowmid":range(21,41),"mid":range(41,61),"highmid":range(61,81),"high":range(81,100+1)}

terms = {"low":range(1,31),"mid":range(31,62),"high":range(62,100+1)}
dotes = map(int,input().split()) #after dotes -> list(dotes)  dotes will be clear!

something  = {"bad":range(1,33),"good":range(33,68),"best":range(68,100+1)}
rules = [['low','low'],
         ['mid','low'],
         ['mid','mid'],
         ['low','mid'],
         ['mid','high'],
         ['high',"mid"],
         ['high','low'],
         ['low','high'],
         ['high','high']]

answers = ["bad",'bad','good','bad','best','good','bad','good','best']










if __name__ == "__main__":

    input_data = affilation.Affilation(terms)
    input_data.definition_eps(terms)

    output_data = affilation.Affilation(something)
    output_data.definition_eps(something)

    print(input_data.extremums)

    dots_data = []
#

    #получаем степень принадлежности каждого входного четкого элемента ко всем термам
    for dot in dotes:
        dots_data += [input_data.result_affilation(dot)]




    #Следующий Этап  - "пересечение" предпосылок для каждого правила

    value_rules = []
    for i,rule in enumerate(rules):
        value_rules += [input_data.obtaining_prerequisites(dots_data,rule,i)]

    print(value_rules)
    #Выбираем те пересечения,которые > 0

    value_rules_greater_zero = [(aff,i) for aff,i in value_rules if aff > 0]
    print(value_rules_greater_zero)


    partTwo = []
    for mn,index_rule in value_rules_greater_zero:
        temp_dots = something[answers[index_rule]]
        print(temp_dots)
        #получаем отсеченную функцию
        temp_dots = [(min(output_data.result_affilation(dot)[answers[index_rule]][0],mn),dot) for dot in temp_dots]
        partTwo += temp_dots



    #Этап 3 композиция
    print(partTwo)
    results = {number:ver for ver,number in sorted(partTwo,key = lambda cartesh:cartesh[0])}
    #фазификация

    up = 0
    down = 0
    for key,value in results.items():
        up += key*value
        down += value

    print(up/down)




    # for i in range(len(rules)):
    #
    #     result_for_rule = rules_get_aff.get_aff_for_rule(dots_data,rules[i],i)
    #     if result_for_rule[0]:
    #         results[answers[i]] += [result_for_rule]

    # #агрегирование предпосылок сделано
    # print(results,dots_data,sep='\n')
    # ans = None
    # chisl = 0
    # znam = 0
    # for massive in results.values():
    #     for values in massive:
    #         chisl += values[0]*values[1]
    #         znam += values[0]
    # print(chisl/znam)

    #Активизация проведена(условно,так как коэффы равны 1)


    # show.show_gragh_aff(list(dotes),terms)
