def get_count(sentence):
    s = ['a', 'e', 'i', 'o', 'u']
    return sum([sentence.count(i) for i in s])
