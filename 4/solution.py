# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3.11 (aoc22)
#     language: python
#     name: aoc22
# ---

# %%
from pathlib import Path
from functools import reduce
from itertools import accumulate

# %%
with Path("input.txt").open("r") as f:
    lines =  [x.rstrip("\n").split(",") for x in f.readlines()]


# %%
def right_inclusive_range(start, stop):
    return range(start, stop + 1)


# %%
n_fully_contained = 0
n_overlap = 0
for assignments in lines:
    pairs = []
    for sections in assignments:
        pairs.append(set(right_inclusive_range(*list(map(int, sections.split("-"))))))
    if (pairs[0].union(pairs[1]) == pairs[0]) or (pairs[1].union(pairs[0]) == pairs[1]):
        n_fully_contained += 1
    if len(pairs[0]) + len(pairs[1]) != len(pairs[0].union(pairs[1])):
        n_overlap += 1
print(n_fully_contained, n_overlap)      

# %%
