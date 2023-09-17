def compute_values(n) :
  result = []
  for i in range(n):
    if i == 0:
      result.append(3)
    elif i % 2 == 1:
      result.append(i**2)
    else:
      result.append(i * 2)
  return result


if __name__ == '__main__':

  test_cases = int(input())

  for _ in range(test_cases):
    n = int(input())
    result = compute_values(n)
    print(*result)
