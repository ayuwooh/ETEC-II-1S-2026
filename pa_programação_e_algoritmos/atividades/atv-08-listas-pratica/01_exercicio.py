m = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

print("Antes:")
print(m[0])
print(m[1])
print(m[2])

for i in range(3):
    for j in range(3):
        if i == j:
            m[i][j] = 5 * m[i][j]

print("Depois:")
print(m[0])
print(m[1])
print(m[2])
