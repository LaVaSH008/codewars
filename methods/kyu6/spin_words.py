def spin_words(sentence):
    s = []
    for i in sentence.split(" "):
        s.append(i[::-1]) if len(i) >= 5 else s.append(i)

    return ' '.join(s)
