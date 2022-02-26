import json
import affilation



#получаем базу с правилами
with open("rules.json") as f:

    rules_json = json.load(f)

rules = rules_json["rules"]
answers = rules_json["result"]


#термы короче для выход/вход переменной
terms_out  = {"noob":range(1,21),"trainee ":range(21,41),"master":range(41,61),"pro":range(61,81),"expert":range(81,101)}
terms_in = {"low":range(1,21),"uplow":range(21,41),"mid":range(41,61),"upmid":range(61,81),"high":range(81,100+1)}

dotes = map(int,input().split()) #after dotes -> list(dotes)  dotes will be clear!









if __name__ == "__main__":


    input_data = affilation.Affilation(terms_in)
    input_data.definition_eps(terms_in)

    output_data = affilation.Affilation(terms_out)
    output_data.definition_eps(terms_out)



    dots_data = []


    #получаем степень принадлежности каждого входного четкого элемента ко всем термам
    for dot in dotes:
        dots_data += [input_data.result_affilation(dot)]




    #Следующий Этап  - "пересечение" предпосылок для каждого правила

    value_rules = []
    for i,rule in enumerate(rules):
        value_rules += [input_data.obtaining_prerequisites(dots_data,rule,i)]


    #Выбираем те пересечения,которые > 0

    value_rules_greater_zero = [(aff,i) for aff,i in value_rules if aff > 0]



    partTwo = []
    for mn,index_rule in value_rules_greater_zero:
        temp_dots = terms_out[answers[index_rule]]

        #получаем отсеченную функцию
        temp_dots = [(min(output_data.result_affilation(dot)[answers[index_rule]][0],mn),dot) for dot in temp_dots]
        partTwo += temp_dots



    #Этап 3 композиция

    results = {number:ver for ver,number in sorted(partTwo,key = lambda cartesh:cartesh[0])}
    #фазификация

    up = 0
    down = 0
    for key,value in results.items():
        up += key*value
        down += value

    #четкое число
    print(up/down)

