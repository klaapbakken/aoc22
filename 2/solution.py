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
moves = {
    "A" : "Rock",
    "B" : "Paper",
    "C" : "Scissor",
    "X" : "Rock",
    "Y" : "Paper",
    "Z" : "Scissor"
}

move_scores = {
   "Rock" : 1,
    "Paper" : 2,
    "Scissor" : 3
}


# %%
def determine_winner(player_1, player_2):
    if player_1 == player_2:
        return 0
    elif player_1 == "Rock":
        if player_2 == "Paper":
            return 2
    elif player_1 == "Paper":
        if player_2 == "Scissor":
            return 2
    elif player_1 == "Scissor":
        if player_2 == "Rock":
            return 2
    return 1


# %%
(
    lines
    .str
    .split(" ", expand=True)
    .applymap(lambda x: moves[x])
    .assign(
        winner = lambda x: list(map(lambda y: determine_winner(*y), zip(x[0], x[1]))),
        shape_score = lambda x: x[1].map(move_scores),
        result_score = lambda x: (x.winner == 2) * 6 + (x.winner == 0) * 3 + (x.winner == 1) * 0
    )
    .eval("total_score = shape_score + result_score")
    .total_score
    .sum()
)

# %%
outcomes = {
    "X" : 1,
    "Y" : 0,
    "Z" : 2
}


# %%
def determine_move(move, outcome):
    if outcome == 0:
        return move
    elif move == "Rock":
        if outcome == 2:
            return "Paper"
        elif outcome == 1: 
            return "Scissor"
    elif move == "Paper":
        if outcome == 2:
            return "Scissor"
        elif outcome == 1: 
            return "Rock"
    elif move == "Scissor":
        if outcome == 2:
            return "Rock"
        elif outcome == 1: 
            return "Paper"


# %%
(
    lines
    .str
    .split(" ", expand=True)
    .assign(
        move_1 = lambda x: x[0].map(moves),
        outcome = lambda x: x[1].map(outcomes),
        move_2 = lambda x: list(map(lambda y: determine_move(*y), zip(x["move_1"], x["outcome"]))),
        winner = lambda x: list(map(lambda y: determine_winner(*y), zip(x["move_1"], x["move_2"]))),
        shape_score = lambda x: x[1].map(move_scores),
        result_score = lambda x: (x.winner == 2) * 6 + (x.winner == 0) * 3 + (x.winner == 1) * 0
    )
    .eval("total_score = shape_score + result_score")
    .total_score
    .sum()
)

# %%
