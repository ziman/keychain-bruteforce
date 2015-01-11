#!/usr/bin/env python2

# This program generates various kinds of typos in the given password.
# 
# Useful for generating wordlists in case you mistyped your password twice when setting it.
#

# SUBSTS = {'s': 'ad', 'h': 'jg', ...}
# PWD = 'my secret original password'
from substs import SUBSTS, PWD

def mogrify(pwd):
    guesses = set()

    for i in xrange(len(pwd)):
        x = pwd[i]
        if x in SUBSTS:
            for r in SUBSTS[x]:
                guesses.add(pwd[:i] + r + pwd[i+1:])

    return guesses

def leave_out(pwd):
    guesses = set()

    for i in xrange(len(pwd)):
        guesses.add(pwd[:i] + pwd[i+1:])

    return guesses

guesses = {PWD}

def perform(action):
    global guesses

    sub = set()
    for guess in guesses:
        sub |= action(guess)
    guesses |= sub

perform(mogrify)
perform(mogrify)
#perform(leave_out)
perform(leave_out)

for guess in guesses:
    print guess
