from pool_results import pool_result
from sets import set_dict

def check_score(pl_rlst, sets):
    """Function checks which 5-item set was scored in the particular pooling.
    It also shows 3-item subset which was scored in this pooling"""
    for each_item in sets:
        score = []
        for each_item2 in sets[each_item]:
            if each_item2 in pl_rlst:
                score.append(each_item2)
        if len(score) > 2:
            print (each_item, score)

def generate_combination_3_from_5(set):
    i1 = set_dict[set][0]
    i2 = set_dict[set][1]
    i3 = set_dict[set][2]
    i4 = set_dict[set][3]
    i5 = set_dict[set][4]
    print [i1,i2,i3]
    print [i1,i2,i4]
    print [i1,i2,i5]
    print [i1,i3,i4]
    print [i1,i3,i5]
    print [i1,i4,i5]
    print [i2,i3,i4]
    print [i2,i3,i5]
    print [i2,i4,i5]
    print [i3,i4,i5]

def generate_sets_combination(sets):
    for each_item in sets:
        print "==="+each_item+"==="
        generate_combination_3_from_5(each_item)






