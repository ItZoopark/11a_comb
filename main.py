import itertools


def f():
    count = 0
    for i in itertools.product('ИВАН', repeat=5):
        word = ''.join(i)
        if word.count('И') > 0:
            count += 1
    print(count)


def pol_5010():
    res = set()
    count = 0
    glas = "ЕА"
    sogl = "ПРТ"
    for i in itertools.permutations('ПРЕПАРАТ'):
        word = ''.join(i)
        for j in range(len(word) - 1):
            if (word[j] in glas and word[j + 1] in glas) or (word[j] in sogl and word[j + 1] in sogl):
                # count += 1
                res.add(word)
                break
    print(len(res))


pol_5010()
