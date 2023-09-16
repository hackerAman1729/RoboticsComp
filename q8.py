def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        data = []
        for _ in range(N):
            name, score = input().split()
            score = float(score)
            data.append((score, name))
        data.sort(key=lambda x: (-x[0], x[1]))
        max_score = data[0][0]
        for score, name in data:
            if score == max_score:
                print(name)
            else:
                break

main()
