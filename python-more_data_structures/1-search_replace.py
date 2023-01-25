#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_l = my_list.copy()
    for s, r, in enumerate(my_list):
        if r == search:
            n_l[s] = replace
    return n_l
