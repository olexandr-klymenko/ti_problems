# from functools import lru_cache
# import re
# from typing import Iterator
#
# VOWELS_RE = re.compile(r"(A|E|I|O|U)\w*")
#
#
# def substring_generator(string):
#     length = len(string)
#     for idx, char in enumerate(string):
#         yield char
#         for sub_idx in range(idx + 1, length):
#             yield char + string[idx + 1:sub_idx + 1]
#
#
# @lru_cache()
# def match(sub_str):
#     if VOWELS_RE.match(sub_str):
#         return "Kevin"
#     return "Stuart"
#
#
# def classify(sub_collection: Iterator):
#     score = {"Kevin": 0, "Stuart": 0}
#     for sub_str in sub_collection:
#         person = match(sub_str)
#         score[person] += 1
#     return score
#
#
# def minion_game(string):
#     string = string.upper()
#     sub_collection = substring_generator(string)
#     score = classify(sub_collection)
#     if score["Kevin"] == score["Stuart"]:
#         print("Draw")
#     else:
#         winner = max(score, key=score.get)
#         print(f"{winner} {score[winner]}")
def minion_game(string):
    vowels = 'AEIOU'
    Stuart_score, Kevin_score = 0, 0
    length = len(string)
    for start_idx in range(length):
        score = length - start_idx
        if string[start_idx] in vowels:
            Kevin_score += score
        else:
            Stuart_score += score
    if Stuart_score == Kevin_score:
        print('Draw')
    if Stuart_score > Kevin_score:
        print('Stuart {}'.format(Stuart_score))
    if Stuart_score < Kevin_score:
        print('Kevin {}'.format(Kevin_score))


if __name__ == '__main__':
    s = input("Enter string: ")
    minion_game(s)