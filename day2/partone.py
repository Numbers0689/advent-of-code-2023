
inputFile = open('input.txt')
ans = 0
for line in inputFile:
    ok = True
    id_, line = line.split(":")
    for event in line.split(";"):
        for balls in event.split(","):
            n, color = balls.split()
            if int(n) > {"blue": 14, "red": 12, "green": 13}.get(color, 0):
                ok = False
    if ok:
        ans += int(id_.split()[-1])

print(ans)