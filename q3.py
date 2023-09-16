from typing import List

def generate_pattern(n: int) -> List[str]:
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

# Read the number of test cases
test_cases = int(input())

for _ in range(test_cases):
    n = int(input())  # Read the integer N for each test case
    pattern = generate_pattern(n)
    for row in pattern:
        print(row)
