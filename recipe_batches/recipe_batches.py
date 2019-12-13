#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):

    if len(recipe) == len(ingredients):

        batches_dict = {}
        for i in recipe:
            batches_dict.update({i: 0})

        for i in recipe:
            num_batch = ingredients[i] // recipe[i]
            batches_dict[i] = num_batch

        batch_min = min(batches_dict.keys(), key=(lambda k: batches_dict[k]))

        return batches_dict[batch_min]
    else:
        return 0


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
