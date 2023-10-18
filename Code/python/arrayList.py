m = [[1,2], [3,8], [10, 43], [3,4]]
n = [[5,7], [9,5], [1, 44], [3,4]]

jml = []

for i in range(len(m)):
    total = []
    jml.append(total)
    for v in range(len(m[i])):
        total.append(m[i][v] + n[i][v])

print(jml)