# https://www.codewars.com/kata/5270d0d18625160ada0000e4

def score(dice):
    rules = {'111': 1000, '1': 100, '5': 50, '222': 200, '333': 300, '444': 400, '555': 500, '666': 600}
    res, count, out = [], 0, 0

    while len(dice):
        res.append(dice.count(dice[0]) * str(dice[0]))
        dice = [x for x in dice if x is not dice[0]]

    while count < len(res):
        if len(res[count]) > 3:
            res.append((len(res[count]) - 3) * res[count][0])
            res[count] = res[count][:-(len(res[count]) - 3)]

        if len(res[count]) == 2:
            res.append(res[count][0])
            res[count] = res[count][:-1]

        if res[count] in rules:
            out += rules[res[count]]

        count += 1

    return out
