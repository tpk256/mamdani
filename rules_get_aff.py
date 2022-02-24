import functools



def get_aff_for_rule(dote_data,rule,index_rule):

    curr_aff = 1
    for var,condition in zip(dote_data,rule):
        curr_aff = min(curr_aff,var[condition][0])

    return (curr_aff,index_rule)
