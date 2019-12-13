#!/usr/bin/python

import sys


def get_perms(n, perm):
    if n > 1:
        # Adding all permutations to a single list
        return get_perms(n - 1, perm + (['rock'])
                         ) + get_perms(n - 1, perm + (['paper'])
                                       ) + get_perms(n - 1, perm + (['scissors']))
    elif n == 1:
        # Putting completed permutations to a sub list
        return [get_perms(n - 1, perm + (['rock'])
                          ), get_perms(n - 1, perm + (['paper'])
                                       ), get_perms(n - 1, perm + (['scissors']))]
    else:
        # return the permutation
        return perm


def rock_paper_scissors(n):
    if n < 1:
        return [[]]
    else:
        return get_perms(n, [])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
