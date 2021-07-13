class Number:
    MAX_SAFE_INTEGER = 9007199254740990

num = Number().MAX_SAFE_INTEGER
powerof2 = [0]                                                 # O(1)
for i in range(1, num + 1):                                    # O(N)
    powerof2.append(i**2)                                      # O(log(i)**2)

mapper = {}                                                    # O(1)
for i in range(1, num):                                        # }
    for j in range(1, num):                                    # }O(N^2)
        a = i if i>j else j
        b = i if i<j else j
        if (a, b) not in mapper:
            mapper[(a, b)] = powerof2[i] + powerof2[j]


for k in range(1, num):                                       # }
    for val in mapper:                                        # }O(N^2)
        if mapper[val] == powerof2[k]:
            print(val[0], val[1], k)
            

# Time  Complexity = O(N^2)
# Space Complexity = O(N^2)
