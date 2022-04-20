def find_outlier(integers):
    c1 = [abs(integers[0]) % 2, abs(integers[1]) % 2, abs(integers[2]) % 2]

    if c1.count(1) >= 2:
        return [i for i in integers if abs(i) % 2 == 0][0]
    else:
        return [i for i in integers if abs(i) % 2 == 1][0]
