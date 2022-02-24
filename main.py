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
    extremums = affilation.definition_eps(terms)
    print(extremums)
    # print(extremums,affilation.EPSILENT)
    results = {key:[] for key in set(answers)}
    dots_data = []
    for dot in dotes:
        dots_data += [affilation.result_affilation(extremums,dot)]

    for i in range(len(rules)):

        result_for_rule = rules_get_aff.get_aff_for_rule(dots_data,rules[i],i)
        if result_for_rule[0]:
            results[answers[i]] += [result_for_rule]

    #агрегирование предпосылок сделано
    print(results,dots_data,sep='\n')
    ans = None
    chisl = 0
    znam = 0
    for massive in results.values():
        for values in massive:
            chisl += values[0]*values[1]
            znam += values[0]
    print(chisl/znam)

    #Активизация проведена(условно,так как коэффы равны 1)


    # show.show_gragh_aff(list(dotes),terms)
