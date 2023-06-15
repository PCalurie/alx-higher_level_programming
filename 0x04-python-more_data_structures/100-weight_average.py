#!/usr/bin/python3
def weight_average(my_list=[]):
    # check if list is empty and return 0 if true
    if not my_list:
        return 0
    # create variables to store sum of weighted scores and the weights
    weighted_scores = 0
    weights = 0
    # loop through each tuple in the list
    for score, weight in my_list:
        # multiply score by weight and add it to weighted_scores
        weighted_scores += score * weight
        # add weight to weights
        weights += weight
    average = weighted_scores / weights
    return average
