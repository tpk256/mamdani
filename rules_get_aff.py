#


def get_aff_for_rule(dote_data,rule,index_rule,var_names):
    # print(dote_data)
    # print(rule)
    curr_aff = 1

    for var,dotl,condition in zip(var_names,dote_data,rule):

        curr_aff = min(curr_aff,dotl[var][condition][0])


    return (curr_aff,index_rule)
