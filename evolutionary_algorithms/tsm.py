#! /usr/bin/env python
# coding=utf-8

import random
import exceptions

DISTANCES = (
    ( 0, 15, 22, 31,  1),
    (15,  0, 12, 29,  1),
    (22, 12,  0, 32,  2),
    (31, 29, 32,  0,  1),
    ( 1,  1,  2,  1, -3),
)
# DISTANCES = (
#     ( 0, 15, 22, 31,  1, 13),
#     (15,  0, 12, 29,  1, 16),
#     (22, 12,  0, 32,  2, 25),
#     (31, 29, 32,  0,  1, 12),
#     ( 1,  1,  2,  1, -3, 17),
#     (13, 16, 25, 12, 17,  0),
# )

NAMES = ('FCW', 'H+M', 'Visilab', 'Globus', 'Glühwein')

def main(keep_best_count, mutation_factor, rounds, target, stagnate):
    """tries to find the shortest way"""
    ways = [range(len(DISTANCES))]
    result = {'round':0,'cost':None}
    for i in range(rounds):
        ways = mutate(ways,mutation_factor)
        best = []
        for way in ways:
            best.append((rate(way),way))
        best.sort()
        print "Round %d best way is %s" % (i+1, best[0][0])
        # break if we hit the target
        if best[0][0] <= target:
            print "Hit Target"
            break
        # break if we stagnate to long
        if result['cost'] is None or best[0][0] <result['cost']:
            result['cost'] = best[0][0]
            result['round'] = i+1
        elif result['round'] + stagnate <= i+1:
            print "Stagnate to long"
            break
        ways = list(b[1] for b in best[0:keep_best_count])
    print ""
    print "best found order with cost=%d" % best[0][0]
    print ' '.join(list(NAMES[i] for i in best[0][1]))

def mutate(ways, multiply):
    """shuffles the given ways"""
    mutated=ways[:]
    for way in ways:
        for i in range(multiply):
            new_way = way[:]
            shuffle = [random.randrange(len(way)),random.randrange(len(way)-1)]
            shuffle[1] = shuffle[1] if shuffle[1]<shuffle[0] else shuffle[1]+1
            shuffle.sort()
            mutated.append(way[:shuffle[0]]+[way[shuffle[1]]]+way[shuffle[0]+1:shuffle[1]]+[way[shuffle[0]]]+way[shuffle[1]+1:])
    return mutated

def rate(way):
    """rates the way and gives cost back"""
    cost = 0
    for i in range(len(way)-1):
        cost += DISTANCES[way[i]][way[i+1]]
    return cost

if __name__ == '__main__':
    import sys
    rounds = 10
    keep = 5
    multiply = 3
    target = 0
    stagnate = 10
    try:
        for arg in sys.argv[1:]:
            if arg[0:9] == '--rounds=':
                rounds = int(arg[9:])
            elif arg[0:7] == '--keep=':
                keep = int(arg[7:])
            elif arg[0:11] == '--multiply=':
                multiply = int(arg[11:])
            elif arg[0:9] == '--target=':
                target = int(arg[9:])
            elif arg[0:11] == '--stagnate=':
                stagnate = int(arg[11:])
            elif arg in ('',' '):
                pass
            else:
                raise exceptions.ValueError()
    except:
        print """
This Programm tries to find the shortest way for the traveling salesmen
Usage:
tsm [options]

--keep=NUM      Keep NUM ways after selecting the best. default=5
--multiply=NUM  Mutate every way NUM times. default=3

--rounds=NUM    Run at most NUM rounds. default=10
--target=NUM    Stop trying if the best way is cheaper or equal to NUM.
                default=0 (never stop)
--stagnate=NUM  Stop trying if no better ways were found for NUM rounds.
                default=10
"""
        exit()
            
    main(keep, multiply, rounds, target, stagnate)