from collections import defaultdict
inputFile = open('input.txt')
ans = 0
for line in inputFile:
    ok = True
    v = defaultdict(int)
    id_, line = line.split(":")
    for event in line.split(";"):
        for balls in event.split(","):
            n, color = balls.split()
            v[color] = max(v[color], int(n))
            if int(n) > {"blue": 14, "red": 12, "green": 13}.get(color, 0):
                ok = False
    score = 1
    for v in v.values():
        score *= v
    ans += score
    # if ok:
    #     ans += int(id_.split()[-1])

print(ans)