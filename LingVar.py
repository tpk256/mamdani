class LingVar:

    def __init__(self,name,terms,value):

        self.name = name
        self.terms = terms
        self.value = value


        self.extremums = None
        self.eps = None
        self.aff_terms = None

    def get_range(self):

        ranges_terms = {}
        count_terms = len(self.terms)
        step = 100 // count_terms
        for i in range(count_terms):
            if i != count_terms - 1:
                ranges_terms[self.terms[i]] = range(i * step + 1, (i + 1) * step + 1)
            else:
                ranges_terms[self.terms[i]] = range(i * step + 1, 100 + 1)


        self.terms = ranges_terms

    def get_affilation(self, diap, number):
        # здесь diap есть экстремум

        # Получаем степень принадлжености четкого X

        if self.check_eps(diap, number):
            return (self.eps - abs(diap - number)) / self.eps, number

        return 0, number

    def ready_aff(self):
        extremums = self.extremums
        number = self.value



        result = {name_terms: 0 for name_terms in self.terms}
        for ext, key in zip(extremums, result):
            result[key] = self.get_affilation(ext, number)

        self.aff_terms = result
        # print(result)


    def check_eps(self,diap, number):
        #Проверка на вхождение в эпсилент окрестность

        return abs(diap-number) <= self.eps



    def definition_eps_ext(self):
        #Определение Эписилент и получение точек экстремумов
        terms = self.terms
        centers = []
        for value in terms.values():
            ext = (value[0] + value[-1]) // 2
            centers.append(ext)

        self.eps = sum(len(ranges) for ranges in terms.values()) / len(terms)
        self.extremums = centers


    def __repr__(self):
        data = {key:value for key,value in self.__dict__.items()}
        return f"{data}"