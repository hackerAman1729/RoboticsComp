def is_palindrome(s: str) -> str:
  s = s.lower()
  if s == s[::-1]:
    return "It is a palindrome"
  else:
    return "It is not a palindrome"


def main():
  t = int(input())
  for _ in range(t):
    s = input().strip()
    print(is_palindrome(s))


main()
