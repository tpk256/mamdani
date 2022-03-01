

import json
import Result
import LingVar
import sys

# считываем термы
with open("terms.json", encoding="UTF-8") as f:
    terms = json.load(f)

# получаем базу с правилами
with open("rules.json") as f:
    rules_json = json.load(f)

    if __name__ == "__main__":

        # Получаем переменные
        variables = {var: int(dig) for dig, var in zip(sys.argv[1:], [key for key in terms if key != "Result"]) if
                     dig.isdigit()}

        # Представляем каждую переменную в виде независимого объекта
        lingVars = [LingVar.LingVar(name, terms[name], variables[name]) for name in variables]

        # Формируем ренджи для каждого терма у переменной
        for lv in lingVars:
            lv.get_range()

        # Определяем экстремумы и эпсилент
        for lv in lingVars:
            lv.definition_eps_ext()

        # Получаем истинность каждой лингв переменной
        for lv in lingVars:
            lv.ready_aff()
        res = Result.Result(rules_json)
        # посчитали подзаключения
        subconclusions = res.get_subconclusions_for_all_rules(*lingVars)


        #посчитали правила
        var_res = LingVar.LingVar("Result", terms["Result"], -1)
        var_res.get_range()
        var_res.definition_eps_ext()

        base_rule = set()
        for i in range(1,100+1):
            var_res.value = i
            var_res.ready_aff()

            for value in var_res.aff_terms:
                base_rule |= {(value,*var_res.aff_terms[value])}


        # Найдём усеченные функции для каждого правила subconclusions
        values_from_rules = []
        for aff,key_rule in subconclusions:
            find_rule = [rule for rule in rules_json if rule["Key"] == key_rule][-1]["Result"]
            find_range = var_res.terms[find_rule]

            better_range = range(max(1,find_range.start - int(var_res.eps)),min(101,find_range.stop+int(var_res.eps)))

            for i in better_range:
                aff_from_base = [x for x in base_rule if x[0] == find_rule and x[-1] == i][-1][1]


                values_from_rules.append((min(aff,aff_from_base),i))



        #объединение всех правил
        obb_rules = { value:aff for aff,value in sorted(values_from_rules,key = lambda el:el[0])}
        #дефазификация
        # print(obb_rules)
        up = 0
        down = 0

        for value in obb_rules:
            up += value*obb_rules[value]
            down += obb_rules[value]


        print(up/down)

        # Я остановился на моменте с поиск истинности подзаключений операция min
        # print(lingVars[-1])
        # # print(lingVars)


