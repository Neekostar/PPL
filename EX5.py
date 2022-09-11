print('a b c f1 f2 f3')
for a in range(2):
    for b in range(2):
        for c in range(2):
            f1 = 1 - (a or b)
            f2 = (a != c)
            f3 = f1 and f2
            print("%d" % a, "%d" % b, "%d " % c, "%d " % f1, "%d" % f2, "%d" % f3)
