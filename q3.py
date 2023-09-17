def generate_pattern(n):
    rows = []
    for i in range(n, 0, -1):
        row = ""
        for j in range(1, i + 1):
            if j % 5 == 0:
                row += "#"
            else:
                row += "*"
        rows.append(row)
    return rows

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())  
    pattern = generate_pattern(n)
    for row in pattern:
        print(row)
