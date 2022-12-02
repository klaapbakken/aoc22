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
import pandas as pd

# %%
with Path("input.txt").open("r") as f:
    lines =  pd.Series([x.rstrip("\n") for x in f.readlines()])

# %%
line_break = lines.str.len() == 0
identity = line_breaks.cumsum()

# %%
(
    identity
    .loc[~line_break]
    .to_frame("identity")
    .assign(
        calories = pd.Series(lines).loc[~line_breaks].astype(int)
    )
    .groupby("identity")
    .agg("sum")
    .max()
)

# %%
(
    identity
    .loc[~line_break]
    .to_frame("identity")
    .assign(
        calories = pd.Series(lines).loc[~line_breaks].astype(int)
    )
    .groupby("identity")
    .agg("sum")
    .sort_values("calories", ascending=False)
    .head(3)
    .calories
    .sum()
)

# %%
