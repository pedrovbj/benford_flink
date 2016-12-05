import benfordStat

with open("results.txt", "r") as f:
    for path in f:
        print path[:-1] + ":"
        benfordStat.analyse(path[:-1])
        print ""
