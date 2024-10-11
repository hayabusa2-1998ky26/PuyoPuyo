tates = [
    [9, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 0, 9],
    [9, 0, 1, 2, 0, 9],
    [9, 0, 0, 0, 0, 9],
    [9, 9, 9, 9, 9, 9]
]
for x in range(len(tates)):
    for y in reversed(range(len(tates[x]))):
        if tates[x][y] != 0 and tates[x][y] != 9:
            i = -1
            while True:
                i += 1
                print(x, y)
                if tates[x][y + i + 1] != 0:
                    break
                else:
                    tates[x][y + i], tates[x][y + i + 1] = tates[x][y + i + 1], tates[x][y + i]
print(tates)