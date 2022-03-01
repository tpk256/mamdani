import rules_get_aff



class Affilation:

    EPSILENT = None
    def __init__(self,terms,var_names = None):
        self.var_names = var_names
        self.terms = terms
        if self.EPSILENT is None:
            self.definition_eps(terms)
    def result_affilation(self,number,extremums = None): ###TyT
        #получаем степень принадлежности к каждому терму
        if extremums is None:
            extremums = self.extremums

        results = {}

        if not(self.var_names is None):


            for name in self.var_names:

                result = {name_terms:0 for name_terms in self.terms[name]}

                for ext,key in zip(extremums,result):
                    result[key] = self.get_affilation(ext,number)
                results[name] = result
        else:

            name = "Results"
            result = {name_terms: 0 for name_terms in self.terms}

            for ext, key in zip(extremums, result):
                result[key] = self.get_affilation(ext, number)
            results[name] = result



        print(results)
        return results

    def check_eps(self,diap, number):
        #Проверка на вхождение в эпсилент окрестность

        return abs(diap-number) <= self.EPSILENT

    def obtaining_prerequisites(self,dots_data,rule,index_answer):
        #степень истиности предпосылок для правила
        return rules_get_aff.get_aff_for_rule(dots_data, rule, index_answer,self.var_names)

    def get_affilation(self,diap,number):
        #здесь diap есть экстремумы

        #Получаем степень принадлжености четкого X

        if self.check_eps(diap,number):
            return (self.EPSILENT - abs(diap-number)) / self.EPSILENT,number

        return 0,number



