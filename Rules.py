from Lingvar import Varling
class Rule:
    def __init__(self,key,rule,result):
        self.rule = rule
        self.key = key
        self.result = result
        self.status = 1


    def get_status(self,*lingvars):
        #получаем истинность одзаключений правила
        for var in lingvars:
            self.status = min(self.status,var.affilation_terms[self.rule[var.name_ling]])
    def __repr__(self):
        return f'''id:{self.key}  status:{self.status:.3f}
'''
