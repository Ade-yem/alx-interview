#!/usr/bin/python3
"""Prime Game"""

scores = {'Maria': 0, 'Ben': 0}
player_choices = {'Maria': 0, 'Ben': 0}
players = list(player_choices.keys())


def is_prime(num):
    """checks if number is prime"""
    if num <= 1:
        return False
    if num <= 3 and num > 1:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def lose(round_list):
    """checks for losers"""
    ind = 0
    lose = False
    index = None
    while lose is False:
        current_player = players[ind]
        for i in range(len(round_list)):
            if len(round_list) == 1 and is_prime(round_list[0]):
                return players[ind - 1]
            if len(round_list) == 1 and not is_prime(round_list[0]):
                return current_player

            if is_prime(round_list[i]):
                index = i
                break
        if index:
            player_choices[current_player] = round_list.pop(index)
            round_list = [
                x for x in round_list if x %
                player_choices[current_player] != 0]
        else:
            lose = True
            return current_player
        ind = (ind + 1) % len(players)


def isWinner(x, nums):
    """returns the winner"""
    for i in range(x):
        round = nums[i]
        round_list = [x for x in range(1, round + 1)]
        player = lose(round_list)
        scores[player] -= 1
    if scores['Ben'] == scores['Maria']:
        return None
    maxi = max(scores['Ben'], scores['Maria'])
    for k in scores.keys():
        if scores[k] == maxi:
            return k
