import rules_get_aff



class Affilation:

    EPSILENT = None
    def __init__(self,terms):

        self.terms = terms
        if self.EPSILENT is None:
            self.definition_eps(terms)
    def result_affilation(self,number,extremums = None):
        #получаем степень принадлежности к каждому терму
        if extremums is None:
            extremums = self.extremums
        result = {name_terms:0 for name_terms in self.terms}

        for ext,key in zip(extremums,result):
            result[key] = self.get_affilation(ext,number)
#
        return result

    def check_eps(self,diap, number):
        #Проверка на вхождение в эпсилент окрестность

        return abs(diap-number) <= self.EPSILENT

    def obtaining_prerequisites(self,dots_data,rule,index_answer):
        #степень истиности предпосылок для правила
        return rules_get_aff.get_aff_for_rule(dots_data, rule, index_answer)

    def get_affilation(self,diap,number):
        #здесь diap есть экстремумы

        #Получаем степень принадлжености четкого X

        if self.check_eps(diap,number):
            return (self.EPSILENT - abs(diap-number)) / self.EPSILENT,number

        return 0,number

    def definition_eps(self,terms:dict):
        #Определение Эписилент и получение точек экстремумов
        centers = []
        for value in terms.values():
            ext = (value[0] + value[-1]) // 2
            centers.append(ext)




        self.EPSILENT = sum(len(ranges) for ranges in terms.values()) / len(terms)
        self.extremums = centers


