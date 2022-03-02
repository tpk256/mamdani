class Varling:
    def __init__(self,terms,value,name_ling):
        self.terms = terms
        self.value = value
        self.name_ling = name_ling
        self.definition_ranges_terms()
        if not (value is None):
            self.affilation_trapeze()
    def definition_ranges_terms(self):
        ranges_terms = {}
        count_terms = len(self.terms)

        #eps для значений,для которых функция принадлжености принимает значения > 0
        step = 100 // count_terms


        #eps для ядра множества терма
        core_step = step // 3 // 2

        for i in range(count_terms):
            if i == 0:
                core = range(1, i * step + 1 + step // 2 + core_step)
                aff = range(1, (i + 1) * step + 1 + core_step)

            elif i == count_terms - 1:
                aff = range(ranges_terms[self.terms[i-1]]["core"][-1], 100 + 1)
                core = range(i * step + 1 + step // 2-core_step,100 + 1 )
            else:
                aff = range(ranges_terms[self.terms[i-1]]["core"][-1], (i + 1) * step + 1+core_step)
                core = range(i * step + 1 + step // 2 - core_step, i * step + 1 + step // 2 + core_step)
            ranges_terms[self.terms[i]] = {"aff":aff,"core":core}
        self.ranges_terms = ranges_terms

    def affilation_trapeze(self):
        self.affilation_terms = {}
        for term_range in self.ranges_terms:
            if self.value in self.ranges_terms[term_range]["aff"]:
                if self.value in  self.ranges_terms[term_range]["core"]:
                    self.affilation_terms[term_range] = 1.
                else:

                    if self.value < self.ranges_terms[term_range]["core"][0]:
                        cur_val = self.value - self.ranges_terms[term_range]["aff"][0]
                        self.affilation_terms[term_range] = cur_val / (self.ranges_terms[term_range]["core"][0]-self.ranges_terms[term_range]["aff"][0])
                    else:
                        cur_val = self.ranges_terms[term_range]["aff"][-1] - self.value
                        self.affilation_terms[term_range] = cur_val / abs(self.ranges_terms[term_range]["aff"][-1] - self.ranges_terms[term_range]["core"][-1])


            else:
                self.affilation_terms[term_range] = 0.






    def __repr__(self):
        data = {key:value for key,value in self.__dict__.items()}
        return f"{data}"