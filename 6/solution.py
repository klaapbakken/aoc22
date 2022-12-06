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

# %%
with Path("input.txt").open(mode="r") as f:
    input_ = np.array(list(f.read()))

# %%
input_


# %%
def detect_marker(n):
    sliding_window = np.arange(n)
    detected = False
    i = n
    while not detected:
        detected = (len(set(input_[sliding_window])) == n)
        if detected:
            print(i)
        else:
            i += 1
            sliding_window += 1


# %%
detect_marker(4)

# %%
detect_marker(14)
