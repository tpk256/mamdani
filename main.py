



rules_json.sort(key = lambda rule: rule['Key'])



def unpack_rules(froms:dict) -> "Возвращает rules,result":
    rules = []
    results = []

    for rule in froms:
        keys_rule = [key for key in terms if key not in ("Key","Result")]

        rules.append([rule[key] for key in keys_rule])


        results.append(rule["Result"])
    return rules,results




def get_ranges_for_var(vars_and_terms):
    vars = {}

    for var in vars_and_terms:
        ranges_terms = {}
        count_terms = len(vars_and_terms[var])
        step = 100 // count_terms
        for i in range(count_terms):
            if i != count_terms - 1:
                ranges_terms[vars_and_terms[var][i]] = range(i * step + 1, (i + 1) * step + 1)
            else:
                ranges_terms[vars_and_terms[var][i]] = range(i * step + 1, 100 + 1)
        vars[var] = ranges_terms

    return vars


# names_dotes = list(terms)[:-1]
# print(names_dotes)

#Получаем ренджи для выходной лингв переменной
# terms_out = get_ranges_for_var({"Result":terms["Result"]})["Result"]


rules,answers = unpack_rules(rules_json)

#термы  для выход/вход переменной

terms_out = get_ranges_for_var(terms)
terms_in = {key:terms_out[key] for key in terms_out if key != "Result"}
terms_out = terms_out["Result"]

# print(terms_out,terms_in)


if __name__ == "__main__":

    # Получаем точки

    dotes = [80,74,44,57,80,80]
    input_data = affilation.Affilation(terms_in,list(terms_in))
    # input_data_disp =
    input_data.definition_eps(terms_in)

    output_data = affilation.Affilation(terms_out)
    output_data.definition_eps(terms_out)
    # print(input_data.EPSILENT,output_data.EPSILENT) #OK


    dots_data = []


    #получаем степень принадлежности каждого входного четкого элемента ко всем термам
    for dot in dotes:
        print(dot)
        dots_data += [input_data.result_affilation(dot)]
    # print(dots_data)






    #Следующий Этап  - "пересечение" предпосылок для каждого правила

    value_rules = []
    for i,rule in enumerate(rules):
        value_rules += [input_data.obtaining_prerequisites(dots_data,rule,i)]


    #Выбираем те пересечения,которые > 0

    value_rules_greater_zero = [(aff,i) for aff,i in value_rules if aff > 0]


    partTwo = []
    print(value_rules_greater_zero)



    for mn,index_rule in value_rules_greater_zero:
        temp_dots = terms_out[answers[index_rule]]

        #получаем отсеченную функцию
        temp_dots = [(min(output_data.result_affilation(dot)["Results"][answers[index_rule]][0],mn),dot) for dot in temp_dots]
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

