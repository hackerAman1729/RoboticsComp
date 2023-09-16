# Import reduce module
from functools import reduce


# Function to generate the A.P. series
def generate_AP(a1, d, n):
  # Using list comprehension to generate A.P. series
  AP_series = [a1 + (i - 1) * d for i in range(1, n + 1)]
  return AP_series


# Main function
if __name__ == '__main__':

  # Take the T (test_cases) input
  test_cases = int(input())

  # Process each test case
  for _ in range(test_cases):
    # Read a1, d and n values
    a1, d, n = map(int, input().split())

    # Generate the A.P. series
    AP_series = generate_AP(a1, d, n)
    print(*AP_series)

    # Using lambda and map functions, find squares of terms in AP series
    sqr_AP_series = list(map(lambda x: x**2, AP_series))
    print(*sqr_AP_series)

    # Using lambda and reduce functions, find sum of squares of terms in AP series
    sum_sqr_AP_series = reduce(lambda x, y: x + y, sqr_AP_series)
    print(sum_sqr_AP_series)
