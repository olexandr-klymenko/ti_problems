from itertools import product
import sys
from typing import List


def func(col: List[int], div) -> int:
    return sum([el * el for el in col]) % div


def maximize_it(colls: List[List[int]], div: int):
    max_res = 0
    for candidate in product(*colls):
        cur_res = func(candidate, div)
        if cur_res > max_res:
            max_res = cur_res
    return max_res


if __name__ == "__main__":
    src_in = sys.stdin.readlines()
    quon_of_lists, divider = src_in[0].split()
    quon_of_lists = int(quon_of_lists)
    divider = int(divider)
    lists = []
    for idx in range(1, quon_of_lists + 1):
        lists.append([int(el) for el in src_in[idx].split()[1:]])
    print(maximize_it(lists, divider))
