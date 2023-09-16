def process_list(nums):
    print(*nums[::-1])
    print(*[nums[i] + 3 for i in range(0, len(nums), 3)])
    print(*[nums[i] - 7 for i in range(0, len(nums), 5)])
    print(sum(nums[3:8]))

def main():
    T = int(input())
    for _ in range(T):
        _ = int(input())
        nums = list(map(int, input().split()))
        process_list(nums)

main()
