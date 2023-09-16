def word_lengths(sentence: str) -> str:
  words = sentence[1:].split()
  lengths = [str(len(word)) for word in words]
  return ",".join(lengths)


def main():
  test_cases = int(input())

  for _ in range(test_cases):
    sentence = input().strip()
    print(word_lengths(sentence))


main()

