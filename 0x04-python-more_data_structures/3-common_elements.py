#!/usr/bin/pythn3
def common_elements(set_1, set_2):
    result = set()
    for i in set_1:
        if i in set_2:
            result.add(i)
        return result