import LingVar
class Result:

    def __init__(self,rules):
        self.rules = rules

    def get_subconclusions_for_all_rules(self,*vars:LingVar):
        subconclusions = []
        for rule in self.rules:


            cur_aff = 1
            for name in rule:
                # print(rule[name])
                for var in vars:
                    if name == var.name:

                        cur_aff = min(cur_aff,var.aff_terms[rule[name]][0])
            if cur_aff > 0 :
                subconclusions.append((cur_aff,rule["Key"]))
        subconclusions = [(x,y) for x,y in subconclusions if x > 0]


        return subconclusions
