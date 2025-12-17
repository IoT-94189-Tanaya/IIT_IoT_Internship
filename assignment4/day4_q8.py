data = ((10, 10, 10, 12),
        (30, 45, 56, 45),
        (81, 80, 39, 32),
        (1, 2, 3, 4))

avg_list = []

for i in range(len(data[0])):
    total = 0
    for row in data:
        total += row[i]
    avg_list.append(total / len(data))

print(avg_list)

