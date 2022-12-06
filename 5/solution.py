# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3.11 (aoc22_env)
#     language: python
#     name: aoc22_env
# ---

# %%
from pathlib import Path
import numpy as np
from collections import deque
import re
from collections import namedtuple

instruction = namedtuple("Instruction", ["n", "a", "b"])

def create_stacks(initial_stack):
    stacks = []
    for i in range(initial_stacks.shape[1]):
        stack = deque()
        for crate in initial_stacks[:, i]:
            if crate != " ":
                stack.appendleft(crate)
        stacks.append(stack)
    return stacks

def cratemover(stacks, movements, model):
    crane = deque()
    for movement in movements:
        matches = re.search("move (\d+) from (\d+) to (\d+)", movement).groups()
        instruction_tuple = instruction(*map(int, matches))
        for i in range(instruction_tuple.n):
            crane.append(stacks[instruction_tuple.a - 1].pop())
        for i in range(instruction_tuple.n):
            if model == "9000":
                crate = crane.popleft()
            elif model == "9001":
                crate = crane.pop()
            else:
                raise ValueError
            stacks[instruction_tuple.b - 1].append(crate)
    return "".join([x.pop() for x in stacks])

with Path("input.txt").open(mode="r") as f:
    lines = [x.rstrip("\n") for x in f.readlines()]

line_break = next(i for i, x in enumerate(lines) if len(x) == 0)

index = lines[line_break - 1]
index_positions = [i for i, x in enumerate(index) if x.isnumeric()]

initial_stacks = np.array([[line[idx] for idx in index_positions] for line in lines[:line_break - 1]])
movements = lines[line_break + 1:]

stacks = create_stacks(initial_stacks)
print(cratemover(stacks, movements, "9000"))

stacks = create_stacks(initial_stacks)
print(cratemover(stacks, movements, "9001"))

# %%
