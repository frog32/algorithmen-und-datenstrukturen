#! /usr/bin/env python
import exceptions
import itertools

def main(i):
    var = list(itertools.repeat(None,i))
    try:
        next_step(var)
    except exceptions.Exception, data:
        print_solution(data[1])
    
def next_step(solution):
    for i, val in enumerate(solution):
        if val == None:
            next_index = i
            break
    for i in range(len(solution)):
        new_solution = solution[:]
        new_solution[next_index] = i
        if check(new_solution):
            next_step(new_solution)

def check(solution):
    for i, val1 in enumerate(solution):
        if val1 == None:
            return True
        for j, val2 in enumerate(solution[0:i]):
            if val1 == val2:
                return False
            if i-val1 == j-val2:
                return False
            if i+val1 == j+val2:
                return False
    # print_solution(solution)
    # return False
    raise exceptions.Exception('solved', solution)

def print_solution(solution):
    print ''.join('-' for k in range(1+2*len(solution)))
    for i in solution:
        print '|'+'|'.join(('x' if j==i else ' ') for j in range(len(solution))) + '|'
        print ''.join('-' for k in range(1+2*len(solution)))
    
    
if __name__ == '__main__':
    main(8)