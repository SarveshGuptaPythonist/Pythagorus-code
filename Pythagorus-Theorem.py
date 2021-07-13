class Number:
    MAX_SAFE_INTEGER = 9007199254740990

num = Number().MAX_SAFE_INTEGER
powerof2 = [0]
for i in range(1, num + 1):
    powerof2.append(i**2)

mapper = {}
for i in range(1, num):
    for j in range(1, num):
        a = i if i>j else j
        b = i if i<j else j
        if (a, b) not in mapper:
            mapper[(a, b)] = powerof2[i] + powerof2[j]


for k in range(1, num):
    for val in mapper:
        if mapper[val] == powerof2[k]:
            print(val[0], val[1], k)
