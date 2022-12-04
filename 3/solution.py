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

# %%
with Path("input.txt").open("r") as f:
    lines =  [x.rstrip("\n") for x in f.readlines()]


# %%
def priority(letter):
    if letter.isupper():
        subtract = 38
    else:
        subtract = 96
    return ord(letter) - subtract


# %%
priorities = []
for line in lines:
    first, second = line[:len(line)//2], line[len(line)//2:]
    common = iter(set(first).intersection(second))
    priorities.append(priority(next(common)))
sum(priorities)

# %%
priorities = []
group = []
counter = 0
for line in lines:
    group.append(line)
    if len(group) == 3:
        common = reduce(lambda x, y: x.intersection(y), group[1:], set(group[0]))
        priorities.append(priority(next(iter(common))))
        group = []
sum(priorities)        
