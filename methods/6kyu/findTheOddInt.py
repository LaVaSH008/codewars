def find_it(seq):
    unique_seq = list(set(seq))
    for i in unique_seq:
        if seq.count(i) % 2 == 1:
            return i
