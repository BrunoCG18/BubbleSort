values = [7, 1, 5, 3, 10, 13, 2, 4, 8]
size_list = len(values) - 1
c = 0
okloop = False

while True:
    if okloop == True:
        break
    ok = 0
    for x in range(0, size_list):
        y = x + 1
        if values[x] > values[y]:
            values[x], values[y] = values[y], values[x]
            ok += 1

    if ok == 0:
        okloop = True
        break
    c += 1

print(values)
print(f'We needed {c} iterations')
