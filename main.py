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


# pol_5010()
def pol_1901():
    alphabet = "0123456789ABCDEF"
    evens = "02468ACE"
    odds = "13579BDF"
    count = 0
    for i in itertools.permutations(alphabet, r=3):
        word = ''.join(i)
        if word[0] != '0' and (word[0] in evens and word[1] in odds and word[2] in evens or
                               word[0] in odds and word[1] in evens and word[2] in odds):
            count += 1
    print(count)


# pol_1901()

def pol_4198():
    alphabet = "КРЫША"
    glas = "ЫА"
    sogl = "КРШ"
    count = 0
    for l in range(3, 6):
        for i in itertools.product(alphabet, repeat=l):
            word = ''.join(i)
            if (word[0] in sogl and len(set(sogl)&set(word[1:])) == 0) or len(set(word) & set(sogl)) == 0:
                if word.count(glas[0]) <= 2 and word.count(glas[1]) <= 2:
                    count += 1
    print(count)


pol_4198()
# x = "КРЫША"
# y = "ЕНПШ"
# print(len(list(x) & list(y)))
