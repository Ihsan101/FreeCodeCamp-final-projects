from random import randint

all_plays = {}
counter = {"R": "P", "P": "S", "S": "R"}
plays = ["R", "P", "S"]


def listjoin(x):
  a = ""
  for i in x:
    a += i
  return a


def player(prev_play, opponent_history=[]):
  global all_plays

  #Why does if not prev_play not work??? Why Error??? I dont understand why this works but if not doesnt??? Shouldnt empty strings be considered as Null values???
  if prev_play != '':
    opponent_history.append(prev_play)

  if len(opponent_history) <= 6:
    return plays[randint(0, 2)]

  #I do not understand why when I use else statement this doesnt work, but when i manually type it to be greater than 7 it does. Any reason why would be appreciated.

  if len(opponent_history) > 7:
    del opponent_history[0]

  play = listjoin(opponent_history)
  all_plays[play] = all_plays.get(play, 0) + 1

  playlist = listjoin(opponent_history[1:7])
  predict = max([playlist + "R", playlist + "P", playlist + "S"],
                key=lambda key: all_plays.get(key, 0))[-1]

  return counter[predict]
  #Huge thanks to a-mt for making me realize i did not need machine learning for this final project, which is ironic cuz this is supposed to be the first and easiest project but still the one I took the most time on. Anyway. Thanks again for ur time. Have a nice day.
