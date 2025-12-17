
m1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
     ]
m2 = (
    (12, 11, 10, 9),
    (8, 7, 6, 5),
    (4, 3, 2, 1)
     )

def matrix_operations(a, b):
    add = []
    sub = []

    for i in range(3):
        add_row = []
        sub_row = []
        for j in range(4):
            add_row.append(a[i][j] + b[i][j])
            sub_row.append(a[i][j] - b[i][j])
        add.append(add_row)
        sub.append(sub_row)

    return add, sub

addition, subtraction = matrix_operations(m1, m2)

print("Addition Matrix:")
for row in addition:
    print(row)

print("\nSubtraction Matrix:")
for row in subtraction:
    print(row)
